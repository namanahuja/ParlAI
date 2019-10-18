import json

with open("valid_random_split.json", "r") as read_file:
    allData = json.load(read_file)
    jsonData = []


    for data in allData:

        dialogs = data['dialog']
        numDialogs = len(dialogs)
        lastDialog = dialogs[numDialogs - 1]
        jsonObj = {}
        jsonObj['convesation'] = []
        jsonObj['suggestions'] = []

        for dialog in dialogs:
            jsonObj['convesation'].append(dialog['text'])

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