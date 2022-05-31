def greet_user(myName):
    print('It is nice to meet you, ' + myName)


print('Hi there!')
print('What is your name?')
name = input()
greet_user(name)

def square(number):
    return number * number


print(square(3))

#create a function that takes a list of numbers and returns a new list with only the even numbers 
def even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

even_numbers()