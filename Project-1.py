# course = '''
# hi monir

# There is my first email to you.

# thank you 
# for support me.

# '''
# print(course)

# formated string
# first_name = "Md"
# last_name = "Moniruzzaman"
# message = first_name+' ' + last_name + ' is a coder.'
# msg = f'{first_name} [{last_name}] is a coder.'
# print(msg)

# string method

# course = 'Python for Begginers'

# print(len(course))
# print(course.upper())
# print(course.find("f"))
# print(course.replace('Begginers','Beginners'))
# print(course.title())

# if statement

# price = 1000000
# has_good_creadit = True

# if has_good_creadit:
#     down_payment = 0.1*price
# else:
#     down_payment = 0.2*price

# print(f'Down payment: ${down_payment}')    

# logical operator
# name = 'monir'

# if len(name)<3:
#     print('Name must be at least 3 charecters.')
# elif len(name)>50:
#     print('Name can be a maximum 50 charecters.')
# else:
#     print('Name looks good')

# nested for loop

numbers = [3,1,3,1,3]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# finding maximum number from list
number = [2, 3, 5, 10, 15, 11, 8, 6, 9, 7]
max = number[0]
for item in number:
    if item > max:
        max = item
print(max)