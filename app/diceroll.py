import random

def main():
    min = 1
    max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(1,6))

    roll_again = input("Roll the dices again?")

    if __name__ == "__main__":
 
        main()