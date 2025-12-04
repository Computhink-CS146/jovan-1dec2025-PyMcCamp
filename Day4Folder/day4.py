# # # # # Write all your codes for Day 4 here.
# # # # # COMMENT out the previous task before going on to the next task
# # # # print("hello from day4")

# # # # ########################################################################
# # # # # Task 1:
# # # num1 = 0
# # # while num1 <= 9:
# # #     print(num1)
# # #     num1 += 1
# # ##########################################################################
# # num1 = 5
# # while num1 <= 32:
# #     print(num1)
# #     num1 += 1
# ##############################################################################
# num1 = 50
# while num1 >= 1:
#     print(num1)
#     num1 -= 1
# ########################################################################
# # Task 2:
answer = input("I arrive before I’m sent. I’m received before I’m read. I can be lost even when I never existed. You create me, but you may not remember doing so. What am I?")
realAnswer = "thought"
while answer != realAnswer:
    print("NOPE. try again.")
    answer = input("I arrive before I’m sent. I’m received before I’m read. I can be lost even when I never existed. You create me, but you may not remember doing so. What am I?")
else:
    print("You have guessed correctly")

# ########################################################################
# # Additional exercises: