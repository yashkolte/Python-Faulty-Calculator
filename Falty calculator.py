"""
Falty Calculator
"""

print("\t\t\t\t\t\t\t\t Exam Calculator\n ")
print("NOTE : Don't calculate the number which are already in questions\n")

#43* = 555, 56+9 = 77, 15-6

inp1 = input("Operator\n")
inp2 = input("First Number\n")
inp3 = input("Second Number\n")

new_input = inp2 + inp1 + inp3

if new_input == "43*3":
    print("Your answer is ",555,"\n")

elif new_input == "56+9":
    print("Your answer is ",77,"\n")

elif new_input == "15-6":
    print("Your answer is ",65,"\n")

elif inp1 == "*":
    print("Your answer is ",int(inp2)* int(inp3),"\n")

elif inp1 == "+":
    print("Your answer is ",int(inp2) + int(inp3),"\n")

elif inp1 == "-":
    print("Your answer is ",int(inp2) - int(inp3),"\n")

elif inp1 == "/":
    print("Your answer is ",int(inp2) / int(inp3),"\n")

else :
    print("You Type Wrong Number\n")