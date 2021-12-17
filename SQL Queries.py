'''Queries for sqlite to Postgres pipeline'''

create_table='''CREATE TABLE test_table IF NOT EXSISTS (
                id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                number INT);''' 
 

insert_data='''INSERT INTO test_table(name, number)
    VALUES ('A row name', 6), ('Another row',72);'''


select_all = '''SELECT * FROM test_table;'''

get_characters='''
SELECT * FROM charactercreator_character;
'''

get_character_table = '''PRAGMA table.info(charactercreator_character);'''

create_character_table = '''
CREATE TABLE IF NOT EXISTS charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULl,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
);
'''
