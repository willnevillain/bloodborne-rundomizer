class Hunter:
    
    def __init__(self, name, items):
        self.name = name
        self.items = {}
        self.req_stats = {}

        self.add_items(items)
        self.calculate_stats()

    def add_items(self, items):
        plural = ''
        if isinstance(items['trick'], list) and isinstance(items['firearm'], list):
            plural = 's'
        self.items['trick' + plural]  = items['trick']
        self.items['firearm' + plural]  = items['firearm']
        
        armor = ['head', 'chest', 'hand', 'leg']
        for piece in armor:
            self.items[piece] = items[piece]

    def calculate_stats(self):
        stats = ['str', 'skl', 'blt', 'arc']
        trick_stats = {}
        firearm_stats = {}

        
        if 'tricks' in self.items:
           for stat in stats:
               trick_stats[stat] = max(int(self.items['tricks'][0][stat + '_req']), 
                                       int(self.items['tricks'][1][stat + '_req']))
        else:
           for stat in stats:
               trick_stats[stat] = int(self.items['trick'][stat + '_req'])
        

        if 'firearms' in self.items:
           for stat in stats:
               firearm_stats[stat] = max(int(self.items['firearms'][0][stat + '_req']), 
                                         int(self.items['firearms'][1][stat + '_req']))
        else:
           for stat in stats:
               firearm_stats[stat] = int(self.items['firearm'][stat + '_req'])

        
        for stat in stats:
            self.req_stats[stat + '_req'] = max(trick_stats[stat], firearm_stats[stat])

    def display_info(self):
        for item in self.items:
            if isinstance(self.items[item], list):
                names = []
                for each in self.items[item]:
                    names.append(each['name'])
                print(item + ': ' + str(names))
            else:
                print(item + ': ' + self.items[item]['name'])
        for stat in self.req_stats:
            print('Required ' + stat[:3].title() + ': ' + str(self.req_stats[stat]))
