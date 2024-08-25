#dictionary comprehension = create dictionary using an expression
#                           can replace for loops and certain lambda functions
#
#dictionary = {key:expression for (key,value) in iterable}
#dicitionary = {key:expression for (key,value) in iterable if conditional}
#dictionary = {key:(if/else) for (key,value) in iterable}
#dictionary = {key:function(value) for (key,value) in iterable}

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#cities_in_c = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_c)

#weather = {'New York':"snowing",'Boston':"sunny",'los angeles':"sunny",'Chicago':"cloudy"}
#weather_sunny = {Key:value for (Key,value) in weather.items() if value == "sunny"  }
#print(weather_sunny)

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#cities_in_c = {key:("WARM" if  value >= 40 else "COLD") for (key,value) in cities_in_F.items()}
#print(cities_in_c)

def check_temp(value):
    if value >= 70:
        return 'HOT'
    elif 69>= value >=40:
        return 'WARM'
    else:
        return 'COLD'
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_c = {key:check_temp(value) for (key,value) in cities_in_F.items()}
print(cities_in_c)
