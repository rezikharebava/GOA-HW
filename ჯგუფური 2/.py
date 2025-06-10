

def create_user():
    print("Enter user details:")
    name = input("Name: ")
    surname = input("Surname: ")
    born_year = int(input("Born Year: "))
    password = input("Password: ")
    email = input("Email: ")
    


    print(f"User {name} {surname} created successfully!")



    
    

# ლოგინი
users = {
    "admin": "password123",
    "user1": "mypassword"
}

def login():
    print("Log In System")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

login()




# converation
def conversation():
    print("გამარჯობა! როგორ ხარ?")
    answer = input("თქვი როგორ ხარ? ")
    
    if 'კარგად' in answer or 'სუპერ' in answer:
        print(" მიხარია რომ კარგად ხარ!")
    elif 'არამშვენიერ' in answer or 'ნაღველი' in answer:
        print("ვწუხვარ. იმედია მალე გაგიადვილდება.")
    else:
        print("ძაან კაია რომ კარგად ხარ!")


conversation()















def view_account(users, email):
    for user in users:
        if user['gmail'] == email:
            print("--- User Account ---")
            print(f"Name: {user['name']} {user['surname']}")
            print(f"Birth Year: {user['birth_year']}")
            print(f"Gmail: {user['gmail']}")
            print(f"Card Type: {user['card_type'] if user['card_type'] else 'No card assigned'}")
            return
    print("Account not found!")

users_list = [
    {"name": "რეზი", "surname": "ხარებავა", "birth_year": "2010", "gmail": "kharebavareziko@gmail.com", "password": "password123", "card_type": "visa"}
]
view_account(users_list, "kharebavareziko@gmail.com")















import sqlite3

def perform_transaction():

    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION;")
        
        cursor.execute("INSERT INTO accounts (name, balance) VALUES ('Alice', 1000);")
        
        cursor.execute("INSERT INTO accounts (name, balance) VALUES ('Bob', 500);")
        
        cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Alice';")
        cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Bob';")
        
        connection.commit()
        print("ტრანზაქცია წარმატებით შესრულდა.")
        
    except sqlite3.Error as e:

        connection.rollback()
        print(f"შეცდომა: {e}")
        
    finally:

        connection.close()

perform_transaction()


















import random

def choose_card():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    suit = random.choice(suits)
    rank = random.choice(ranks)
    
    card = f"{rank} of {suit}"
    return card


selected_card = choose_card()
print(f"მოხდა არჩევა: {selected_card}")
