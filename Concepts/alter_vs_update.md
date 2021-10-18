## Alter Table <br>
    - Alter is a DDL. add column/modify/delete/
    - In general, when changing the structure/definition of the table.

## Update table
    - Update values in a column or something. 
    
```sql 
UPDATE Salary 
SET 
sex= (
    case when (sex='f') 
    then 
        'm' 
    else 
        'f'
    end
);
```

