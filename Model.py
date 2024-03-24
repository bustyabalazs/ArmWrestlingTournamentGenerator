import json
from json import JSONEncoder

import bisect
from math import log2
import math

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

    def getCompetitorsInCategory(self, category):
        competitors = []
        for competitor in self.competitors:
            if category in competitor.categories:
                competitors.append(competitor)
        return competitors

    def saveCompetition(self):
        with open(self.fileName + '.json', 'w') as fp:
            json.dump(self, fp, indent = 4, cls = EncodeCompetition)

    def loadCompetition(fileName):
        with open( fileName, 'r') as fp:
            competition = json.loads(fp.read())
        return Competition(competition)


    def getCategoriesByNames(self, categories):
        categoryList = []
        for category in self.categories:
            if category.toString() in categories:
                categoryList.append(category)
        return categoryList
                                                                                                             
    def addCategoryFromExcel():
        pass
    
    def loadCompetitionFromExcel():
        pass


class Match:
    isWinnersFinal = False
    isLoosersFinal = False
    looser = None
    def __init__(self, id, competitor1, competitor2, winner, round, isWinnerBranch = True, isFinal = False):
        self.id = id[0]
        id[0] = id[0] + 1
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.winner = winner
        self.round = round
        self.isWinnerBranch = isWinnerBranch
        self.isFinal = isFinal
    
    def setWinner(self, isComp1Winner):
        if isComp1Winner:
            self.winner = self.competitor1
            self.looser = self.competitor2
        else:
            self.winner = self.competitor2
            self.looser = self.competitor1

    def toString(self):
        return str(self.id) + ' # ' + ("-----------" if self.competitor1 is None else self.competitor1.name) + ' VS ' \
                + ("-----------" if self.competitor2 is None else self.competitor2.name) \
                + ' # ' +  self.roundToString()

    def roundToString(self):
        return 'Final' if self.isFinal else ('WinnersSemiFinal' if self.isWinnersFinal else ('LoosersSemiFinal' if self.isLoosersFinal else ('Round: ' + 
        ('Winners' if self.isWinnerBranch else 'Loosers') + str(self.round))))

    def toStrinGFinished(self):
        return self.toString() + ("---Winner: " + self.winner.name)

class Round:
    def __init__(self, matches, competitors):
        self.competitors = competitors
        self.matches = matches

class Ranking:
    def __init__(self, competitor, position):
        self.competitor = competitor
        self.position = position

    def __lt__(self, other):
        return self.position < other.position
    
    def toString(self):
        return str(self.position) + '. ' + self.competitor.name

