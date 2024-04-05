from sqlite3 import Cursor
from sql_connection import get_sql_connection

def get_all_products(connection):
   
    cursor = connection.cursor()

    query = "SELECT p.product_id, p.name, u.uom_name, p.price_per_unit FROM products as p inner join uom as u on p.uom_id = u.uom_id order by p.product_id;"

    cursor.execute(query)

    response = []

    for (product_id, name, uom_name, price_per_unit) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name' : name,
                'uom_name' : uom_name,
                'price_per_unit' : price_per_unit,

            }
        )


    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products (name, uom_id, price_per_unit) values (%s, %s, %s);")

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from products where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 18))
