import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="139271",
    database="restaurant" 
)

c = conn.cursor()

# Execute the query
query = """
SELECT 
    o.order_id,
    o.total_price,
    u.user_name,
    u.phone_num,
    d.dish_name,
    orq.quantity
FROM 
    Orders o
INNER JOIN 
    User u ON o.user_id = u.user_id
INNER JOIN 
    Order_req orq ON o.order_id = orq.order_id
INNER JOIN 
    Dish d ON orq.dish_id = d.dish_id
ORDER BY 
    o.order_id;
"""
c.execute(query)

results = c.fetchall()

for row in results:
    order_id, total_price, user_name, phone_num, dish_name, quantity = row
    
    print("-" * 40) 
        
    print(f"Order ID: {order_id}")
    print(f"Total Price: {total_price}")
    print(f"User: {user_name} ({phone_num})")
    print("Dishes:")

    print(f"  - {dish_name} x{quantity}")

print("-" * 40)

c.close()
conn.close()