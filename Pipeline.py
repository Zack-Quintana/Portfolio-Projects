import psycopg2
from queries import *
import sqlite3

#Connect to Postgres DB

DBN = "ezfttctb"
USER = "ezfttctb"
PW = "WvZF19mAOJ0xEcb3kRqGPdASMtQB3NPL"
HOST = "kashin.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=DBN,user=USER, password=PW, host=HOST)
pg_curs = pg_conn.cursor()

#Connect to SQLite DB

sl_conn=sqlite3.connect('rpg_db.sqlite3')
sl_curs=sl_conn.cursor()

def execute_query_sl(curs, conn, query):
    results = curs.execute(query).fetchall()
    return results

def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results
if __name__ =='__main__':
    #print(execute_query(curs, create_table))
    #print(execute_query(curs, insert_data))
    #print(execute_query(curs, select_all))
    characters = execute_query_sl(sl_curs, sl_conn, get_characters)
    #print(characters)
    execute_query_pg(pg_curs, pg_conn, create_character_table)
    
    for character in characters:
        insert_statement = '''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {}'''.format(character[1:])
        execute_query_pg(pg_curs, pg_conn, create_character_table)