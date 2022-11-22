# Python project 2
# Written by Getachew Gessesse and Sintayehu Taddese
# Lectu. Israel Mengistu
def cosmetics():
    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait = cosmetics()


def perfumery():
    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait2 = perfumery()


def pharmaceutical():
    n1 = 1
    n2 = 0
    # line2 = 1
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1


wait3 = pharmaceutical()


def messages():
    print("Please wait and someone will assist you")
    print("******************************************")


message = "Your number is:"
lists = ["c", "p", "ph"]
print("**** Welcome to our pharmacy (drugstore):**** ")
stop = ""
while True:
    clientChoice = input("""
        choose 'C' for cosmetics
        choose 'P' for perfumery
        choose 'Ph' for pharmaceutical
        """)
    if clientChoice == lists[0]:
        print(message, "C - ", next(wait))
        messages()
    elif clientChoice == lists[1]:
        print(message, "P - ", next(wait2))
        messages()
    elif clientChoice == lists[2]:
        print(message, "PH - ", next(wait3))
        messages()
    else:
        print("Sorry, You didn't enter a valid input to visit, Please try again:")
        print("******************************************")

    # proceed = input("Do you want to take another number? ")
    # if proceed == "yes":
    #
    #     clientChoice1 = input("""
    # choose 'C' for cosmetics
    # choose 'P' for perfumery
    # choose 'Ph' for pharmaceutical
    # """)
    # elif proceed == "no":
    #     print("If so, you can choose other sites:")
    #     if stop == "no":
    #         break
    # elif clientChoice != clientChoice1:
    #     print("Sorry you chose a wrong site. you can take another number only within the same site")
    # else:
    #     continue

    stop = input("Do you want to take another number?")
    # if stop == "yes":
    #     clientChoice = input("""
    #           choose 'C' for cosmetics
    #           choose 'P' for perfumery
    #           choose 'Ph' for pharmaceutical
    #           """)
    #     if clientChoice == list[0]:
    #         wait = cosmotics()
    #         print("Your number is: C - ", next(wait) + 1)
    #         print("Please wait and someone will assist you")
    #         print("******************************************")
    #     elif clientChoice == list[1]:
    #         wait = perfumery()
    #         print("Your number is: P - ", next(wait) + 1)
    #         print("Please wait and someone will assist you")
    #         print("******************************************")
    #     elif clientChoice == list[2]:
    #         wait = pharmaceutical()
    #         print("Your number is: PH - ", next(wait) + 1)
    #         print("Please wait and someone will assist you")
    #         print("******************************************")
    #     else:
    #         print("Sorry, You didn't enter a valid input to visit, Please try again:")
    #         print("******************************************")
    if stop == "no":
        break
print("")
print("*******************************************************")
print("Dear customer, Thank you for visiting us, Keep coming: ")
print("*******************************************************")
