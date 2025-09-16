sentence = 'leetcode'

alphseen = set()

for i in range(0, len(sentence)):
    if sentence[i] not in alphseen:
        alphseen.add(sentence[i])
        
if(len(alphseen) == 26):
    print('sentence contains at least one of every letter of the English alphabet.')
else:
    print('false') 
