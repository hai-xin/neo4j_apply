from src import MyPymysqlPool
from src.neo4j_graph.service import neo4j_service

mysql = MyPymysqlPool()

node_datas = {"country": [],
              "province": [],
              "city": [],
              "city_region": []}

relation_datas = {"country-province": [],
                  "province-city_region": [],
                  "city_region-city": []}

# 查询国家
sql = """select * from regions where id like '%000000' order by id"""
countries = mysql.getAll(sql)

# 查询省份
for country in countries:
    country.update({"label": "country"})
    node_datas["country"].append(country)
    print(country)
    sql = f"""select * from regions where id like '{str(country["id"])[:3]}%' and SUBSTR(id,6,4)='0000' and id !='{country["id"]}'"""
    # print(sql)
    provinces = mysql.getAll(sql)
    # print(provinces)
    # 根据省份标识获取市区
    if provinces:
        for province in provinces:
            relation_datas["country-province"].append(
                [country, province, "country-province"]
            )
            province.update({"label": "province"})
            node_datas["province"].append(province)
            sql = f"""select * from regions where id like '{str(province["id"])[:5]}%' and id !='{country["id"]}' and '{str(province["id"])[-2:]}'='00' order by id"""
            city_regions = mysql.getAll(sql)
            # 根据市区标识获取城市
            for city_region in city_regions:
                relation_datas["province-city_region"].append(
                    [province, city_region, "province-city_region"]
                )
                city_region.update({"label": "city_region"})
                if city_region not in node_datas["city_region"]:
                    node_datas["city_region"].append(city_region)
                sql = f"""select * from regions where id like '{str(city_region["id"])[:7]}%' and id !='{city_region["id"]}' order by id """
                cities = mysql.getAll(sql)
                if cities:
                    for city in cities:
                        city_region_city = [
                            city_region, city, "city_region-city"
                        ]
                        if city_region_city not in relation_datas["city_region-city"]:
                            relation_datas["city_region-city"].append(city_region_city)
                        city.update({"label": "city"})
                        if city not in node_datas["city"]:
                            node_datas["city"].append(city)

# print(node_datas)
# tmp_data = []
# for k,items in node_datas.items():
#     print(k)
#     print(len(items))
#     for item in items:
#         if item not in tmp_data:
#             tmp_data.append(item)
#             neo4j_service.create_node(item)

tmp_data_relation = []
for k,items in relation_datas.items():
    print(k)
    print(len(items))
    for item in items:
        if item not in tmp_data_relation:
            tmp_data_relation.append(item)
            neo4j_service.create_relation(item)