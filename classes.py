class Competitor:
    def __init__(self, name, category, country, email):
        self.name = name
        self.category = category
        self.country = country
        self.email = email

class Competition:
    def __init__(self, name, date, competitors, categories):
        self.name = name
        self.date = date
        self.competitors = competitors
        self.categories = categories

    def addCategory(self, category):
        self.competitors.append(category)

    def addCategoryFromExcel():
        pass
    
    def addCompetitionFromExcel():
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
    def __init__(self, name, competitors, matches, bracket):
        self.name = name
        self.competitors = competitors
        self.matches = matches
        self.bracket = bracket

    def addCompetitor(self, competitor):
        self.competitors.append(competitor)
    
    def readCategoryFromExcel():
        pass
