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
        Sit Back, Relax Let Fate do its Thing!
---------------------------------------------------------------------------------
'''
QUESTION = (
    'Mark Lee is the Best Man Ever',
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
    userResponse = int(input(QUESTION[i]))
    # TO DO VALIDIATE RESPONSE AND ASK QUESTION AGAIN IF NEEDED
   

    response.append(userResponse)

    questionCompatability = 5 - abs(userResponse - DESIRED_REPONSE[i])
    comptability.append(questionCompatability)
    print('Question %d Comptability %d\n' % (i+1, questionCompatability))

totalCompatability = 0 
for c in comptability:
    totalCompatability += c

totalCompatability *=100/MAX_SCORE
print('Total Compatability: %d\n\n' % (totalCompatability))

# TO DO DETERMINE COMPTABILITY RANGE


