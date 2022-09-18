#excercise 4.2
import random
print("Welcome to treasure island")
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


person_pay = random.choice(names)
print(person_pay + " will pay today.")

#lists

#methods of lists:
#1. list.append(x)
#2. list.extend(iterable)
#3. list.insert(i,x)
#4. remove(x)
#5. list.pop([i])
#6. clear,index,sort,count,reverse