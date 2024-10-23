#Jackson M.

def encode(password):

    encrypted = ""
    for x in password:

        temp = int(x) + 3
        if temp > 9:
            temp -= 10
        
        encrypted = encrypted + str(temp)

    return encrypted

if __name__ == "__main__":

    while(1):
        print("       Menu\n    __________\n\n1. encode password\n2. decode password\n3. exit")
        choice = input("\nenter menu option: ")

        if choice == "1":
            user_input = input("enter password: ")

            new_password = encode(user_input)

            print(f"Encoded password is: {new_password}")

        elif choice == "2":

            pass

        elif choice == "3":

            break

        else:

            print("not a valid menu option")