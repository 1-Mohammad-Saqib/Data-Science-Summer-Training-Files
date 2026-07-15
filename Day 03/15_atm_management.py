# create a atm system that first asks language then asks card if card is valid then asks for pin if pin is valid then gives options to user to choose from 1.widrow cash 2.check balance 3.change pin 4.help 5.exit after widraw cash it should give option to go one step back to main menu or exit after check balance it should give option to go one step back to main menu or exit after change pin it should give option to go one step back to main menu or exit after help it should give option to go one step back to main menu or exit after exit it should print thank you for using our atm have a great day
print('''Welcome to ATM 
      Please select your language:''')
language = input("1. English\n2. Urdu\n3. Hindi\n")
if language in ['1', '2', '3']:
    print("Please insert your card")
    card = input("Card: ")
    if card == 'valid':
        pin = '1234'
        entered_pin = input("Please enter your pin:")
        if entered_pin == pin:
            print('''Please select an option:
                  \t1. Withdraw Cash
                  \t2. Check Balance
                  \t3. Change Pin
                  \t4. Help
                  \t5. Exit
                  ''')
            option = input("Option:")
            if option == '1':
                amount = input("Enter the amount to withdraw:")
                print(f"You have withdrawn {amount} cash.")
            elif option == '2':
                print("Your balance is $1000.")
            elif option == '3':
                new_pin = input("Enter your new pin:")
                print("Your pin has been changed successfully.")
            elif option == '4':
                print("For help, please contact customer support at 123-456-7890.")
            elif option == '5':
                print("Thank you for using our ATM. Have a great day!")
            else:
                print("Invalid option. Please try again.")

            choice = input("Do you want to go back to the main menu or exit? (back/exit): ")
            if choice.lower() == 'back':
                print('''Please select an option:
                      \t1. Withdraw Cash
                      \t2. Check Balance
                      \t3. Change Pin
                      \t4. Help
                      \t5. Exit
                      ''')
                option = input("Option:")
                if option == '1':
                    amount = input("Enter the amount to withdraw:")
                    print(f"You have withdrawn {amount} cash.")
                elif option == '2':
                    print("Your balance is $1000.")
                elif option == '3':
                    new_pin = input("Enter your new pin:")
                    print("Your pin has been changed successfully.")
                elif option == '4':
                    print("For help, please contact customer support at 123-456-7890.")
                elif option == '5':
                    print("Thank you for using our ATM. Have a great day!")
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid pin. Please try again.")
    else:
        print("Invalid card. Please try again.")
else:
    print("Invalid language selection. Please try again.")