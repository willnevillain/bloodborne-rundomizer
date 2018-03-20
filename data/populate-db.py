from tinydb import TinyDB

def populateWeapons(db, file_name, table_name):
    table = db.table(table_name)
    with open(file_name) as f:
        for row in f:
            if row[0] != '#':
                columns = row.split(',')
                item = {
                    'name': columns[0],
                    'str_req': columns[1],
                    'skl_req': columns[2],
                    'blt_req': columns[3],
                    'arc_req': columns[4],
                    'plus': columns[5],
                    'chalice': columns[6].rstrip()
                }
                table.insert(item)

def populateArmor(db, file_name, table_name):
    table = db.table(table_name)
    with open(file_name) as f:
        for row in f:
            if row[0] != '#':
                columns = row.split(',')
                item = {
                    'name': columns[0],
                    'set': columns[1],
                    'plus': columns[2],
                    'chalice': columns[3]
                }
                table.insert(item)

def main():
    db = TinyDB('db.json')
    db.purge_tables()

    populateWeapons(db, 'trick-weapons.txt', 'trick_weapons')
    populateWeapons(db, 'firearms.txt', 'firearms')

if __name__ == '__main__':
    main()
