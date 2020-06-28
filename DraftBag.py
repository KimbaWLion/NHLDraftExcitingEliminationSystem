import random
import copy

import Constants


class DraftBag():
    def __init__(self):
        self.listOfBalls = []

    def _debug(self, strList):
        #print(''.join(strList))
        pass

    def add(self, team):
        self.listOfBalls.append(team)
        self._debug(["added ball for", team])

    def size(self):
        return len(self.listOfBalls)

    def endIfNoBallsInBag(self):
        if self.size() is 0:
            raise Exception("There are no balls in the bag")

    def pick(self):
        self.endIfNoBallsInBag()
        randIndex = random.randint(0, self.size() - 1)
        pickedBall = self.listOfBalls.pop(randIndex)
        print("picked ball for ", pickedBall)
        return pickedBall

    def countTeamBalls(self, team):
        return self.listOfBalls.count(team)

    def removeTeamsBalls(self, team):
        newListOfBalls = []
        for ball in self.listOfBalls:
            if ball is not team:
                newListOfBalls.append(ball)
        self._debug(["removed balls for team ",team])
        self.listOfBalls = newListOfBalls


    def startRound(self, roundNum=""):
        self.endIfNoBallsInBag()
        print('================')
        print('start of round', roundNum)
        print('= = = = = = = = ')
        listOfTeams = self.getAllTeamsInBag()
        print("current # of balls in bag")
        for team in listOfTeams:
            print(team, ": ", str(self.countTeamBalls(team)), " balls")
        print('================')
        hasTeamBeenPickedMap = self._createBoolMapForTeams()
        while (self._countTeamsWithNoBallPicked(hasTeamBeenPickedMap))[0] > 1:
            (numTeamsLeft, teamsLeft) = self._countTeamsWithNoBallPicked(hasTeamBeenPickedMap)
            self._debug(["number teams left: ", str(numTeamsLeft), "| teams: ", ','.join(teamsLeft)])
            pickedBall = self.pick()
            hasTeamBeenPickedMap[pickedBall] = True
        for team in hasTeamBeenPickedMap:
            if hasTeamBeenPickedMap[team] is False:
                teamWithPickThisRound = team
        self._debug(["the team with the pick this round is: ", teamWithPickThisRound])
        print('----------------')
        self._debug(['end of round', roundNum])
        self._debug('- - - - - - - - ')
        self._debug("balls left in bag")
        for team in listOfTeams:
            self._debug([team, ": ", str(self.countTeamBalls(team)), " balls"])
        self._debug('----------------')
        return teamWithPickThisRound


    def getAllTeamsInBag(self):
        list_dict = {}
        for ball in self.listOfBalls:
            list_dict.update({ball: None})
        return list(list_dict.keys())

    def _createBoolMapForTeams(self):
        listOfTeams = self.getAllTeamsInBag()
        dictOfTeams = { team : False for team in listOfTeams }
        return dictOfTeams

    def _countTeamsWithNoBallPicked(self, boolMap):
        count = 0
        teamsNotPickedYet = []
        for team in boolMap:
            if not boolMap[team]:
                count += 1
                teamsNotPickedYet.append(team)
        return (count, teamsNotPickedYet)

def main():
    print("It's lottery time!")
    listOfTeamsInDraftOrder = list(Constants.DICT_OF_TEAMS_IN_DRAFT_ORDER_WITH_BALLS_NUM.keys())
    print("Here are the teams reverse order of points who can score big today:", ', '.join(listOfTeamsInDraftOrder))
    originalDraftBag = DraftBag()
    for i in range(0, len(listOfTeamsInDraftOrder)):
        for j in range(i, len(listOfTeamsInDraftOrder)):
            originalDraftBag.add(listOfTeamsInDraftOrder[i])
    activeDraftBag = copy.deepcopy(originalDraftBag)
    draftRecapMessages = []
    draftRecapPositions = {}
    for roundNum in range(1, len(listOfTeamsInDraftOrder) + 1):
        currentRoundDraftBag = copy.deepcopy(activeDraftBag)
        teamLostRound = currentRoundDraftBag.startRound(roundNum)
        pickNum = len(listOfTeamsInDraftOrder) - roundNum + 1

        roundMessage = ' '.join(["The team", teamLostRound, "has the number", str(pickNum), "draft pick"])
        print(roundMessage)
        draftRecapMessages.append(roundMessage)

        draftRecapPositions[teamLostRound] = pickNum

        activeDraftBag.removeTeamsBalls(teamLostRound)

    print("*****************")
    print("Finally, a recap for those who are just tuning in")
    for i in range(0, len(draftRecapMessages)):
        print(draftRecapMessages[i])
    print(draftRecapPositions)


main()


