# Implement a class to hold room information. This should have name and
# description attributes.

"""
class Room:
    def __init__(self, name, description): # constructor
        self.name = name
        self.description = description
"""
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = "none" # would be more por to use None python resereved word
        self.s_to = "none"
        self.e_to = "none"
        self.w_to = "none"
