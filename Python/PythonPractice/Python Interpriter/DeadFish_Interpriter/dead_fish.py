# this is a simple interpriter that takes 4 instructons that opperatones on a single number
# the accumulater witch starts at 0. The Instructions are --
# i - adds one tto he accumulater
# d - subtracts one from the accumulater
# s - squares the accumulater
# o - prints the accumulater
# after each instructon the accumulater is reset to 0 if its exactly 256 or -1

user_input = input()

accumulater = 0

for program in user_input:
    if program == 'i':
        accumulater += 1
    elif program == 'd':
        accumulater -= 1
    elif program == 's':
        accumulater **= 2
    elif program == 'o':
        print(accumulater)

    if accumulater == 256 or accumulater == -1:
        accumulater = 0


# user_input = input()

# accumulater = 0

# ip = 0 # instruction pointer

# while ip < len(user_input):
#     program = user_input[ip]

#     if program == 'i':
#         accumulater += 1
#     elif program == 'd':
#         accumulater -= 1
#     elif program == 's':
#         accumulater **= 2
#     elif program == 'o':
#         print(accumulater)

#     if accumulater == 256 or accumulater == -1:
#         accumulater = 0

#     ip += 1