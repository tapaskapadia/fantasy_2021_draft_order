import random
import os
import webbrowser
import json
from datetime import datetime

print(f"current time: ", datetime.now())
output_filename = "owner_climber_assignments.json"
team_owners = ["Alex", "Ajay", "Avery", "Damien", "Justin","Nathan", "Neel", "Tapas", "Taylor", "Sai"]
climbers = [
    {"name": "Kai Harada", "national_team": "Japan", "fact": "Qualified to the olympics in the 'host' spot. 👀"},  
    {"name": "Tomoa Narasaki", "national_team": "Japan", "fact": "He holds the Japanese record for speed climbing with a time of 5.73 seconds."},
    {"name": "Jakob Schubert", "national_team": "Austria", "fact": "He is a World Champion (2012, 2018) and World Cup winner (2011, 2014, 2018) in lead climbing."},
    {"name": "Rishat Khaibullin", "national_team": "Kazakhstan", "fact": "From the same country as the fictional character Borat Margaret Sagdiyev."},
    {"name": "Mickaël Mawem", "national_team": "France", "fact": "His older brother Bassa is also a professional climber."},
    {"name": "Alexander Megos", "national_team": "Germany", "fact": "Megos started climbing at the age of six."},
    {"name": "Ludovico Fossali ", "national_team": "Italy", "fact": "Has won the speed climbing gold medal at the 2019 in Japan"},
    {"name": "Sean McColl", "national_team": "Canada", "fact": "Competed in Ninja Warrior."},
    {"name": "Adam Ondra", "national_team": "Czech Republic", "fact": "According to The Economist, Ondra is 'regarded as possibly the best climber ever to fondle rock'."},
    {"name": "Bassa Mawem", "national_team": "France", "fact": "His younger brother Mickaël is also a professional climber."},
    {"name": "Jan Hojer", "national_team": "Germany", "fact": "On May 2010, he climbed Action Directe, still considered to be one of the most difficult routes in the world."},
    {"name": "Pan Yufei", "national_team": "China", "fact": "His instram handle is yfei_pan."},
    {"name": "Alberto Ginés López ", "national_team": "Spain", "fact": "He placed second in the 2019 Lead Climbing World Cup."},
    {"name": "Nathaniel Coleman", "national_team": "United States", "fact": "He was the first American male climber to qualify to the Olympic Games."},
    {"name": "Colin Duffy", "national_team": "United States", "fact": "He is the youngest climber to qualify."},
    {"name": "Christopher Cosser", "national_team": "South Africa", "fact": "Started climbing in 2012 on a small school wall."},
    {"name": "Aleksei Rubtsov", "national_team": "Russa", "fact": "Opened and manages his own bouldering gym in the North of Moscow, called Toki.o"},
    {"name": "Tom O'Halloran", "national_team": "Australia", "fact": "He decided to come out of competition retirement in to make the Olympic team."},
    {"name": "Chon Jong-won", "national_team": "Korea", "fact": "In 2013, he won second place in the Asian youth championships."},
    {"name": "Michael Piccolruaz", "national_team": "Italy", "fact": "Qualified for the 2020 Summer Olympics after the IFSC reallocated spots that were unused due to cancelled competitions."}
]
owner_climber_assignments = []
# Shuffle the team owners list 
random.shuffle(team_owners)
# Iterate through each owner and select 2 climbers
for owner in team_owners:
    assignment = {"team_owner": owner}
    # Shuffle climbers before selecting 2
    random.shuffle(climbers)
    # Remove the last climber from the list and assigns it to the owner - 2X
    assignment["climber_1"] = climbers.pop()
    assignment["climber_2"] = climbers.pop()
    # add assignment to an list to build the output
    owner_climber_assignments.append(assignment)
# write to json
with open('owner_climber_assignments.json', 'w', encoding='utf-8') as f:
    print(f"writing to file: {output_filename}")
    json.dump(owner_climber_assignments, f,  ensure_ascii=False, indent=2)

