# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, location): # constructor
        self.player_name = player_name
        self.location = location # may need to inhaerit from Room using suppe
    def __str__(self):
        return f"{self.player_name} you are {self.location}"
