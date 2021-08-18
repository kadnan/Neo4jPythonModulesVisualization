from neo4j import GraphDatabase


def query(q, return_result=False):
    driver = get_neo_connection('neo4j', 'pwd')
    session = driver.session(database='neo4j')
    if return_result:
        return session.run(q)
    else:
        session.run(q)
        return None


def create_relationship(start, end, label='USED_BY'):
    q = "MATCH (a:Module),(b:Module) WHERE a.name = '{}' and b.name = '{}' CREATE (a)-[r:{}]->(b) RETURN type(r)".format(
        start, end, label)
    query(q)


def create_node(name):
    # Create New or return exisitng one
    q = "MERGE (m:Module {{name: '{}' }}) RETURN m.name".format(name)
    query(q)

    # q = "CREATE (m:Module {{name: '{}' }})".format(name)
    # query(q)


def get_neo_connection(user, pwd):
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=(user, pwd))
    return driver
