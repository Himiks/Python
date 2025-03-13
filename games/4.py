capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    }


travel_log = [
    {
     "country": "France",
     "cities_visited":["Paris", "Lille", "Dijon"],
     "total_visits": 12
        },
    {
     "country": "Germany",
     "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
        }
    ]


def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
travel_log = [
    {
    "country": "France",
    "visits" : 12,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berlin", "Hamburg", "Stuttgart"]
        },

    ]
    
country = input("Counrty name\n")
visits = int(input("Number of visits\n"))
list_of_cities = input("Cities visited (separated by commas): \n").split(',')



add_new_country(country, visits, list_of_cities)
print(f"l've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")


