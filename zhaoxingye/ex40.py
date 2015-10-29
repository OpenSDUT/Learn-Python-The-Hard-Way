cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else :
        return "Not Found."

cities['find_city'] = find_city
print cities
while True:
    print "State? (ENTER to quite)",
    state = raw_input("> ")
    if not state: break
    #city_found = find_city(cities,state)
    city_found = cities['find_city'](cities,state)
    print city_found
