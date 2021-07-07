LIST_HUMAN = [
    {"id" : 30 , "name" : "name 1", "age" : 23},
    {"id" : 31 , "name" : "name 2", "age" : 56},
    {"id" : 32 , "name" : "name 3", "age" : 54},
    {"id" : 33 , "name" : "name 4", "age" : 67},
    {"id" : 34 , "name" : "name 5", "age" : 23},
    {"id" : 35 , "name" : "name 6", "age" : 20},
    ]

class Database:
    def get(self, id=None):
        print(id)
        if id:
            for human in LIST_HUMAN:
                if human["id"] == id:
                    return human

        return LIST_HUMAN