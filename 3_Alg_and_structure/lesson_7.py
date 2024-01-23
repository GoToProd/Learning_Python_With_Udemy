country_code = [('10', 'USA'), ('2', 'UK'), ('3', 'India')]

vote = {
    10: 'USA',
    2: 'UK',
    3: 'India'
}

def search(list,key):
    if key in list:
        for i in list:
            if i == key:
                return list[i]
            
print(search(vote,10))