from tinydb import TinyDB
from os import listdir

def map_item_to_json(item_type, item_subtype, item_details):
    if item_type == 'armor':
        return {
            'name': item_details[0].strip(),
            'set': item_details[1].strip(),
            'plus': item_details[2].strip(),
            'chalice': item_details[3].strip(),
            'fashion': item_details[4].strip(),
            'subtype': item_subtype
        }
    if item_type == 'weapon':
        return {
            'name': item_details[0],
            'str_req': item_details[1].strip(),
            'skl_req': item_details[2].strip(),
            'blt_req': item_details[3].strip(),
            'arc_req': item_details[4].strip(),
            'plus': item_details[5].strip(),
            'chalice': item_details[6].strip(),
            'subtype': item_subtype
        }

def populate_table(db, item_file):
    table = db.table(item_file[:-4])
    with open(item_file) as f:
        item_type = f.readline().strip()
        item_subtype = f.readline().strip() #e.g. head, hand, firearm, etc.
        for row in f:
            if row[0] != '#':
                item_details_list = row.split(',')
                item = map_item_to_json(item_type, item_subtype, item_details_list)
                table.insert(item)

def main():
    db = TinyDB('db.json')
    db.purge_tables()

    all_item_data_files = []
    for data_file in listdir():
        if data_file.endswith('.txt'):
            all_item_data_files.append(data_file)
    
    for item_file in all_item_data_files:
        populate_table(db, item_file)


if __name__ == '__main__':
    main()
