import random

miscellaneous = {'Thirst' :0,  'Camel tiredness' : 0, }
status = {'Canteens': 4, 'Miles traveled': 0, 'native distance': -20}

def show_status():
    for k, v in status.items():
        print(k, v)

def rest():
    status['native distance'] += random.randint(7,14)
    miscellaneous['Camel tiredness'] = 0
    print("Your Camel is happy")

def full_speed():
    status['native distance'] += random.randint(7,14)
    status['Miles traveled'] += random.randint(10,20)
    miscellaneous ['Thirst'] += 1
    miscellaneous['Camel tiredness'] += random.randint(1,3)
    print("You have traveled ", status['Miles traveled'], " miles")

def moderate_speed():
    status['native distance'] += random.randint(7, 14)
    status['Miles traveled'] += random.randint(5, 12)
    miscellaneous['Thirst'] += 1
    miscellaneous['Camel tiredness'] += 1
    print("You have traveled ", status['Miles traveled'], " miles")

def drink_water():
    if status['Canteens'] <= 0:
        print("You don't have more canteens full")
    else:
        status['Canteens'] -= 1
        miscellaneous ['Thirst'] = 0


print("Welcome to Camel!", )
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

def main():
    done = False
    while not done:
        if miscellaneous['Thirst'] >= 4:
            print("You are thirsty")
        elif miscellaneous['Thirst'] == 6:
            print("you died of thirst")
            done = True
        if miscellaneous['Camel tiredness'] >= 5:
            print("your camel is tired")
        elif miscellaneous['Camel tiredness'] >= 8:
            print("your camel is dead")
            done = True
        if status['native distance'] >= status['Miles traveled']:
            print("the natives have caught you")
            done = True
        elif status['Miles traveled'] >= 200:
            done = True
        elif (status['Miles traveled']- status['native distance']) <= 15:
            print("The natives are getting close")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")
        choice = str(input(("What is your choice? "))).upper()
        if choice == "Q":
            done = True
        elif choice == "E":
            show_status()
        elif choice == "D":
            rest()
        elif choice == "C":
            full_speed()
        elif choice == "B":
            moderate_speed()
        elif choice == "A":
            drink_water()


main()