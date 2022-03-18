greeting = input('Hello stranger! Whats your name?: ')
print(f"Nice to meet you {greeting}.")
print("My name is Gabbagoo, your personal assistant.")

while True:
    is_ready = input("Would you like to take the tutorial first? type Y or N: ")

    if is_ready == "Y":
        print("great! Let's get moving!!!")
        break


    elif is_ready == "N":
        print("Tough guy! I like that. lets skip it then.")
        break
    else:
        print("try again")
        continue


