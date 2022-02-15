basketball_players = [
    {"first name" : "Jill", "last name" : "Haung", "team" : "Gators"},
    {"first name" : "Janko", "last name" : "Barton", "team" : "Sharks"},
    {"first name" : "Wanda", "last name" : "Vakulskas", "team" : "Sharks"},
    {"first name" : "Jill", "last name" : "Moloney", "team" : "Gators"},
    {"first name" : "Luuk", "last name" : "Watkins", "team" : "Gators"}
]

football_players = [
    {"first name" : "Hanzla", "last name" : "Radosti", "team" : "32ers"},
    {"first name" : "Tina", "last name" : "Watkins", "team" : "Barleycorns"},
    {"first name" : "Alex", "last name" : "Patel", "team" : "32ers"},
    {"first name" : "Jill", "last name" : "Haung", "team" : "Barleycorns"},
    {"first name" : "Wanda", "last name" : "Vakulskas", "team" : "Barleycorns"}
]

def find_multisport_athlets(basketball, football): #hash table algorithm (O(N^2) => O(N))
    multiathlets = []
    basketball_hash_table = []
    for i in basketball:
        basketball_hash_table.append(i["first name"] + " " + i["last name"])
    for i in football:
        if i["first name"] + " " + i["last name"] in basketball_hash_table:
            multiathlets.append(i["first name"] + " " + i["last name"])
    return multiathlets

print(find_multisport_athlets(basketball_players, football_players))