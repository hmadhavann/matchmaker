# Hima Madhavan
# Matchmaker

INTRODUCTION = '''
            MatchMaker 2021
---------------------------------------------------------------------------------
            MatchMaker Version 1.0
            Finding Love Since 2021
    Wanna find out if we are destined to be together? 
    Well you are in Luck, Welcome to Matchmaker!
Simply Answer the Five Questions Honestly with a Number 1-5:
5- Strongly Agree, 4- Agree, 3- Neutral, 2- Disagree, 1- Strongly Disagree
        Sit Back, Relax and Let Fate do its Thing!
---------------------------------------------------------------------------------
'''
QUESTION = (
    'Green is the best color',
    'Football is the best sport',
    'Haikyuu is the best anime series',
    'Alfredo Pasta is the Best',
    'History is the worst subject'
)

DESIRED_REPONSE = (
    5, # STRONGLY AGREE
    1, # STRONGLY DISAGREE
    4, # AGREE
    3, # NEUTRAL
    1, # STRONGLY DISAGREE
)

MAX_SCORE =  5 * len(QUESTION) 

print(INTRODUCTION)

response = []
comptability = []

for i in range(len(QUESTION)):
    try:
        userResponse = int(input(QUESTION[i]))
    except ValueError:
        print('Please Enter a Number')
        userResponse = int(input(QUESTION[i]))
        questionCompatability = 5 - abs(userResponse - DESIRED_REPONSE[i])
        comptability.append(questionCompatability)
        print('Question %d Comptability: %d\n' % (i+1, questionCompatability))
        continue
    while userResponse > 0  and userResponse < 6:
        print('That is a Number!')
        response.append(userResponse)
        questionCompatability = 5 - abs(userResponse - DESIRED_REPONSE[i])
        comptability.append(questionCompatability)
        print('Question %d Comptability: %d\n' % (i+1, questionCompatability))
        break
    else:
        print('That is the Wrong Response\nPlease Try Again')
        userResponse = int(input(QUESTION[i]))
        questionCompatability = 5 - abs(userResponse - DESIRED_REPONSE[i])
        comptability.append(questionCompatability)
        print('Question %d Comptability: %d\n' % (i+1, questionCompatability))
        continue
             
totalCompatability = 0 
for c in comptability:
    totalCompatability += c

totalCompatability *= 100/MAX_SCORE
print('Are we meant to be?\nYour Result is %d/100' % (totalCompatability)) 

if totalCompatability <=69:
    print('...Perhaps in Another Lifetime:(\n') 
else:
    if 70 <= totalCompatability <= 79:
        print('...Maybe Another Time:[\n')
if 80 <= totalCompatability <= 89:
    print('...Hmmmm....Friends?\n')
else:
    if 90 <= totalCompatability <= 99:
        print('...We Should Hang Out!!\n')
if totalCompatability == 100:
    print('...Im Sorry, are we....SOULMATES???\n')
      
