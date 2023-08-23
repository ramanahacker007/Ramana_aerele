# Ramana_aerele_project.

I used mysql and flask for this project database connection.

Frontend: Html & Css

Backend : Python , Python-flask framework , Mysql

NOTE: I used users table name instead of company name

**The tables : initialy tables are empty......**

items(id,item_name,seller_id,qty)

![Screenshot (210)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/728fd8d4-0e16-4b45-912a-16b0154e70f1)

purchases(purchase_id,buyer_id,seller_id,item_id,quantity,rate,amount,timestamp)

![Screenshot (211)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/12ed2b15-b3f8-453d-a2d5-2dec672f01f8)

sales(sales_id,buyer_id,seller_id,item_id,quantity,rate,amount,timestamp)

![Screenshot (212)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/7205aaf3-e385-429d-b69c-5b2ecd45ef32)

users(id,username,password,cash_balance)

![Screenshot (213)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/05d271b7-539f-4e66-b7e8-8fc77a90f565)

After i created table in mysql , i used visual code to run this project.

**The project demo**

This is the layout.html page , here i added login and register button, if new user he will register else login.

![Screenshot (233)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/77c3ac90-da10-4ba4-93a9-85103597d306)

This is the login.html page, 

![Screenshot (216)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/4c015bb9-3a8c-4df1-9504-e7d88eaa5876)

This is the register.html page, here you can also add your initial deposit amount for buying and selling.

![Screenshot (217)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/5731bc1b-fe80-4c66-b6dc-968e8424c6df)

This is the Home.html page, i just registered and logged as user1 and my initial deposit is 1000$

![Screenshot (218)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/981ad6e4-cacf-4a58-a6db-cd859f8c2472)

Now i gonna to add items , the added items will be display in home page for all the users , if you want to login as another user you can logout. After i clicking add items button this page will show. I gonna add two items

![Screenshot (219)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/c86b7df1-5e4e-447a-88e9-11ac4bd6a081)

The rsults will be shown in home page

![Screenshot (220)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/8841f7c1-2e64-4844-9de1-c59f041e85b9)

You can also view added items by clicking view_added_items

![Screenshot (221)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/5b1bfedd-9f06-4c1d-90fe-a9911888e1b5)

Just check the cash balance , i am not buyed or selled any items 

![Screenshot (222)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/e5f9ce8d-1cc9-472f-a300-a2ced638c2f6)

Now i login as user2 and gonna purchase. then i will show the cash balance of both users after transaction and showing you user1 sales record and user2 purchase record and items remaining

User2 home page and his cash balance is 1000$

![Screenshot (223)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/acfd5716-173f-4aee-8a2e-baee5087e2e4)

user two purchase two pencil 30 *2 = 60 amount and one bag 100 * 1 = 100 , then total amount is 160$ . This 160 will add to user1 and reduce in user2.

The view_purchases for user2 shows:

![Screenshot (224)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/0b80b08f-d878-425c-8d11-9922c2b0124f)

Cash balance for user2: 160 is reduced from 1000

![Screenshot (225)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/c2ba07b0-033b-413f-bc39-fd4ed6bc7762)

The view_sales for user1 shows:

![Screenshot (226)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/9a3a9e31-d4cf-4866-815f-09c266f36513)

cash balance for user1: 160 is added from 1000:

![Screenshot (227)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/53cb3b87-b6df-4de8-a68f-5facd74bfbe7)

Now you can also check the added_items record , two pencil is reduced and one bag is reduced initialy their quantity is 7 and 5 but now 5 and 4:

![Screenshot (228)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/aecfb4fa-f05a-483c-b8eb-458d08592c49)

This is the simple process i created , It took me very hard to complete this because i didn't know about flask before this project.

**Now i done three purchases and show you the updated mysql database**

![Screenshot (229)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/22606d23-bae0-4937-9b27-37558add7fe0)

![Screenshot (230)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/9178de43-6cf3-4299-9a52-459e370977a5)

![Screenshot (231)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/05851cf2-3546-42a5-9269-b89fbdc01490)

![Screenshot (232)](https://github.com/ramanahacker007/Ramana_aerele/assets/81798536/fbbbee48-c31f-4318-84ff-fd7bcde8a95b)



**I also added sql file you can import it in mysql......**






