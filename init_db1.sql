mysql> CREATE DATABASE liu_db;
Query OK, 1 row affected (0.03 sec)

mysql> USE liu_db;
Database changed
mysql> CREATE TABLE etudiants (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(50),
    -> prenom VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.09 sec)

mysql> INSERT INTO etudiants (nom, prenom) 
    -> VALUES ('Iman', 'Cheibany'),
    -> ('Mariem', 'Vall Abdy'),
    -> ('Fatimatou', 'Cheikh Sidi'),
    -> ('Lalla', 'Yacoub');
Query OK, 4 rows affected (0.03 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM etudiants;
+----+-----------+-------------+
| id | nom       | prenom      |
+----+-----------+-------------+
|  1 | Iman      | Cheibany    |
|  2 | Mariem    | Vall Abdy   |
|  3 | Fatimatou | Cheikh Sidi |
|  4 | Lalla     | Yacoub      |
+----+-----------+-------------+
4 rows in set (0.00 sec)

mysql> UPDATE etudiants SET nom = 'Mina' WHERE id = 4;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM etudiants;
+----+-----------+-------------+
| id | nom       | prenom      |
+----+-----------+-------------+
|  1 | Iman      | Cheibany    |
|  2 | Mariem    | Vall Abdy   |
|  3 | Fatimatou | Cheikh Sidi |
|  4 | Mina      | Yacoub      |
+----+-----------+-------------+
4 rows in set (0.00 sec)

mysql> DELETE FROM etudiants WHERE id = 4;
Query OK, 1 row affected (0.03 sec)

mysql> SELECT * FROM etudiants;
+----+-----------+-------------+
| id | nom       | prenom      |
+----+-----------+-------------+
|  1 | Iman      | Cheibany    |
|  2 | Mariem    | Vall Abdy   |
|  3 | Fatimatou | Cheikh Sidi |
+----+-----------+-------------+
3 rows in set (0.00 sec)