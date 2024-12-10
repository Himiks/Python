class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.pop = population


    def get_info(self):
        return {
            "Name": self.name,
            "Capital":self.capital,
            "Population": self.pop
        }

class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gpd):
        super().__init__(name, capital, population)
        self.gpd = gpd

    def get_info(self):
        info = super().get_info()
        info["GPD"] = self.gpd
        return info


class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi


    def get_info(self):
        info = super().get_info()
        info["HDI"] = self.hdi
        return info



class World:
    def __init__(self):
        self.countries = []


    def add_country(self, country):
        self.countries.append(country)


    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None


world = World()
usa = DevelopedCountry("United States", "Washington, D.C.", 331000000, 22512000)
india = DevelopingCountry("India", "New Delhi", 1380004385, 0.645)
china = DevelopingCountry("China", "Beijing", 1444216107, 0.758)

world.add_country(usa)
world.add_country(india)
world.add_country(china)

country_info = world.get_country_info("India")

if country_info:
    print("Country info: ")
    for key, value in country_info.items():
        print(f"{key}:{value}")
else:
    print("Country not found")
