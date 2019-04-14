responses = {}

active = True

while active:
    name = input("\nWhat's your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        active = False

print('\n--- Poll Results ---')

for name, respond in responses.items():
    print(name, 'would like to climb', respond)
