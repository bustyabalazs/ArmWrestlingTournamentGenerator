import json
from json import JSONEncoder

import bisect

class EncodeCompetition(JSONEncoder): 
        def default(self, o): 
            return o.__dict__ 
        

class Competitor:
    def __init__(self, id, name, category, country, email):
        self.id = id
        self.name = name
        self.category = category
        self.country = country
        self.email = email
    
    def toString(self):
        return self.name + ' ## ' + self.category + ' ## ' + self.country + ' ## ' + self.email
    
    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name


class Competition:
    def __init__(self, fileName, name, date, competitors, categories, tables, countries):
        self.fileName = fileName
        self.name = name
        self.date = date
        self.competitors = competitors
        self.categories = categories
        self.tables = tables
        self.countries = countries

    def __init__(self, dict):
        self.fileName = dict['fileName']
        self.name = dict['name']
        self.date = dict['date']
        self.competitors = []
        for competitor in dict['competitors']:
            self.competitors.append(Competitor(competitor['id'], competitor['name'], competitor['category'], competitor['country'], competitor['email']))
        self.categories = []
        for category in dict['categories']:
            bisect.insort(self.categories, createCategoryFromDict(category)) 
        self.tables = []
        for table in dict['tables']:
            self.tables.append(table)
        self.countries = []
        for country in dict['countries']:
            self.countries.append(Country(country['name']))
        
    def addCategory(self, category):
        bisect.insort(self.categories, category)

    def addCompetitor(self, competitor):
        bisect.insort(self.competitors, competitor)
    
    def addTable(self, table):
        bisect.insort(self.tables, table)

    def addCountry(self, country):
        bisect.insort(self.countries, country)

    def saveCompetition(self):
        with open(self.fileName + '.json', 'w') as fp:
            json.dump(self, fp, indent = 4, cls = EncodeCompetition)

    def loadCompetition(fileName):
        with open( fileName, 'r') as fp:
            competition = json.loads(fp.read())
        return Competition(competition)

    def addCategoryFromExcel():
        pass
    
    def loadCompetitionFromExcel():
        pass


class Match:
    def __init__(self, id, competitor1, competitor2, winner):
        self.id = id
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
    def __init__(self, age, weight, hand, gender, matches, bracket):
        self.age = age
        self.weight = weight
        self.hand = hand
        self.gender = gender
        self.matches = matches
        self.bracket = bracket

    def __lt__(self, other):
        return ((self.age, self.weight, self.hand, self.gender) <
                (other.age, other.weight, other.hand, other.gender))
    
    def __eq__(self, other):
        return ((self.age, self.weight, self.hand, self.gender) ==
                (other.age, other.weight, other.hand, other.gender))
    
    def toString(self):
        return self.age + ' ## ' + self.weight + ' ## ' + self.hand + ' ## ' + self.gender

    
    def readCategoryFromExcel():
        pass


class Country:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def toString(self):
        return self.name

def createCategoryFromDict(category):
    matches = []
    for match in category['matches']:
        matches.append(Match(match['id'], match['competitor1'], match['competitor2'], match['winner']))
    return Category(category['age'], category['weight'], category['hand'], category['gender'], matches, category['bracket'])