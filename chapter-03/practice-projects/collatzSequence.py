def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

try:
    print("Enter number:")
    userNum = int(input())
    while userNum != 1:
        userNum = collatz(userNum)
except ValueError:
    print('Please enter an integer')