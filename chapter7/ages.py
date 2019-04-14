prompt = "\nQuery movie prices by ages: "
prompt += "\nEnter 0 to end the program. How old are you? "

age = 0

def movie_price(age):
    if age < 3:
        return 0
    elif age < 12:
        return 10
    else:
        return 15

while True:
    age = int(input(prompt))
    if age == 0:
        break
    print('Age at', age, 'the price is', movie_price(age))
