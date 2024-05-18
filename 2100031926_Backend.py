import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gokusolos$1",
    database="safertek"
)

# Create cursor
cursor = db_connection.cursor()

# Sample Queries
queries = [
    "SELECT * FROM Customers;",
    "SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31';",
    "SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, Customers.Email FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID;",
    "SELECT Products.ProductName FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE OrderItems.OrderID = 1;",
    "SELECT Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID;",
    "SELECT Products.ProductName, SUM(OrderItems.Quantity) AS TotalOrdered FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Products.ProductID ORDER BY TotalOrdered DESC LIMIT 1;",
    "SELECT DATE_FORMAT(Orders.OrderDate, '%Y-%m') AS Month, COUNT(Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSales FROM Orders JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE YEAR(Orders.OrderDate) = 2023 GROUP BY DATE_FORMAT(Orders.OrderDate, '%Y-%m');",
    "SELECT Customers.FirstName, Customers.LastName FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID HAVING SUM(Products.Price * OrderItems.Quantity) > 1000;"
]

try:
    # Execute each query
    for index, query in enumerate(queries, start=1):
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"Query {index}:")
        for row in results:
            print(row)
        print()

except mysql.connector.Error as err:
    print("Error executing query:", err)

finally:
    # Close cursor and database connection
    if cursor:
        cursor.close()
    if db_connection:
        db_connection.close()
