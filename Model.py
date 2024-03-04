import json
from json import JSONEncoder

class EncodeStudent(JSONEncoder): 
        def default(self, o): 
            return o.__dict__ 
        

class Competitor:
    def __init__(self, name, category, country, email):
        self.name = name
        self.category = category
        self.country = country
        self.email = email

class Competition:
    def __init__(self, name, date, competitors, categories, tables):
        self.name = name
        self.date = date
        self.competitors = competitors
        self.categories = categories
        self.tables = tables

    def __init__(self, dict):
        self.name = dict['name']
        self.date = dict['date']
        self.competitors = dict['competitors']
        self.categories = dict['categories']
        self.tables = dict['tables']

    def addCategory(self, category):
        self.competitors.append(category)

    def saveCompetition(self):
        with open( self.name + '.json', 'w') as fp:
            json.dump(self, fp, indent = 4, cls = EncodeStudent)


    def loadCompetition(fileName):
        with open( fileName, 'r') as fp:
            competition = Competition(json.loads(fp.read()))
        return competition

    def addCategoryFromExcel():
        pass
    
    def loadCompetitionFromExcel():
        pass

class Match:
    def __init__(self, competitor1, competitor2, winner):
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.winner = winner

    def setWinner(self, winner):
        self.winner = winner

class Bracket:
    def __init__(self, name, matches):
        self.name = name
        self.matches = matches

    def addMatch(self, match):
        self.matches.append(match)

class Category:
    def __init__(self, age, weight, hand, gender, competitors, matches, bracket):
        self.age = age
        self.weight = weight
        self.hand = hand
        self.gender = gender
        self.competitors = competitors
        self.matches = matches
        self.bracket = bracket

    def addCompetitor(self, competitor):
        self.competitors.append(competitor)
    
    def readCategoryFromExcel():
        pass
