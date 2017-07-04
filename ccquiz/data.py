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
        """ The capital is the answer and the country is the hint """
        ans = self.capital
        hint = self.country
        return ans, hint

    @property
    def countries(self):
        """ The country is the answer and the capital is the hint """
        ans = self.country
        hint = self.capital
        return ans, hint

    def gimmie(self, kind):
        """
        pass in either 'capitals' or 'countries' (this is done automatically for you by the Quiz class)
        returns the corresponding answer and hint
        :param kind:
        :return:
        """
        if kind == 'capitals':
            return self.capitals
        elif kind == 'countries':
            return self.countries
        else:
            ValueError("Not a valid kind of quiz")