# მომხმარებლების მონაცემები
users = []

def create_user():
    print("Enter user details:")
    name = input("Name: ")
    surname = input("Surname: ")
    born_year = int(input("Born Year: "))
    password = input("Password: ")
    email = input("Email: ")
    
    # მომხმარებლის მონაცემების შენახვა
    user = {
        "name": name,
        "surname": surname,
        "born_year": born_year,
        "password": password,
        "email": email,
        "cards": []
    }
    users.append(user)
    print(f"User {name} {surname} created successfully!")

def add_card(user):
    card_type = input("Enter card type (e.g., mastercard, visa, amex): ")
    balance = float(input("Enter balance: "))
    currency = input("Enter currency (e.g., usd, gel): ")
    user["cards"].append([card_type, balance, currency])
    print(f"Card {card_type} added successfully!")

def get_user_by_email(email):
    for user in users:
        if user["email"] == email:
            return user
    return None

def transfer_funds(from_user, to_user, from_card_index, to_card_index, amount):
    from_card = from_user["cards"][from_card_index]
    to_card = to_user["cards"][to_card_index]

    if from_card[1] >= amount:
        from_card[1] -= amount
        to_card[1] += amount
        print(f"Transfer successful: {amount} {from_card[2]} from {from_user['name']} to {to_user['name']}")
    else:
        print("Insufficient funds.")

def convert_currency(amount, from_currency, to_currency):
    conversion_rates = {
        ('gel', 'usd'): 0.38,
        ('usd', 'gel'): 2.63
    }
    
    if from_currency == to_currency:
        return amount

    if (from_currency, to_currency) in conversion_rates:
        return amount * conversion_rates[(from_currency, to_currency)]
    else:
        print(f"Conversion not available between {from_currency} and {to_currency}.")
        return None

def transfer_with_conversion(from_user, to_user, from_card_index, to_card_index, amount, from_currency, to_currency):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        transfer_funds(from_user, to_user, from_card_index, to_card_index, converted_amount)
        print(f"Amount {amount} {from_currency} converted to {converted_amount} {to_currency}")
    else:
        print("Conversion failed.")

# მთავარი პროგრამა
def main():
    print("Welcome to the Bank!")
    
    while True:
        print("\nMenu:")
        print("1. Create user account")
        print("2. Add card to existing user")
        print("3. Transfer funds between users")
        print("4. Convert currency and transfer")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            create_user()
        elif choice == "2":
            email = input("Enter the email of the user: ")
            user = get_user_by_email(email)
            if user:
                add_card(user)
            else:
                print("User not found!")
        elif choice == "3":
            from_email = input("Enter sender's email: ")
            to_email = input("Enter receiver's email: ")
            
            from_user = get_user_by_email(from_email)
            to_user = get_user_by_email(to_email)
            
            if from_user and to_user:
                print("\nSelect card from sender:")
                for i, card in enumerate(from_user["cards"]):
                    print(f"{i}. {card[0]} - {card[1]} {card[2]}")
                from_card_index = int(input("Enter card index: "))
                
                print("\nSelect card from receiver:")
                for i, card in enumerate(to_user["cards"]):
                    print(f"{i}. {card[0]} - {card[1]} {card[2]}")
                to_card_index = int(input("Enter card index: "))
                
                amount = float(input("Enter amount to transfer: "))
                transfer_funds(from_user, to_user, from_card_index, to_card_index, amount)
            else:
                print("One or both users not found!")
        elif choice == "4":
            from_email = input("Enter sender's email: ")
            to_email = input("Enter receiver's email: ")
            
            from_user = get_user_by_email(from_email)
            to_user = get_user_by_email(to_email)
            
            if from_user and to_user:
                print("\nSelect card from sender:")
                for i, card in enumerate(from_user["cards"]):
                    print(f"{i}. {card[0]} - {card[1]} {card[2]}")
                from_card_index = int(input("Enter card index: "))
                
                print("\nSelect card from receiver:")
                for i, card in enumerate(to_user["cards"]):
                    print(f"{i}. {card[0]} - {card[1]} {card[2]}")
                to_card_index = int(input("Enter card index: "))
                
                amount = float(input("Enter amount to transfer: "))
                from_currency = input("Enter currency to convert from: ")
                to_currency = input("Enter currency to convert to: ")
                
                transfer_with_conversion(from_user, to_user, from_card_index, to_card_index, amount, from_currency, to_currency)
            else:
                print("One or both users not found!")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()