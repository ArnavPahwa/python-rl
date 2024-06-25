'''
Q1.1: Try block ecloses code that may cause an error
    Except bloack catches and handles the error
    Else block runs if try block had no errors
    finally bloack runs in all cases, ignoring any errors
1.2: Having many different excpet bloacks lets us detect the spefic error, like zerodivisionerror, import error, etc
1.3 - expection chaining in python tells us the specififc error, thus saving us time by telling the cause of the error

Q2.1 Custom exceptions in python are used for when there is no coding error, but there may be a logical error - ex age being -ve
Q2.3 - examply shown in .2 and in case age is being asked - to ensure its not too high or to low
Q2.3 - example - opening a file, adding a given str to it, closing file. try takes string andd ensures it is correct, else adds string, finaly closes file


'''
import pandas as pd
class InvalidAgeError(Exception):
    pass
try:
    pd.read_csv('abc.csv')
except FileNotFoundError:
    print("file does not exist")

try:
    a = int(input("enter age"))
    if a > 120 or a < 0:
        raise InvalidAgeError
    else:
        print("age is valid")
except InvalidAgeError :
    print("Age is invalid. Please enter a valid age")


i = [1,2,3,4,5.6]
num = 0
try:
    for n in i:
        num = num+n
    print(num/(len(i)))
except ZeroDivisionError :
    print("list has no intgers")
