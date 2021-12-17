import sqlite3
import pymongo

pw = 'YLYYGYiFMOnSNZf2'
dbn = 'test'
usn = 'blah'

def create_sql_conn(source_db='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(source_db)
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()

def create_mdb_conn(password, dbname, user, collection_name):
    client_mg = pymongo.MongoClient('mongodb+srv://{}:{}@cluster0.fngna.mongodb.net/{}?retryWrites=true&w=majority'.format(usn,pw,dbn))
    db = client_mg[dbn]
    col = db[collection_name]
    return col

def character_doc_creation(collection, character_list):
    for char in character_list:
        character_doc = {
            'name':char[1],
            'level':char[2],
            'exp':char[3],
            'hp':char[4],
            'strength':char[5],
            'intelligence':char[6],
            'dexterity':char[7],
            'wisdom':char[8],
        }
        collection.insert_one(character_doc)

if __name__ == '__main__':
    sl_conn = create_sql_conn()
    sl_curs = sl_conn.cursor()
    get_characters = '''
    SELECT * FROM charactercreator_character;
    '''
    characters = execute_query(sl_curs, get_characters)
    col = create_mdb_conn(pw, dbn, usn, 'characters')
    character_doc_creation(col, characters)