from tinydb import TinyDB

def main():
    db = TinyDB('db.json')
    sets = set()
    for table_name in db.tables():
        table = db.table(table_name)
        if table == '_default':
            continue
        for item in table.all():
            if 'set' not in item:
                break
            if item['set'] == 'NO_SET':
                continue
            sets.add(item['set'])
    print(sorted(sets))
    print(len(sets))
            

if __name__ == '__main__':
    main()
