# Part 1 

day = "5"
month = "August" 
year = "1979"

my_birthday = month + " " + day + ", " + year

print(my_birthday)

# Part 2
first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = first + " " + second + " " + third + " " + fourth


print(final.upper())

#Part 3
#Felt silly having only the age of 15, so I modified 

ages = [9, 10, 11, 13, 15, 17, 19]
for age in ages:
    if age < 10:
        print("Not permitted")
    elif age > 10 and age < 15:
        print("Permitted with a parent")
    elif age > 15 and age < 18:
        print("Permitted to attend with anyone over 18")
    else:
        print("Permitted to attend alone")
    



#Here is the original, with just the age of 15 (but changable): 
age = 15
rating = " "
if age <= 10:
    rating = "Not permitted"
elif age >= 10 and age <= 15:
    rating = "Permitted with a parent"
elif age >= 15 and age <= 18:
    rating = "Permitted with anyone over 18"
else:
    rating = "Permitted to attend alone"

print(rating)







