#Part 1: Creating two dictionaries with info about pets. 
Mufasa = {
    "Type" : "Cat", 
    "Color" : "Orange",
    "Nickname" : "Foss",
    "Owner" : "Brit"
}

Millie = {
    'Type' : 'Dog',
    'Color' : 'White',
    'Nickname' : 'Mimi',
    'Owner' : 'Mari'
}

for key,value in Mufasa.items():
    print(key + ": " + value)

for key,value in Millie.items():
    print(key + ": " + value)

#Part 2 International Cities (added 3 of my own to the list because that's what it sounded like I was supposed to do)
print("*** Part 2 ***")
Turkey = {'Capital': 'Ankara'}
Japan = {'Capital': 'Tokyo'}
Nigeria = {'Capital': 'Abuja'}
England = {'Capital': 'London'}
France = {'Capital': 'Paris'}
Belgium = {'Capital': 'Brussels'}
#Adding population data
Turkey['Population'] = '84.78 million'
Japan['Population'] = '125.7 million'
Nigeria['Population'] = '213.4 million'
England['Population'] = '53.01 million'
France['Population'] = '66.9 million'
Belgium['Population'] = '11.35 million'
#Adding and interesting fact
Turkey["Interesting fact"] = "On two continents"
Japan["Interesting fact"] = "Where most zippers are from"
Nigeria["Interesting fact"] = "Over 500 indigenous languages"
England["Interesting fact"] = "More chickens than people"
France["Interesting fact"] = "Most visited country in the world"
Belgium["Interesting fact"] = "Birthplace of Audrey Hepburn"
#Adding top language spoken by locals
Turkey['Top Language'] = 'Turkish'
Japan['Top Language'] = 'Japanese'
Nigeria['Top Language'] = 'Hausa'
England['Top Language'] = 'English'
France['Top Language'] = 'French'
Belgium['Top Language'] = 'Dutch'
for k, v in Turkey.items():
    print(k + " : "  + v)
for k, v in Japan.items():
    print(k + " : "  + v)
for k, v in Nigeria.items():
    print(k + " : "  + v)
for k, v in England.items():
    print(k + " : "  + v)
for k, v in France.items():
    print(k + " : "  + v)
for k, v in Belgium.items():
    print(k + " : "  + v)

#Part 3 Pizza Orders
print("Part 3")
pizza_order = {
    "name" : "Fred", 
    "size" : "medium", 
    "crust" : "stuffed", 
    "toppings" : "extra cheese, pineapple, canadian bacon"
}

print("Thank you for your order, " + pizza_order.get("name"))
print("You have ordered a " + pizza_order.get("size") + ", "
      + pizza_order.get("crust") + "-crust pizza with the following toppings: " 
      + pizza_order.get("toppings"))
