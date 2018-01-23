import os


def menu():
    """
    function to clear the window and it is displayed again
    """

    os.system('cls')  # NOTE for windows use the option cls
    print("Select an option")
    print("\t1 - first option")
    print("\t2 - second option")
    print("\t3 - third option")
    print("\t9 - exit")


while True:

    # display menu
    menu()
    # ask to user a option
    option_menu = input("insert a number value >> ")

    if option_menu == "1":

        print("")
        input("You selected the option 1...\npress a key to continue")

    elif option_menu == "2":

        print("")
        input("You selected the option 2...\npress a key to continue")

    elif option_menu == "3":

        print("")
        input("You selected the option 3...\npress a key to continue")

    elif option_menu == "9":

        break

    else:

        print("")
        input("please select a correct option...\npress a key to continue")