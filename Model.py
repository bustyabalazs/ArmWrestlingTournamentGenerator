import json
from json import JSONEncoder

import bisect

class EncodeCompetition(JSONEncoder): 
        def default(self, o): 
            return o.__dict__ 
        

class Competitor:
    def __init__(self, id, name, categories, country, email):
        self.id = id
        self.name = name
        self.categories = categories
        self.country = country
        self.email = email
    
    def toString(self):
        categories = ''
        for category in self.categories:
            categories += category + ', '
        return str(self.id)  + ' # ' + self.name + ' # ' + categories + ' # ' + self.country + ' # ' + self.email
    
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
            bisect.insort(self.competitors, createCompetitorFromDict(competitor))
        self.categories = []
        for category in dict['categories']:
            bisect.insort(self.categories, createCategoryFromDict(category)) 
        self.tables = []
        for table in dict['tables']:
            self.tables.append(Table(table['name']))
        self.countries = []
        for country in dict['countries']:
            self.countries.append(Country(country['name']))
        
    def addCategory(self, category):
        bisect.insort(self.categories, category)

    def getCategoryList(self):
        categoryList = []
        for category in self.categories:
            categoryList.append(category.toString())
        return categoryList

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
    def __init__(self, id, competitor1, competitor2, winner, round):
        self.id = id
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.winner = winner
        self.round = round


class Round:
    def __init__(self, matches, competitors):
        self.competitors = competitors
        self.matches = matches


class Bracket:
    matchCounter = 1
    loosers_branch = None
    next_matches = []
    finished_matches = []
    winners_rounds = []
    loosers_rounds = []

    def __init__(self, name, category, competitors):
        self.name = name
        self.category = category
        self.round1Competitors = competitors

    def addMatch(self, match):
        self.next_matches.append(match)
        self.matchCounter += 1

    def genBracket(self):
        bracketNum = self.getBracketNum()
        matchNum = bracketNum/2
        numofCompetitors = len(self.round1Competitors)

        for i in range (0, matchNum):
            self.addMatch(Match(self.matchCounter, self.round1Competitors[i], None, None, 0))
        temp = 0
        for i in range (matchNum, numofCompetitors):
            if (i-matchNum)%2 == 0:
                self.next_matches[temp].competitor2 = self.round1Competitors[i]
            else:
                self.next_matches[temp + matchNum/2].competitor2 = self.round1Competitors[i]
                temp += 1
        
        self.genRounds()

    def genRounds(self):
        for i in range(0, self.getBracketNum()/2+1):
            self.loosers_rounds.append(Round([], []))
            # winners branch is half length
            if i%2:
                self.winners_rounds.append(Round([], []))
           
    def getBracketNum(self):
        num = len(self.round1Competitors)
        if num <= 2:
            return 2
        elif num <= 4:
            return 4
        elif num <= 8:
            return 8
        elif num <= 16:
            return 16
        elif num <= 32:
            return 32
        elif num <= 64:
            return 64
        elif num <= 128:
            return 128
        else:
            return 0
        # Find minimum 'n' such that 2^n >= number of competitors
        # next_higher_power_of_two = int(math.pow(2, math.ceil(math.log2(len(competitors_list)))))
    
    def setWinner(self, match, isComp1Winner):
        self.finished_matches.append(match)
        if isComp1Winner:
            match.winner = match.competitor1
            self.winners_rounds[match.round + 1].competitors.append(match.competitor1)
            self.loosers_branch
            self.loosers_branch.append(match.competitor2)
        else:
            match.winner = match.competitor2
            self.loosers_branch.append(match.competitor1)
        self.next_matches.remove(match)
        self.genNextMatch(match)

    def genNextMatch(self, match):
        if self.matchCounter % 2 == 0:
            self.addMatch(Match(self.matchCounter, None, None, None))
        else:
            self.next_matches[self.matchCounter - 1].competitor1 = match.winner 
    def updateBracket(self):
        pass

    def decideTableSide(self, match):
        pass

    def randomSeeding(self):
        pass


class Category:
    table = None
    isFree = True
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
        return self.age + ' ' + self.weight + ' ' + self.hand + ' ' + self.gender

    
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

class Table:
    isUsed = False
    def __init__(self, name):
        self.name = name

    def toString(self):
        return self.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __eq__(self, other):
        return self.name == other.name
    


def createCategoryFromDict(category):
    matches = []
    for match in category['matches']:
        matches.append(Match(match['id'], match['competitor1'], match['competitor2'], match['winner']))
    return Category(category['age'], category['weight'], category['hand'], category['gender'], matches, category['bracket'])

def createCompetitorFromDict(competitor):
    categories = []
    for category in competitor['categories']:
        categories.append(category)
    return Competitor(competitor['id'], competitor['name'], categories, competitor['country'], competitor['email'])