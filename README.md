## Requirements:
Run the code below to install the necessary modules.

    pip install -r requirements.txt

## Database init
1. set the database in __init__.py file.
2. GRANT ALL PRIVILEGES ON SCHEMA public TO **user**;
3. run schema_drop.sql, schema.sql and schema_ins.sql in your database

Example: 
    psql -d{database} -U{user} -W -f schema.sql

## Running flask

go to the correct directory and say

    python3 run.py

