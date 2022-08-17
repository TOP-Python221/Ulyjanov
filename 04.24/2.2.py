age_str = input("Введите свой возраст ")
age = int(age_str)
if age<= 13:
    print("детство")
elif age >=14 and age <=24:
    print("молодость")
elif age >=25 and age <= 59:
    print("зрелость")
else:
    print("старость")
