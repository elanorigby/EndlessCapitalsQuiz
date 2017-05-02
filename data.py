from random import choice
from tinydb import TinyDB


class Data:

    db = TinyDB('db.json')

    def __init__(self):
        """ Pick a random capital and country pair from db """
        pair_dict = choice(self.db.all())
        self.country = pair_dict.get('country')
        self.capital = pair_dict.get('capital')

    @property
    def capitals(self):
        ans = self.capital
        hint = self.country
        return ans, hint

    @property
    def countries(self):
        ans = self.country
        hint = self.capital
        return ans, hint

    def gimmie(self, kind):
        if kind == 'capitals':
            return self.capitals
        elif kind == 'countries':
            return self.countries
        else:
            ValueError("Not a valid kind of quiz")
