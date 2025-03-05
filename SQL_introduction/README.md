# SQL - Introduction

## 📌 Description
This project is an introduction to SQL and MySQL. It helps you learn the basics of relational databases and execute essential SQL queries.

---

## 🎯 Learning Objectives
By the end of this project, you will be able to:
- Understand what a **database** and a **relational database** are.
- Explain what **SQL** means and what **MySQL** is.
- Create a database in **MySQL**.
- Understand the differences between **DDL (Data Definition Language)** and **DML (Data Manipulation Language)**.
- Use basic SQL commands:
  - `CREATE`, `ALTER`, `DROP` (DDL)
  - `SELECT`, `INSERT`, `UPDATE`, `DELETE` (DML)
- Execute **subqueries** and use **SQL functions**.

---

## 📖 Useful Resources
- [What is Database & SQL?](https://www.geeksforgeeks.org/introduction-to-database-sql/)
- [MySQL Server Installation](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)
- [Basic MySQL Tutorial](https://www.mysqltutorial.org/)
- [MySQL Cheat Sheet](https://devhints.io/mysql)

---

## ⚙️ Installing MySQL
### On Ubuntu 20.04 / 22.04
```bash
# Update package list
sudo apt update

# Install MySQL
sudo apt install mysql-server

# Check installation
mysql --version

# Start MySQL service
sudo service mysql start

# Connect to MySQL server
mysql -uroot
```

---

## 📌 Running SQL Queries
You must write your SQL queries in `.sql` files with **explanatory comments**.

### Example:
```sql
-- Show all databases
SHOW DATABASES;
```

### Running an SQL script:
```bash
cat file.sql | mysql -uroot -p
```

---

## 📜 Rules to Follow
✅ All files must end with a **new line**.
✅ All **SQL keywords** must be in **UPPERCASE** (`SELECT`, `WHERE`, ...).
✅ A **README.md** file is mandatory.
✅ Add **comments** in your SQL files to explain your queries.

---

## ✅ Quiz and Validation
At the end of the project, a quiz will validate your knowledge of:
- The basics of relational databases
- The use of SQL and MySQL
- Writing basic SQL queries                                      
