## SQL

1. **RDBMS vs DBMS** <br>
rdbms stores data in form of tables with given schema and relations can be defined on these tables. 

2. **Primary Key** <br>
implicitly non-null and unique. a table can have only one primary key but the key can be made up of multiple columns.
```sql
CREATE TABLE Students (   /* Create table with multiple fields as primary key */
   ID INT NOT NULL,
   LastName VARCHAR(255),
   FirstName VARCHAR(255) NOT NULL,
   CONSTRAINT PK_Student
   PRIMARY KEY (ID, FirstName)
);
```

3. **Foreign Key** <br>
field(s) in a table that are primary keys in some other table. 
```sql
CREATE TABLE Students (
   ID INT NOT NULL PRIMARY KEY,
   Name VARCHAR(255),
   LibraryID INT FOREIGN KEY (Library_ID) REFERENCES Library(LibraryID)
);
```

4. **Index** <br>
provides quick lookup of data in column(s) of table at cost of additional memory and writes. 
```sql
CREATE INDEX index_name
ON table_name (column_1, column_2);
```

5. **Delete vs Truncate** <br>
Delete is DML: can be used with ```where```. <br>
Truncate is DDL: faster and can't be rolled back. (doesn't remove the table) <br>
Drop: drops the table/database. 

6. **Stored Procedure** <br>
subroutine available to applications that access a rdbms. if user doesnt have access to table, can still execute stored procedure of that table. 
```sql
DELIMITER $$
CREATE PROCEDURE FetchAllStudents()
BEGIN
SELECT *  FROM myDB.students;
END $$
DELIMITER ;
```



7. **Copy of Table with same schema?** <br>
```sql
SELECT * INTO Students_copy
FROM Students WHERE 1 = 2;
```