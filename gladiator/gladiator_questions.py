from sklearn.linear_model import LinearRegression

import dccontroller
import marvelcontroller
import MarvelConn
import dcconn
import statistics
import math

def collect_data():

    print("----------Enter DC player data----------")
    team_dc = dccontroller.DC_Controller().dc_controller()

    print("----------Enter Marvel player data----------")
    team_marvel = marvelcontroller.Marvel_Controller().marvel_controller()

    return team_dc, team_marvel

# team_dc, team_marvel = collect_data()
"""
Q1. Implement a python code that finds the probability of selection of 2 from Marvel 
and 3 from DC teams.
"""

def level1_question1(dc, marvel):
    n = len(marvel)
    m = len(dc)

    marvel_combinations = math.comb(n, 2)
    dc_combinations = math.comb(m, 3)
    total_combinations = math.comb(n + m, 5)

    probability = (marvel_combinations * dc_combinations) / total_combinations

    return {
        "Marvel Combos (C(n, 2))": marvel_combinations,
        "DC Combos (C(m, 3))": dc_combinations,
        "Total Combos (C(n+m, 5))": total_combinations,
        "Probability": round(probability, 4)
    }


"""
Q2. List all those stars who are heavier than SpiderMan and taller than Henery
"""    

def level1_question2(dc, marvel):
    henery_height = None
    spiderman_weight = None
    for i in dc:
        if i['name'] == 'Henery':
            henery_height = i['height']
    for i in marvel:
        if i['name'] == 'SpiderMan':
            spiderman_weight = i['weight']
    ans = []
    for i in dc:
        if i['height'] > henery_height and i['weight'] > spiderman_weight:
            ans.append(i['name'])
    for i in marvel:
        if i['height'] > henery_height and i['weight'] > spiderman_weight:
            ans.append(i['name'])
    return ans

"""
Q3. List all those stars who have played more than 100 games and are heavier than Captain America
"""

def level1_question3(dc, marvel):
    captain_america_weight = None
    ans = []
    for i in marvel:
        if i['name'] == 'Captain America':
            captain_america_weight = i['weight']
            break
    for j in dc:
        if j['weight'] > captain_america_weight and j['games_played'] > 100:
            ans.append(j['name'])
    for k in marvel:
        if k['weight'] > captain_america_weight and k['games_played'] > 100:
            ans.append(k['name'])
    
    return ans
"""
Q4. For the given dataset representing stars from the Marvel and DC teams, if a 
metaverse is to be formed where the summation of the stats (height, weight, and 
games played) of any star is greater than 350 units, then display the names of all the 
stars meeting this criterion
"""

def level1_question4(dc, marvel):
    ans = []
    for i in dc:
        if(i['weight'] + i['height'] + i['games_played']) > 350:
            ans.append(i['name'])
    
    for j in marvel:
        if(j['weight'] + j['height'] + j['games_played']) > 350:
            ans.append(j['name'])
    
    return ans

"""
Q5. If all these have to be stored in a database implementation then perform the 
necessary code
"""

def level1_question5(dc, marvel):

    marvel_obj_insert = MarvelConn.MarvelConnector().insert_marvel(marvel)
    dc_obj_insert = dcconn.DCConnector().insert_dc(dc)
    marvel_obj_insert
    dc_obj_insert
    return dcconn.DCConnector().display_dc(), MarvelConn.MarvelConnector().display_marvel()

"""
Level 2 

Q1 Find Mean and Median of their respective heights, weights and Games played

"""

def level2_question1(dc, marvel):
    
    def get_team_info(data):

        height_arr = []
        weight_arr = []
        games_played_arr = []

        for i in data:
            height_arr.append(i['height'])
            weight_arr.append(i['weight'])
            games_played_arr.append(i['games_played'])
    
        mean_height = sum(height_arr)/len(height_arr)
        mean_weight = sum(weight_arr)/len(weight_arr)
        mean_games_played = sum(games_played_arr)/len(games_played_arr)

        median_height = statistics.median(height_arr)
        median_weight = statistics.median(weight_arr)
        median_games_played = statistics.median(games_played_arr)

        return {
            'height':{
            'mean': mean_height,
            'median': median_height
            },
            'weight':{
                'mean': mean_weight,
                'median': median_weight    
            },
            'games_played':{
                'mean': mean_games_played,
                'median': median_games_played
            }    
        }
    
    dc_info = get_team_info(dc)
    marvel_info = get_team_info(marvel)

    return {
        'dc': dc_info,
        'marvel': marvel_info
    }

"""
Q2. Find Deviation and Standard deviation of height and weight
"""

def level2_question2(dc, marvel):
    
    def get_deviation_info(data):
        height_arr = []
        weight_arr = []

        for i in data:
            height_arr.append(i['height'])
            weight_arr.append(i['weight'])
        mean_height = sum(height_arr) / len(height_arr)
        mean_weight = sum(weight_arr) / len(weight_arr)

        mean_dev_height = sum(abs(h - mean_height) for h in height_arr) / len(height_arr)
        mean_dev_weight = sum(abs(w - mean_weight) for w in weight_arr) / len(weight_arr)

        
        std_dev_height = statistics.stdev(height_arr)
        std_dev_weight = statistics.stdev(weight_arr)

        return {
            'height': {
                'mean_deviation': mean_dev_height,
                'std_deviation': std_dev_height
            },
            'weight': {
                'mean_deviation': mean_dev_weight,
                'std_deviation': std_dev_weight
            }
        }
    
    dc_stats = get_deviation_info(dc)
    marvel_stats = get_deviation_info(marvel)

    return {
        'dc': dc_stats,
        'marvel': marvel_stats
    }

"""
Q3. Perform the necessary operation to find linear regression model of effect of weight on games played 
(take games played as y and weight as x).
"""

def level2_question3(dc, marvel):
    pass
        

"""
uncomment this if you want to test

Marveldata=[
        {"name": "IronMan", "height":182, "weight": 90, "games_played": 105},
        {"name": "Thor", "height":187, "weight": 120, "games_played": 75},
        {"name": "Captain America", "height":184, "weight": 85, "games_played": 205},
        {"name": "SpiderMan", "height":175, "weight": 75, "games_played": 45},
        {"name": "Hulk", "height":179, "weight": 290, "games_played": 210}
]

dcdata = [
        {"name": "BatMan", "height":180, "weight": 85, "games_played": 105},
        {"name": "SuperMan", "height":189, "weight": 95, "games_played": 305},
        {"name": "Harvedent", "height":181, "weight": 75, "games_played": 55},
        {"name": "Henery", "height":176, "weight": 87, "games_played": 125},
        {"name": "Heralt", "height":184, "weight": 100, "games_played": 145}
    ]
"""