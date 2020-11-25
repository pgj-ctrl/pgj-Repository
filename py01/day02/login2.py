import getpass

user = input('username: ')
password = getpass.getpass('passd: ')
# if password == '123456' and user == 'bob':
#     print('Login successful')
# else:
#     print('Login inorrect')

if user == 'bob':
    if password == '123456':
        print('Login successful')
    else:
        print('Login inorrect')
else:
    print('Login inorrect')