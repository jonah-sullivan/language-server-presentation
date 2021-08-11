from twoInts import add_two_ints
import typing

firstInt = 5
secondInt = 2

additionOutput = add_two_ints(firstInt, secondInt)
print(f"firstInt: {firstInt}, secondInt: {secondInt}")
print(f"additionOutput: {additionOutput}")
print("addTwoInts.__doc__", add_two_ints.__doc__)

add_two_ints(1, 2)

add_two_ints(1, "a")
