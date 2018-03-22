from tinydb import TinyDB
from os import listdir

def map_item_to_json(item_type, item_details):
    if item_type == 'armor':
        return {
            'name': item_details[0].strip(),
            'set': item_details[1].strip(),
            'plus': item_details[2].strip(),
            'chalice': item_details[3].strip(),
            'fashion': item_details[4].strip()
        }
    if item_type == 'weapon':
        return {
            'name': item_details[0],
            'str_req': item_details[1].strip(),
            'skl_req': item_details[2].strip(),
            'blt_req': item_details[3].strip(),
            'arc_req': item_details[4].strip(),
            'plus': item_details[5].strip(),
            'chalice': item_details[6].strip()
        }

def populate_table(db, name):
    table = db.table(name)
    with open(name + '.txt') as f:
        item_type = f.readline().strip()
        for row in f:
            if row[0] != '#':
                item_details_list = row.split(',')
                item = map_item_to_json(item_type, item_details_list)
                table.insert(item)

def main():
    db = TinyDB('db.json')
    db.purge_tables()

    all_item_data_files = []
    for data_file in listdir():
        if data_file.endswith('.txt'):
            all_item_data_files.append(data_file)
    
    for item_file in all_item_data_files:
        populate_table(db, item_file[:-4])


if __name__ == '__main__':
    main()
