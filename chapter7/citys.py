prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program. "

city = ''
while True:
    city = input(prompt)
    if city == 'quit':
        break
    print("I'd love to go to", city.title(), "!")
