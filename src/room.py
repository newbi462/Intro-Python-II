# Implement a class to hold room information. This should have name and
# description attributes.

"""
class Room:
    def __init__(self, name, description): # constructor
        self.name = name
        self.description = description
"""
class Room:
    def __init__(self, name, description, item_list=None):
        self.name = name
        self.description = description
        self.n_to = "none" # would be more por to use None python resereved word
        self.s_to = "none"
        self.e_to = "none"
        self.w_to = "none"
        if item_list == None:
            self.item_list = []
        else:
            self.item_list = item_list
        self.give_error = True
    def get_item(self, item):
        for i in self.item_list:
            if i.item_name == item:
                self.item_list.remove(i)
