from psycopg2 import connect
h = 'localhost'
u = 'postgres'
p = '123456789'
db = 'evos_database'
def get_categories():
    try:
        conn = connect(host = h, user = u, password = p,database = db)
        cursor = conn.cursor()
        sql = '''
                SELECT category_name,category_id FROM categories
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return res
    except Exception as e:
        print(e)
def get_products_by_categories(id):
    try:
        conn = connect(host = h, user = u, password = p,database = db)
        cursor = conn.cursor()
        sql = f'''
                SELECT product_name,product_id FROM products
                WHERE category_id = {id}
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return res
    except Exception as e:
        print(e)

