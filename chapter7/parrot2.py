prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ''

while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(message)
print('end of game')
