#Created by: Owen Whalley
#Created on: 2022-10-06
#The code asks the users age, and compares it to age requirements for R rated, PG13, and G rated movies. It then tells the user what movie they can watch.
age = int(input("What is your age? "))
if age >= 17:
  print("You can see an R rated movie alone.")
elif age >= 13:
  print("You can see a PG13 movie alone.")
else:
  print("You can see a G rated movie alone.")