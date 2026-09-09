# Write your MySQL query statement below
select Product.product_name , Sales.year , Sales.price from Product RIGHT JOIN Sales ON Product.product_id = Sales.product_id;