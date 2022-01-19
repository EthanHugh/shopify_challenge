I completed this challenge using the Django REST Framework, which implements the basic CRUD functionality. Using the Django REST Framework, I was able to create API endpoints from which one can manipulate the database. The project is deployed on Heroku, and can be accessed with the following URL:
https://ethanhughbackendchallenge.herokuapp.com/api/
The information is stored in a postgreSQL database through Heroku

To view or create Inventory items, you can visit https://ethanhughbackendchallenge.herokuapp.com/api/inventory/ 
This URL will display the following:
![inventory_api](https://user-images.githubusercontent.com/84813627/150213629-793832e9-4677-458d-bba8-8ccc6441ad54.png)
The form below can be used to store new inventory items, or through HTTP POST methods on any frontend application (mobile and web).
Note that Inventory ID and Name must be unique.

I decided to implement the Warehouse feature as the extra challenge, and can be accessed through
https://ethanhughbackendchallenge.herokuapp.com/api/warehouse/
This URL will display the following:
![warehouse_api](https://user-images.githubusercontent.com/84813627/150214393-8bcb4575-eda4-477e-b297-64d624efaef1.png)
The form below can be used to store warehouse information, or through HTTP POST methods like for inventory.
Note that Warehouse ID and Name must be unique.

In order to assign specific Inventory items to a warehouse, we can do it through the URL:
https://ethanhughbackendchallenge.herokuapp.com/api/relationship/
This URL will show:
![relationship_api](https://user-images.githubusercontent.com/84813627/150214812-89732b02-f6e4-4cbc-a8c3-f6c9139ad235.png)
The form at the bottom will present two dropdowns that allow you to select one warehouse and one inventory item, to 'link' them.
One inventory item can be stored in many warehouses and one warehouse can store many inventory items, making this a relational database.

This page also allows for filtering with the filters button, where you type the name of a Warehouse (it must be exact, for example typing 'US' will not display results for 'USA')
![filter](https://user-images.githubusercontent.com/84813627/150215072-b4b87dd5-d6e0-4e91-a357-3d4a1bbf7d76.png)
This will display all the inventory items stored in the specified warehouse, as shown above.


It is easier to manipulate the database through the admin page, where the username is 'superuser' and password is '123'. I am making this information public because there is nothing sensitive stored.
You can access admin through the URL https://ethanhughbackendchallenge.herokuapp.com/admin/
![admin](https://user-images.githubusercontent.com/84813627/150216014-1afb263f-3481-41ab-8095-06b95e8babd4.png)
You can click on any table to view the information there.

For Inventory, you can edit any existing information by clicking on it, or add more inventory items by clicking on ADD INVENTORY on the top right.
![inventory_admin](https://user-images.githubusercontent.com/84813627/150216108-86152ab8-50dc-4f11-ace8-a26817927c39.png)
(The same applies for warehouses)

The Warehouse to Inventory Relationships table shows the warehouse and inventory links, which has a filter on the right to view items for one specific warehouse.
![relationship_admin](https://user-images.githubusercontent.com/84813627/150216354-b3683110-ecbe-4a83-b7ae-83b968af49aa.png)

Thank you for reading this lengthy tutorial!






