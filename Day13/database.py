LIST_HUMAN = [  
                {'age': 48, 'id': '1', 'name': 'name 1'},
                {'age': 94, 'id': '2', 'name': 'name 2'},
                {'age': 49, 'id': '3', 'name': 'name 3'},
                {'age': 58, 'id': '4', 'name': 'name 4'},
                {'age': 32, 'id': '5', 'name': 'name 5'},
                {'age': 39, 'id': '6', 'name': 'name 6'},
                {'age': 45, 'id': '7', 'name': 'name 7'},
                {'age': 43, 'id': '8', 'name': 'name 8'},
                {'age': 57, 'id': '9', 'name': 'name 9'},
                {'age': 97, 'id': '10', 'name': 'name 10'},
                # {'age': 35, 'id': '11', 'name': 'name 11'},
                # {'age': 64, 'id': '12', 'name': 'name 12'},
                # {'age': 14, 'id': '13', 'name': 'name 13'},
                # {'age': 61, 'id': '14', 'name': 'name 14'},
                # {'age': 93, 'id': '15', 'name': 'name 15'},
                # {'age': 30, 'id': '16', 'name': 'name 16'},
                # {'age': 84, 'id': '17', 'name': 'name 17'},
                # {'age': 39, 'id': '18', 'name': 'name 18'},
                # {'age': 44, 'id': '19', 'name': 'name 19'},
                # {'age': 77, 'id': '20', 'name': 'name 20'}
            ]

LIST_MOCKAPI = [
    {"name" : "Nhan", "url" : "https://60e1a9c05a5596001730f19e.mockapi.io/human"},
    {"name" : "Tien", "url" : "https://60e1a9d05a5596001730f1aa.mockapi.io/humann"},
    {"name" : "Thao", "url" : ""},
    {"name" : "Duc", "url" : ""},
    {"name" : "Hung", "url" : ""},
    {"name" : "Nguyen Anh", "url" : "https://60e1a9545a5596001730f19b.mockapi.io/human"},
    {"name" : "The Anh", "url" : ""},
    {"name" : "Son", "url" : ""},
    {"name" : "Minh", "url" : ""},
    {"name" : "Thanh", "url" : "https://60e484a35bcbca001749ea92.mockapi.io/human"},
    {"name" : "Quang", "url" : ""},
]

class Database:
    def get(self, id=None):
        if id:
            for human in LIST_HUMAN:
                if int(human["id"]) == int(id):
                    return human

        return LIST_HUMAN

    def get_mockapis(self):
        return LIST_MOCKAPI