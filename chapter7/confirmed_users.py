# step 1: create a user list to be confirmed
# step 2: create a confirmed user list (initial empty)

unconfirmed_users = ['tom', 'brian', 'erqidiy']
confirmed_users = []

# verify each unconfirmed user until the unconfirmed user list is empty

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed: ')
for user in confirmed_users:
    print(user.title())
