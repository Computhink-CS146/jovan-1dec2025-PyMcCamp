# # # # # # # # Write all your codes for Day 3 here.
# # # # # # # # COMMENT out the previous task before going on to the next task
# # # # # # # print("hello from day3")

# # # # # # # ########################################################################
# # # # # # # # Task 1:
# # # # # # # name = input("what is your name?")
# # # # # # # title = input("what is your title?")
# # # # # # # command = input("what is your command?")
# # # # # # # print(title + ", " + name + " commands the peasants to " + command)
# # # # # # # ########################################################################
# # # # # # # Task 2:
# # # # # # name = input("what is your name?")
# # # # # # num_pens = input("enter a number")
# # # # # # print(name + " brought " + str(num_pens) + " pens.")

# # # # # # ########################################################################
# # # # # # # Task 3:
# # # # # num1 = int(input("Give me a number"))
# # # # # num2 = int(input("Give me another number"))
# # # # # num3 = num1 ** num2
# # # # # print(str(num1) + " to the power of " + str(num2) + " is " + str(num3))
# # # # # ########################################################################
# # # # # # Task 4:
# # # # price = int(999)
# # # # num1 = int(input("How many items are you buying?"))
# # # # num2 = num1 * price
# # # # print("The total cost is $" + num2)
# # # ########################################################################
# # # # Task 5:
# # # age1 = input("enter a number")
# # # age2 = input("enter another number")
# # # if age1 > age2:
# # #     print(age1 + " is larger than " + age2)
# # # elif age1 == age2:
# # #     print(age1 + " and " + age2 + " are equal" )
# # # else:
# # #     print(age2 + " is larger than " + age1)
# # ########################################################################
# # # Task 6:
# # password = "Nope"
# # entered_password = input("enter the password: ")
# # if password == entered_password:
# #     print("Access Granted!")
# # else:
# #     print("Access Denied.")
# # ########################################################################
# # # Task 7:
# import random
# for i in range(10):
#     a = random.randint(-999, 999)
#     print(a)
# ########################################################################
# # Task 8:
import random
a = random.randint(-999, 999)
b = random.randint(-999, 999)
c = a + b
d = input(a + "+" + b + "=")
if d == c:
    print("Sure. You, unfortunately, passed.")
else:
    print("Go see the principal, you failure.")
########################################################################
# Additional execises
