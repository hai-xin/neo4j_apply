from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph("http://192.168.163.120:7474", auth=("neo4j", "123456abc"), name="neo4j")


class Neo4jService():
    def __int__(self):
        super(self).__init__()

    def appl_cql(self, cql):
        res = graph.run(cql)
        return res

    def fetch_one(self):
        pass

    def save_data(self, node):
        graph.create(node)

    def create_node(self, data):
        # node = Node(label='book', name='黄帝内经')
        node = Node(data["label"], **data)
        self.save_data(node)

    def create_relation(self, data):
        node1 = graph.run(f"""match(n:`{data[0]["label"]}`) where n.id={data[0]["id"]} return n limit 1""")
        node2 = graph.run(f"""match(n:`{data[1]["label"]}`) where n.id={data[1]["id"]} return n limit 1""")
        node1 = node1.data()
        node2 = node2.data()
        if node1 and node2:
            relation = Relationship(node1[0]['n'], data[2], node2[0]['n'])
            self.save_data(relation)


neo4j_service = Neo4jService()

# data = [{'id': 100000000, 'name': '中国', 'first_spell': 'zg', 'full_spell': 'zhongguo', 'label': 'country'},
#         {'id': 100110000, 'name': '北京市', 'first_spell': 'bj', 'full_spell': 'beijing', 'label': 'province'},
#         'country-province']
# neo4j_service.create_relation(data)


# # 头实体
# head = Node("regoin", name='邯郸市')
# # 尾实体
# tail = Node("regoin", name='河北省')
# # 头尾实体关系
# entity = Relationship(head,"属于", tail)
# # 创建实例
# graph.create(entity)
