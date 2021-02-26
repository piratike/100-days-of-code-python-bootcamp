# Code for Day 9, Exercise 2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):

    new_travel = dict()
    new_travel['country'] = country
    new_travel['visits'] = visits
    new_travel['cities'] = cities

    travel_log.append(new_travel)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



