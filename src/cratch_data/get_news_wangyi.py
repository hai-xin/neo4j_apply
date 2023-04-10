import json
import time

from lxml import etree

import requests

from src import MyPymysqlPool

base_url = "https://news.163.com/special/cm_war/?callback=data_callback"
xpath_title = "/html/body/div[2]/div[2]/h1/text()"
xpath_title1 = "/html/body/div[3]/div[1]/h1/text()"
xpath_title2 = '//*[@id="container"]/div[1]/h1/text()'

xpath_content = "/html/body/div[2]/div[2]/div[3]/div[2]/p/text()"
xpath_content1 = "/html/body/div[3]/div[1]/div[3]/div[2]/p/text()"
xpath_content2 = '//*[@id="content"]/div[2]/p/text()'

xpath_source = "/html/body/div[2]/div[2]/div[2]/a[1]/text()"
xpath_source1 = '//*[@id="container"]/div[1]/div[2]/a[1]/text()'
xpath_source2 = '/html/body/div[2]/div[1]/div[2]/a[1]/text()'

xpath_new_link = "/html/body/div[2]/div[2]/div[4]/div[2]/ul/li/a/@href"
xpath_new_link1 = "/html/body/div[2]/div[2]/div[4]/div[3]/div/div/a/@href"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    ,
    'Cookie': '_ntes_nuid=1839cee0911ca48910fda14d0fe84e12; BAIDU_SSP_lcr=https://www.baidu.com/link?url=i4EAHiNwJZe4XwlBUXlxn8Cqyac3PXg8A6f_s4DgJpG&wd=&eqid=b74e7fde001c86fd000000036430c667; __bid_n=1875e8714116a69c0f4207; _antanalysis_s_id=1680918218387; UserProvince=%u5317%u4EAC; WM_NI=mPzC7Mhb5yND%2Fr66M7sTbxVZT9jiNU8gRcwnv%2FgzFfHSzj%2FJZQX1XIHh8fTEWn%2BZ%2FgM6q%2BhOCo9g%2F3cCsIiXg950EC%2FRf8X5cd%2F%2FzZJSYJwD2kHl4bO9%2FNdjLSB6VDDRUXM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaaee4994eda4a5f7668beb8fb6d54a978e8a83c46bab95bc89c9498791b990ee2af0fea7c3b92aaf90b6a4b647acbefb9acd50edaefad7d03db18cae99d55298e7a68acd5ffcb99e84f666b6f1a99bc56e8c8db68bae429a8f98d2db438cb8f887d74f95b2e5bbae6d8feabfcceb4581b1f788ae39a19dbdaaec54a5e7fbd1c849ed8eaad9db3fa1bce1d0f9528a8d97abf650f2b5888db76a8de7e1afe762908d8ed7d550888e9bb9d037e2a3; WM_TID=dBjlBwVl05RFBBEVEUbUL3OsxYDVehs9; pver_n_f_l_n3=a; FPTOKEN=AxL3UBqpBqNyDDTOnGRpaeBgBk4xi+lgPzNVo0QD6ch/l2mbnmJ7YmDJMyXFlYJKoTeOCV8qm4ezJISPGKNCFwalF7vrLo+TsDTv4f5IVZWF/KEro++1SQ5ivnnh4tN0HbjexusSKZQeExEy8STQBRgDYkyGfizPIHSdUtdTnF7nxiEkDnw7C6cwTSmOgvtEBvtwRZr90y7myCfPwyf7Ylzw1MN4wzLF+YTmQIZE1/92O/ZEamGyavHADjVNKbZK9NgOjxMyJDHDjdthvopReXP/VvI+UReVyzu00Qk1zjiqDkBBrHZpkay0KuPEYBz76tZf1K7vK1ErK0vrOA8AEfs4D9LBhz2ncBCzAAL8fVyGDZKf66iGlIa4m66LB5zzhKBYY+a7n8Al9C5sLPMiag==|BJR3XHmT8cW6AVEDZSUkqtXwQyPOrdb+gL3fmV3+MmM=|10|87fa3f6d26ea7362fd994aa836aab350; ne_analysis_trace_id=1680920366256; NTES_PC_IP=%E5%8C%97%E4%BA%AC%7C%E5%8C%97%E4%BA%AC; vinfo_n_f_l_n3=0852ceff460dd325.1.1.1680918122412.1680919791697.1680920371298',
    # 'Referer': 'https://www.baidu.com/link?url=O8Icaz2zeI7Zb18eJRM034wgs-E4TuaXpV0nJeeaIy3&wd=&eqid=aed05fb000018fd30000000362f39cd3'
}


def get_link(links):
    new_links, new_datas = [], []
    for link in links:
        print(link)
        res_detail = requests.get(url=link.strip('"'), headers=headers).text
        html = etree.HTML(res_detail)
        new_link = html.xpath(xpath_new_link)
        new_link1 = html.xpath(xpath_new_link1)
        query_sql = f"""select * from news where news_id='{link}'"""
        print("==>> ", query_sql)
        res = mysql.getOne(query_sql)
        if not res:
            print(res)
            for xpath_title_ in [xpath_title, xpath_title1, xpath_title2]:
                news_title = html.xpath(xpath_title_)
                if news_title:
                    break

            for xpath_content_ in [xpath_content, xpath_content1, xpath_content2]:
                news_content = html.xpath(xpath_content_)
                if news_content:
                    break

            # news_content = ",".join(news_content)
            for ele in news_content:
                if not isinstance(ele, str):
                    news_content.remove(ele)
                else:
                    ele.replace("\\n", "").strip(" ")
            news_content = ",".join(news_content)

            for news_source_ in [xpath_source, xpath_source1, xpath_source2]:
                news_source = html.xpath(news_source_)
                if news_source:
                    break

            new_links.extend(new_link)
            new_links.extend(new_link1)
            print(news_title)
            print(news_content)
            print(news_source)
            if news_title and news_content and news_source:
                news_title = news_title[0]
                news_source = news_source[0]
                new_datas.append((link, news_title, news_content, "网易新闻_" + news_source, "军事"))
            # new_datas = save_data(link, news_title, news_content, news_source, new_datas)
    print(new_datas)
    if new_datas:
        mysql.insertMany(inset_sql, new_datas)
        mysql.dispose()
        print("插入数据")
    if new_links:
        print("递归")
        get_link(new_links)


while True:
    mysql = MyPymysqlPool()
    resp = requests.get(url=base_url).text
    resp = resp.split('"tlink":')[1:]

    inset_sql = "insert into news(news_id,title,content,source,news_type) values(%s,%s,%s,%s,%s)"

    links = [element.split(",")[0] for element in resp]
    if links:
        get_link(links)
    time.sleep(3)
    print("----")
