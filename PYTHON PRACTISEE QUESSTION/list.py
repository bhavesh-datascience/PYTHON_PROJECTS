import random
# modules examples
names = ["sansuu", "annu", "sasnkriti", "bhavesh"]
print(f"{random.choice(names)} will pay the bill")
n=len(names)
print(n)
print(names[n-1])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
postion=int(input("enter postion"))
print(fruits[postion])