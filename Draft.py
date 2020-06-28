from DraftBag import DraftBag
import copy
import numpy as np
#import matplotlib.pyplot as plt
import Constants

class Draft():
    def __init__(self):
        pass

    def runDraft(self, dictOfTeamsInDraftOrderWithBallNum):
        listOfTeamsInDraftOrder = list(dictOfTeamsInDraftOrderWithBallNum.keys())
        print("It's lottery time!")
        print("Here are the teams reverse order of points who can score big today:", ', '.join(listOfTeamsInDraftOrder))
        originalDraftBag = DraftBag()
        # Put balls into draftbag
        # each team has 1 more ball than the last
        # for i in range(0, len(listOfTeamsInDraftOrder)):
        #     for j in range(i, len(listOfTeamsInDraftOrder)):
        #         originalDraftBag.add(listOfTeamsInDraftOrder[i])
        # use values set in dict in Constants
        for i in range(0, len(listOfTeamsInDraftOrder)):
            for j in range(0, dictOfTeamsInDraftOrderWithBallNum[listOfTeamsInDraftOrder[i]]):
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
        return draftRecapPositions



def main():
    print("start")
    numOfRuns = 10000
    draft = Draft()
    listOfTeamsInDraftOrder = list(Constants.DICT_OF_TEAMS_IN_DRAFT_ORDER_WITH_BALLS_NUM.keys())
    dictOfDictsOfPositions = {}
    dictOfPositionsNoRuns = {}
    for i in range(1, len(listOfTeamsInDraftOrder) + 1):
        dictOfPositionsNoRuns[i] = 0
    for team in listOfTeamsInDraftOrder:
        dictOfDictsOfPositions[team] = copy.deepcopy(dictOfPositionsNoRuns)

    for i in range(0,numOfRuns):
        results = draft.runDraft(Constants.DICT_OF_TEAMS_IN_DRAFT_ORDER_WITH_BALLS_NUM)
        for result in results:
            dictOfDictsOfPositions[result][results[result]] += 1

    print(dictOfDictsOfPositions)

    # subplotLocations = ["331", "332", "333", "334", "335", "336", "337", "338", "339"]
    # for i in range(1, 10): #len(listOfTeamsInDraftOrder)):
    #     plt.subplot(subplotLocations[i-1])
    #     teamName = listOfTeamsInDraftOrder[i-1]
    #     height = dictOfDictsOfPositions[teamName].values()
    #     bars = dictOfDictsOfPositions[teamName].keys()
    #     y_pos = np.arange(len(bars))
    #     plt.bar(y_pos, height)
    #     plt.xticks(y_pos, bars)
    #     plt.title(teamName)
    # plt.show()
    #
    # for i in range(10, 16): #len(listOfTeamsInDraftOrder)):
    #     plt.subplot(subplotLocations[i-10])
    #     teamName = listOfTeamsInDraftOrder[i-1]
    #     height = dictOfDictsOfPositions[teamName].values()
    #     bars = dictOfDictsOfPositions[teamName].keys()
    #     y_pos = np.arange(len(bars))
    #     plt.bar(y_pos, height)
    #     plt.xticks(y_pos, bars)
    #     plt.title(teamName)
    #plt.show()

    markdownHeaderRowString = "| Team |"
    markdownSecondRowString = "|------|"
    for i in range(1,len(listOfTeamsInDraftOrder) + 1):
        markdownHeaderRowString = ''.join([markdownHeaderRowString, " ", str(i), "th |"])
        markdownSecondRowString = ''.join([markdownSecondRowString, "------:|"])
    print(markdownHeaderRowString)
    print(markdownSecondRowString)
    for i in range(0,len(listOfTeamsInDraftOrder)):
        teamToAddToMarkdownTable = list(dictOfDictsOfPositions.keys())[i]
        rowString = ''.join(["| ", teamToAddToMarkdownTable, " |"])
        for j in range(1, len(listOfTeamsInDraftOrder) + 1):
            rowString = ''.join([rowString, " ", "{:.2%}".format(dictOfDictsOfPositions[teamToAddToMarkdownTable][j] / numOfRuns), " |"])
        print(rowString)

main()
