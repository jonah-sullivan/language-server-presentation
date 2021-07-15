from twoInts import addTwoInts
from twoInts import multiplyTwoInts

firstInt = 5
secondInt = 2

additionOutput = addTwoInts(firstInt, secondInt)
addTwoInts()
print(f"firstInt: {firstInt}, secondInt: {secondInt}")
print(f"additionOutput: {additionOutput}")
print("addTwoInts.__doc__", addTwoInts.__doc__)

multiplicationOutput = multiplyTwoInts(firstInt, secondInt)
print(f"firstInt: {firstInt}, secondInt: {secondInt}")
print(f"multiplicationOutput: {multiplicationOutput}")
print("multiplyTwoInts.__doc__", multiplyTwoInts.__doc__)
