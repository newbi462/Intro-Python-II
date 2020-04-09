# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, location, item_list=None): # constructor
        self.player_name = player_name
        self.location = location # may need to inhaerit from Room using suppe
        if item_list == None:
            self.item_list = []
        else:
            self.item_list = item_list
        self.give_error = True
    def get_item(self, item):
        for i in self.item_list:
            if i.item_name == item:
                self.item_list.remove(i)
    def __str__(self):
        return f"{self.player_name} you are {self.location}"
