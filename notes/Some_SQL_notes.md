#### LintCode 2544
> We want to insert a message to the teachers table for Feng Qingyang with email feng.qingyang@163.com, age 37 and nationality CN, 
> but the teachers table is locked with a read lock, write an SQL statement to insert the information.

Table created by 
```sql
DROP TABLE IF EXISTS `teachers`;
        CREATE TABLE `teachers`  (
            `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(64) NOT NULL,
            `email` VARCHAR(64) ,
            `age` INT UNSIGNED NOT NULL,
            `country` VARCHAR(32) NOT NULL,
            PRIMARY KEY (`id`)
        );
```
Solution:
```sql
-- 对 teachers 表上读锁，不要删除该代码 --
LOCK TABLES teachers READ;

-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
UNLOCK TABLES;

INSERT INTO teachers (name, email, age, country)
VALUES('Feng Qingyang', 'feng.qingyang@163.com' ,37, 'CN');
```