class Bracket:
    matchCounter = [0]
    next_matches = []
    finished_matches = []
    winners_rounds = []
    loosers_rounds = []
    finalMatch = Match([0], None, None, None, 0, isFinal = True)
    rankings = []

    def __init__(self, competitors):
        self.round1Competitors = competitors

    def genBracket(self):
        bracketNum = self.getBracketNum()
        self.genRounds(bracketNum)        
        matchNum = int(bracketNum/2)
        numofCompetitors = len(self.round1Competitors)
        self.winners_rounds[0].competitors = self.round1Competitors
        for i in range (0, matchNum):
            self.winners_rounds[0].matches[i] = Match(self.matchCounter, self.round1Competitors[i], None, None, 0)

        # helper variable to add competitors to the first and second half of the bracket
        # adding competitors to the matches is starting from the back thus the first competitors dont have to pull twice in a row
        temp = 0 if matchNum <= 2 else matchNum - 1
        for i in range (matchNum, numofCompetitors):
            #logic to add competitors evenly to both sides of the bracket
            if (i-matchNum)%2 == 0:
                self.winners_rounds[0].matches[temp].competitor2 = self.round1Competitors[i]
            else:
                self.winners_rounds[0].matches[temp + int(matchNum/2)].competitor2 = self.round1Competitors[i]
                temp -= 1

        self.next_matches = self.winners_rounds[0].matches.copy()
        if matchNum == 1:
            self.next_matches[0].isWinnersFinal = True
            self.next_matches[0].isLoosersFinal = True
        self.advanceBracket()

        
    def advanceBracket(self):
        range = len(self.next_matches)
        i=0
        while i < range:
            match = self.next_matches[i]
            if match.competitor2 is None:
                self.step(match, True)
                i = i - 1
                range = range - 1
            elif match.competitor1 is None:
                self.step(match, False)
                i = i - 1
                range = range - 1
            i = i + 1
    # advance bracket needs to be callse after looser round 1 and 2

    def genRounds(self, bracketNum):
        roundNumWinners = int(log2(bracketNum))
        roundNumLoosers = roundNumWinners + int(log2(bracketNum/2))-1
        # create rounds for winners
        for i in range(0, roundNumWinners):
            self.winners_rounds.append(Round([None]*int(bracketNum/(2**(i+1))), [None]*int(bracketNum/(2**i))))
        
        # create rounds for loosers
        inc = -1
        for i in range(0, roundNumLoosers):
            if i%2 == 0:
                inc = inc + 1
            self.loosers_rounds.append(Round([None]*int(bracketNum/(2**(inc+2))), [None]*int(bracketNum/(2**(inc+1)))))
    
           
    def getBracketNum(self):
        # Find minimum 'n' such that 2^n >= number of competitors
        return int(math.pow(2, math.ceil(math.log2(len(self.round1Competitors)))))
    

    def step(self, match, isComp1Winner):
        self.next_matches.remove(match)
        match.setWinner(isComp1Winner)
        if match.competitor1 is not None and match.competitor2 is not None:
            self.finished_matches.append(match)

        # handle finals
        if match.isFinal:
            if match.looser is not None:
                bisect.insort(self.rankings, Ranking(match.looser, self.getRanking(match)))
            bisect.insort(self.rankings, Ranking(match.winner, self.getRanking(match)))
            match.id = self.matchCounter[0]
        elif match.isWinnersFinal and match.isLoosersFinal:
            self.finalMatch.competitor1 = match.winner
            self.finalMatch.competitor2 = match.looser
            self.next_matches.append(self.finalMatch)
        elif match.isWinnersFinal:
            self.finalMatch.competitor1 = match.winner
            self.addCompetitorsToNextRound(match)
            if self.next_matches.count(self.finalMatch) == 0:
                self.next_matches.append(self.finalMatch)
        elif match.isLoosersFinal:
            self.finalMatch.competitor2 = match.winner
            if self.next_matches.count(self.finalMatch) == 0:
                self.next_matches.append(self.finalMatch)
            if match.looser is not None:
                bisect.insort(self.rankings, Ranking(match.looser, self.getRanking(match)))
        else:
            self.addCompetitorsToNextRound(match)

            

    def isWinnersFinalMatch(self, match):
        return (match.round == len(self.winners_rounds) - 1)


    def isLoosersFinalMatch(self, match):
        return match.round == len(self.loosers_rounds) - 1
    

    def genNextMatchWinnerBranch(self, f_match):
        index = self.winners_rounds[f_match.round].matches.index(f_match)
        indexDiv2 = int(index/2)
        # if the next round is not long enough, add empty matches
        # if len(self.winners_rounds[match.round + 1].matches) < (indexDiv2 + 1):
        #     for i in range(0, (indexDiv2 + 1) - len(self.winners_rounds[match.round + 1].matches)):
        #         match = Match(self.matchCounter, None, None, None, match.round + 1)  
        #         self.winners_rounds[match.round + 1].matches.append(match)
        #         self.next_matches.append(match)
        next_match = self.winners_rounds[f_match.round + 1].matches[indexDiv2]
        if next_match is None:
            next_match = Match(self.matchCounter, None, None, None, f_match.round + 1)
            if self.isWinnersFinalMatch(next_match):
                next_match.isWinnersFinal = True
            self.next_matches.append(next_match)
            self.winners_rounds[f_match.round + 1].matches[indexDiv2] = next_match
        if index % 2:
            next_match.competitor2 = f_match.winner
        else:
            next_match.competitor1 = f_match.winner


    def genNextMatchLooserBranchFromWinners(self, f_match):
        newMatchRound = 1 if f_match.round == 1 else (0 if f_match.round == 0 else 2 * f_match.round - 1)
        index = self.winners_rounds[f_match.round].matches.index(f_match)
        center = int(len(self.loosers_rounds[newMatchRound].matches)/2)
        invPos = self.invertPosition(center, index)
        next_match = self.loosers_rounds[newMatchRound].matches[invPos]
        if next_match is None:
            next_match = Match(self.matchCounter, None, None, None, newMatchRound, False)
            if self.isLoosersFinalMatch(next_match):
                next_match.isLoosersFinal = True
            self.next_matches.append(next_match)
        next_match.competitor2 = f_match.looser
        self.loosers_rounds[newMatchRound].matches[invPos] = next_match
            

    def genNextMatchLooserBranchZeroFromWinners(self, f_match):
        newMatchRound = 0
        index = int(self.winners_rounds[f_match.round].matches.index(f_match))
        newMatchindex = int(index/2)
        next_match = self.loosers_rounds[newMatchRound].matches[newMatchindex]
        if next_match is None:
            next_match = Match(self.matchCounter, None, None, None, newMatchRound, False)
            if self.isLoosersFinalMatch(next_match):
                next_match.isLoosersFinal = True
            self.next_matches.append(next_match)
            self.loosers_rounds[newMatchRound].matches[newMatchindex] = next_match
        if index % 2:
            next_match.competitor2 = f_match.looser
        else:
            next_match.competitor1 = f_match.looser

    def genNextMatchLooserBranch(self, f_match):
        index = self.loosers_rounds[f_match.round].matches.index(f_match)
        # if the current round is odd then the next will have only half as many matches as the current
        if f_match.round % 2:
            newMatchindex = int(index/2)
        else:
            newMatchindex = index
        next_match = self.loosers_rounds[f_match.round + 1].matches[newMatchindex]
        if next_match is None:
            next_match = Match(self.matchCounter, None, None, None, f_match.round + 1, False)
            if self.isLoosersFinalMatch(next_match):
                next_match.isLoosersFinal = True
            self.next_matches.append(next_match)
            self.loosers_rounds[f_match.round + 1].matches[newMatchindex] = next_match
        # opponent comes from winners branch    
        if next_match.round % 2:
            next_match.competitor1 = f_match.winner
        elif index % 2:      
            next_match.competitor2 = f_match.winner
        else:
            next_match.competitor1 = f_match.winner
        if f_match.looser is not None:
            bisect.insort(self.rankings, Ranking(f_match.looser, self.getRanking(f_match)))


    def getRanking(self, match):
        return len(self.round1Competitors) - len(self.rankings)


    def invertPosition(self, center, position):
        return 0 if center == 0 else center + (center - position) - 1
    

    def addCompetitorsToNextRound(self, match):
        #if match.winner != None: 
        if match.isWinnerBranch:
            index = self.winners_rounds[match.round].matches.index(match)
            # Adding loser to next round on loosers branch
            if match.round == 0:
                self.loosers_rounds[match.round].competitors[index] = match.looser
                self.genNextMatchLooserBranchZeroFromWinners(match)
            else: # TODO implement logic for inversing indexis 
                center = int(len(self.loosers_rounds[2 * match.round - 1].matches))
                invPos = self.invertPosition(center, index)
                self.loosers_rounds[2 * match.round - 1].competitors[invPos] = match.looser
                self.genNextMatchLooserBranchFromWinners(match)
            
            # Adding winner to next round on winners branch, excpet 
            if not match.isWinnersFinal:
                self.winners_rounds[match.round + 1].competitors[index] = match.winner
                self.genNextMatchWinnerBranch(match)
        else:
            index = self.loosers_rounds[match.round].matches.index(match)
            # Adding winner to next round on loosers branch
            self.loosers_rounds[match.round + 1].competitors[index] = match.winner
            self.genNextMatchLooserBranch(match)


    def genRankings(self):
        #az azonos szinten lévő versenyzőknél figyelembe venni a két vesztes meccs ellenfeleinek eredményét
        pass

    def updateBracket(self, match, isComp1Winner):
        pass

    def saveBracket(self):
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
    
    def __eq__(self, other):
        current = self.toString()
        return current == other

    
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
    runningCategory = None
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