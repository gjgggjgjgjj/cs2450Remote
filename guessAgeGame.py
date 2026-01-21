import random

print("Hello! I am going to try to guess your age.")
name = input("What is your name? ")


def main():
    ageGuesser()

def ageGuesser():
    while True:
        age = random.randint(15, 30)
        print("Are you " + str(age) + " years old? (y/n)")
        answer = input()

        if answer == 'y':
            print(name + " is " + str(age) + " years old.")
            return
        else:
            randResponse = random.randint(1,8)
            if randResponse == 8:
                print("Oh reeally i feel this next one will be it")
            if randResponse == 7:
                print("seriously??")
            if randResponse == 6:
                print("damn")
            if randResponse < 6:
                print("rats")

