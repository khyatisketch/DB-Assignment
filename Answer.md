DB-Assignment

Answering the questions based on the shown diagram.
1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

Ans. The "Product" entity has a foreign key category_id that references the id field of the "Product_Category" entity. This indicates a one-to-many relationship between the two entities, where one product category can have multiple products associated with it, but each product can only be associated with one product category.

In other words, the "Product_Category" entity is the parent entity, and the "Product" entity is the child entity. Each row in the "Product_Category" table can have zero or more corresponding rows in the "Product" table that reference it via the category_id field.

This relationship allows you to associate each product with a specific product category and helps you to organize your products based on categories. For example, you could have a "Clothing" product category and have multiple products associated with it, such as "T-Shirt", "Hoodie", and "Pants".

2. How could you ensure that each product in the "Product" table has a valid category assigned to it?

Ans. To ensure that each product in the "Product" table has a valid category assigned to it, you could implement a few strategies in the database design:

     1. Foreign Key Constraint: You can add a foreign key constraint on the category_id column in the product_inventory table, referencing the id column in the product_category table. This will enforce referential integrity, ensuring that each product category ID in the product_inventory table corresponds to an existing category in the product_category table.
 
        Here's an example of how you could define this constraint in SQL:

          ALTER TABLE product_inventory
          ADD CONSTRAINT fk_product_category
          FOREIGN KEY (category_id) REFERENCES product_category(id);

     2. Application-level checks: Before inserting a new product or updating an existing product, your application could validate that the assigned category ID is valid. You could implement this by querying the product_category table to check if the category ID exists before performing the product update or insert.
        By implementing one or both of these strategies, you can help ensure that each product in the "Product" table has a valid category assigned to it.

