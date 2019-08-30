import json
import matplotlib.pyplot as plt
import math

with open('test_random_split.json') as json_data:
    data = json.load(json_data,)
lengths = []    
for i in range(len(data)):
    dialogs = data[i]['dialog']
    currLen = 0
    for k in range(len(dialogs)):
        currLen = currLen + len(dialogs[k]['text'])
    lengths.append(math.log(currLen/len(dialogs)))

plt.plot(lengths)
plt.show()