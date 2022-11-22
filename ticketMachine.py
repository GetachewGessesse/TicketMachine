# TicketMachine
import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        # print(timeformat,end="\r")
        time.sleep(1)
        time_sec -= 1
        print(timeformat, end='\r')
        # print(time_sec)

    print("try again ;later")



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
idList = [346369507, 342650983]
print("**** Welcome to our pharmacy (drugstore):**** ")
stop = ""
count=0
id = int(input('Enter id '))
while count < 3:
    if id == idList[0] or id == idList[1]:
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
        stop = input("Do you want to continue?")
        if stop == "no":
            break

    else:
        count1 = 0
        while count1 < 3:
            x =input('Access denied. Try again.')
            count1 += 1
        # count += 1
        countdown(10)
        break