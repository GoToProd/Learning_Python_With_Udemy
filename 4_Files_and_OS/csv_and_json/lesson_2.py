import json
from typing import Any

class Tournament:
    def __init__(self,name, year):
        self.name = name
        self.year = year
        
tour = {
    'Leonel Messi': 2021,
    'CR7': 2020,
    'Luka Modrich': 2019 
}

json_data = json.dumps(tour, indent=2)
print (json_data)

# lodaded = json.loads(json_data)
# print (lodaded)
# print (type(lodaded))

# t1 = Tournament('Leonel Messi', 2021)
# #json_data = json.dumps(t1)
# json_data = json.dumps(t1.__dict__)
# print (json_data)

# t = Tournament(**json.loads(json_data))
# print(f'name = {t.name} and year = {t.year}')


class Players:
    def __init__(self,tour):
        self.tour = tour
        
t1 = Tournament("Leonel Messi", 2021)
t2 = Tournament("CR7", 2020)
t3 = Tournament("Luka Modrich", 2019)

p1 = Players([t1,t2,t3])

json_data = json.dumps(t1.__dict__)
print(json_data)

json_data = json.dumps(p1, default=lambda obj: obj.__dict__)
print(json_data)


decod = Players(**json.loads(json_data))
print(decod)

pr = decod.tour[0]
print(pr)
print(tour)


class Tournament:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        
    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)
    
class Players:
    def __init__(self,tour):
        self.tour = tour
        
    @classmethod
    def from_json(cls, json_data):
        tour = list(map(Tournament.from_json, json_data['tour']))
        return cls(tour)


json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4)
print(json_data)


with open('pl.json', 'r') as f:
    data = json.load(f)
print(data)

with open('players.json', 'w') as f:
    data = json.dump(data, f)
print(data)
    