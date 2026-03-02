from pyscript import document, display

def Button(event): #when the button is pressed, this shows the list of players that are shown below

    players = [
    "Ebtisam Al Hazmi",
    "Aeiou Alvarez",
    "Ethan Belsa",
    "Giana Bernas",
    "Julianna Calaycay",
    "Jamila Castelo",
    "Francesca Cruz",
    "Ely Defensor",
    "Danielle Dimasuhid",
    "Althea Francisco",
    "Cristina Hsu",
    "Denise Juatchon",
    "Judah Judge",
    "Francis Lilagan",
    "Sam Luna",
    "Enzo Macaranas",
    "Pain Mateo",
    "Ashley Mondragon",
    "Lance Naldoza",
    "Gabriel Natividad",
    "Sofia Ng",
    "Hendrich Ong",
    "Trisha Paz",
    "Miguel Ramos",
    "Queeny Ramos",
    "Samantha Ramos",
    "Ashlei Reodica",
    "Vaughn Repolona"
    ]

    display("Intramurals Players:\n") #when the button is pressed, this displays the list of players that are shown above.

    for i in range(len(players)):
        display(str(i+1) + ". " + players[i])