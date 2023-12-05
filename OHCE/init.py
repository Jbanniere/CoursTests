import datetime as dt

def appli_miroir():
    hello_user()
    user_write = input("Entrez du texte ici : ")
    texte_miroir = user_write[::-1]
    print(texte_miroir)

    if user_write == user_write[::-1]:
        print("Bien Dit ! Well done !")

    bye_user()
    
def hello_user():
    current_hour = dt.datetime.now().hour
    if 6 <= current_hour < 18:
        print("Bonjour ! Hello !")
    else:
        print("Bonsoir ! Good Evening !")

def bye_user():
    current_hour = dt.datetime.now().hour
    if 1 <= current_hour < 12:
        print("Au revoir et bonne journée !")
    elif 12 <= current_hour <18:
        print("Au revoir et bon après-midi !")
    else:
        print("Au revoir et bonne soirée !")



appli_miroir()
