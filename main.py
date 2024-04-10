#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
import json
Purchases = []

with open('Purchases.json', 'r') as openfile:
    # Reading from json file
    Purchases = json.load(openfile)
# Ļauj lietotājam pieejamo līdzekļu jomā izvēlēties programmu.
while True:
    print("\nThe check:")
    print("1. Pievienot produktu")
    print("2. Dzēst produktu no čeka")
    print("3. atcelt ievadu / iztukšot preču sarakstu")
    print("4. piemērot atlaidi, ievadīt summu procentos")
    print("5. beidz")
    choice = input("Enter your choice: ")

    Purchases_file = open('Purchases.json') # opening JSON file
    Purchases = json.load(Purchases_file) # returns JSON object as a dictionary
    Purchases_file.close()
    # Ļauj lietotājam pievienot produktu un tā cenu čekam.
    if choice == "1":
        Purchase_title = input("Enter purchase title: ")
        Purchase_price = int(input("Enter purchase price: "))
        thisdict = {
            "Purchase": Purchase_title,
            "Purchase price": Purchase_price,
            }
        Purchases.append(thisdict)
        print(Purchases)
        with open("Purchases.json", "w") as outfile:
            json.dump(Purchases, outfile)
        pass
    # Ļauj ar indeksa palīdzību izdzest produktu no čeka.
    elif choice == "2":
        id = int(input("Enter the index of purchase the  to remove: "))
        id = id - 1 
        Purchases.pop(id)
        print(Purchases)
        pass
    # Ļauj notīrīt čeku.
    elif choice == "3":
       
        Purchases.clear()
        print(Purchases)
        with open("Purchases.json", "w") as outfile:
            json.dump(Purchases, outfile)
        print(Purchases)
        pass
    # Ļauj ievadīt pircēja atlaidi.
    elif choice == "4":
        sale = int(input("Enter your buyer sale (%): "))
        pass
    # Aizver programmu.
    elif choice == "5":
        break
