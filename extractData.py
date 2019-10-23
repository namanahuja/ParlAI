import json


## Add context number here and world.py


with open("valid_random_split.json", "r") as read_file:
    allData = json.load(read_file)
    jsonData = []


    for data in allData:

        dialogs = data['dialog']
        numDialogs = len(dialogs)

        ########################################################################

        # Extract only the last dialog without checking for Wizard/ Apprentice
        ####lastDialog = dialogs[numDialogs - 1]

        ##########################################################################

        ###########################################################################
        # Get the last conversation with Apprentice


        if 'Wizard' in dialogs[numDialogs - 1]['speaker']:
            lastDialogIndex = numDialogs - 1

        else:
            lastDialogIndex = numDialogs - 2

        lastDialog = dialogs[lastDialogIndex]




        ############################################################################
        jsonObj = {}
        jsonObj['convesation'] = []
        jsonObj['suggestions'] = []
        jsonObj['actualResponse'] = lastDialog['text']

        for i in range(lastDialogIndex):
            jsonObj['convesation'].append(dialogs[i]['text'])

        lastDialogResponses = lastDialog['retrieved_passages']
        numPassages = min (len(lastDialogResponses), 3)

        for i in range(numPassages):
            sugg = lastDialogResponses[i]
            for key,val in sugg.items():
                suggLen = min(2, len(val))
                for j in range(suggLen):
                    jsonObj['suggestions'].append(val[j])

        jsonData.append(jsonObj)

finalJSON = {}
finalJSON['data'] = jsonData
with open('data.json', 'w') as outfile:
    json.dump(finalJSON, outfile)
