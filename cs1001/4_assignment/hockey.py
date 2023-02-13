##
# Class for storing data on a single hockey game.
# File also includes tests for said class
##

class HockeyGame():
    
    # Total number of hockey games
    Games = 0

    GAMETIME = 60
    
    def __init__(
            self,
            homeTeam='unknown',
            awayTeam='unknown',
            homeTeamScore=0,
            awayTeamScore=0,
            extraTime=0,
        ):
        HockeyGame.Games += 1
        self.__gameNumber = HockeyGame.Games
        
        # Sets instance vairables passed to object
        self.__homeTeam = homeTeam
        self.__awayTeam = awayTeam
        self.__homeTeamScore = homeTeamScore
        self.__awayTeamScore = awayTeamScore
        self.__extraTime = extraTime
    
    def getHome(self):
        return self.__homeTeam

    def getAway(self):
        return self.__awayTeam
        
    def getGameNumber(self):
        return self.__gameNumber
    
    def setExtraTime(self, extraTime):
        self.__extraTime = extraTime
    
    # Computes and returns the total amount of minutes in the game
    def computeGameTime(self):
        return HockeyGame.GAMETIME + self.__extraTime
    
    # Returns a formated sting with the score of the game in the format:
    # (Home Score)-(Away Score)
    def getScore(self):
        return f'{self.__homeTeamScore}-{self.__awayTeamScore}'
    
    def __str__(self):
        # Checks if game was in overtime and if it was sets appropriate text
        overtimeText = 'Overtime Game\n' if self.__extraTime else ''
        return (
            f'Game {self.getGameNumber()}\n' # Game ID
            f'{self.getHome()} {self.getScore()} {self.getAway()}\n' # Team names and score
            f'{overtimeText}' # Prints if game was an overtime game
            f'{self.computeGameTime()} minute game\n' # Game length
        )

    
def main():
    # Creates three instances of HockeyGame class
    gameOne = HockeyGame('Labrador City', 'Happy Valley-Goose Bay', 0, 1)
    gameTwo = HockeyGame('Bonavista', 'Corner Brook', 2, 1, 6)
    gameThree = HockeyGame('Gander', 'Happy Valley-Goose Bay', 0, 1)
    
    print(gameOne)
    print(gameTwo)
    print(gameThree)
    
    # Changes extra time of game one
    gameOne.setExtraTime(13)
    print('The game time for Game 1 has been updated from 60 minutes to 73 minutes.\n')
    
    print(gameOne)
    
    print(f'There are {HockeyGame.Games} hockey games in the system.')

if __name__ == "__main__":
    main()