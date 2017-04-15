from random import choice
from tinydb import TinyDB


class Data:

    db = TinyDB('db.json')

    def grow_pair(self):
        """ Pick a random capital and country pair from db """
        pair_dict = choice(self.db.all())
        country = pair_dict.get('country')
        capital = pair_dict.get('capital')
        return country, capital

    def countries(self):
        """ Assign the country to correct_answer and the capital to hint """
        correct_answer, hint = self.grow_pair()
        return correct_answer, hint

    def capitals(self):
        """ Assign the country to hint and the capital to correct_answer """
        hint, correct_answer = self.grow_pair()
        return correct_answer, hint




# get a country and a capital from the db
# sort based on quiz type
# return them



