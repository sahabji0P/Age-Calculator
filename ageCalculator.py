from datetime import date

def calculate_age(Birth_year):

  current_year = date.today().year

  if Birth_year>current_year:
    
    raise ValueError("Invalid Birth year")
  
  else:

    age=current_year-Birth_year
    return age  

try:


  Year=int(input("Enter the birth year:"))
  age=calculate_age(Year)
  print("you are",age,"Years old")

except:
  print("Invalid ")
