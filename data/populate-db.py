from tinydb import TinyDB

def populateWeapons(db, file_name, table_name):
    table = db.table(table_name)
    with open(file_name) as f:
        for row in f:
            if row[0] != '#':
                columns = row.split(',')
                item = {
                    'name': columns[0],
                    'str_req': columns[1].strip(),
                    'skl_req': columns[2].strip(),
                    'blt_req': columns[3].strip(),
                    'arc_req': columns[4].strip(),
                    'plus': columns[5].strip(),
                    'chalice': columns[6].strip()
                }
                table.insert(item)

def populateArmor(db, file_name, table_name):
    table = db.table(table_name)
    with open(file_name) as f:
        for row in f:
            if row[0] != '#':
                columns = row.split(',')
                item = {
                    'name': columns[0].strip(),
                    'set': columns[1].strip(),
                    'plus': columns[2].strip(),
                    'chalice': columns[3].strip(),
                    'fashion': columns[4].strip()
                }
                table.insert(item)

def main():
    db = TinyDB('db.json')
    db.purge_tables()

    populateWeapons(db, 'trick-weapons.txt', 'trick_weapons')
    populateWeapons(db, 'firearms.txt', 'firearms')
    populateArmor(db, 'head-attire.txt', 'head_attire')
    populateArmor(db, 'chest-attire.txt', 'chest_attire')
    populateArmor(db, 'hand-attire.txt', 'hand_attire')
    populateArmor(db, 'leg-attire.txt', 'leg_attire')

if __name__ == '__main__':
    main()
