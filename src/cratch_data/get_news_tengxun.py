# import re
# import time
import datetime
import json
import time

import requests
from lxml import etree
from src import MyPymysqlPool

base_url = "https://r.inews.qq.com/web_feed/getPCList"
xpath_title = "/html/body/div[3]/div[1]/h1/text()"
xpath_content = "/html/body/div[3]/div[1]/div[1]/div[2]/p/text()"

headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    ,
    'Cookie': 'eas_sid=b136p3q453X1I4h2w1Z5s6D3k2; fqm_pvqid=2912c15f-a1c2-4860-a5fc-cbea585f84da; iip=0; LW_sid=A1i6g3O4x391w4X3O302H1o0n1; LW_uid=f106s3T4S331G482A175G6v2a0; o_cookie=1239676778; pac_uid=1_1239676778; pgv_pvid=6531328166; ptcz=d1c49617e8b14221591f2d667eed59fcbe7ffe2faa4d6cfd6ba76c2134218717; RK=f47AQDUaOd; tvfe_boss_uuid=4a9af621bc6cbdbe; _clck=3085157109|1|f3p|0; pgv_info=ssid=s3679942986; ts_last=news.qq.com/; ts_refer=www.baidu.com/link; ts_uid=3167588418; ad_play_index=38'
    ,
    'Referer': 'https://www.baidu.com/link?url=O8Icaz2zeI7Zb18eJRM034wgs-E4TuaXpV0nJeeaIy3&wd=&eqid=aed05fb000018fd30000000362f39cd3'
}

body = {
    "qimei36": "0_076a4ba56a2ad",
    "forward": "1", "base_req": {"from": "pc"},
    "flush_num": 10,
    "channel_id": "news_news_mil",
    "device_id": "0_076a4ba56a2ad",
    "is_local_chlid": ""
}

while True:
    mysql = MyPymysqlPool()
    resp = requests.post(url=base_url, json=body, headers=headers)
    resp = resp.json()
    ids = []
    if resp.get("data"):
        for new_ietm in resp["data"]:
            query_sql = f"""select * from news where news_id='{new_ietm["id"]}'"""
            res = mysql.getOne(query_sql)
            if not res and new_ietm["id"] not in ids:
                url = "https://new.qq.com/rain/a/" + new_ietm["id"]
                datas = requests.get(url).text
                html = etree.HTML(datas)
                news_title = html.xpath(xpath_title)
                news_content = html.xpath(xpath_content)
                inset_sql = "insert into news(news_id,title,content,source,news_type) values(%s,%s,%s,%s,%s)"
                content = ""
                for i in news_content:
                    content += i.strip()
                new_datas = []
                new_datas.append((new_ietm["id"], news_title[0], content, "腾讯新闻", "军事"))
                ids.append(new_ietm["id"])
                mysql.insertMany(inset_sql, new_datas)
                print(new_ietm["id"])
        if ids:
            sql = "select max(id) as id from news"
            max_id = mysql.getOne(sql)
            mysql.dispose()
            time.sleep(1)
            print(datetime.datetime.now())
            if max_id["id"] > 1000000:
                break
