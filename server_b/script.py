import mysql.connector as mysql

db = mysql.connect(
    host='server_a',
    user='root',
    password='root',
    port=3306,
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE users_db")
cursor.execute("USE users_db")
cursor.execute("CREATE TABLE User (UserID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `Name` VARCHAR(255), Address VARCHAR(255))")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (1, 'Adam', 'Jasminowa 22/1, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (2, 'Mariusz', 'Jasminowa 22/2, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (3, 'Cezary', 'Jasminowa 22/3, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (4, 'Narzena', 'Jasminowa 22/4, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (5, 'Piotr', 'Jasminowa 22/5, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (6, 'Izabela', 'Jasminowa 22/6, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (7, 'Monika', 'Jasminowa 22/7, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (8, 'Janusz', 'Jasminowa 22/8, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (9, 'Aurelia', 'Jasminowa 22/9, Wroclaw');")
cursor.execute("insert into users_db.User (UserID, `Name`, Address) values (10, 'Sam', 'Jasminowa 22/10, Wroclaw');")

db.commit()
