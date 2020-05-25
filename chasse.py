# Auteur Pascal VINCENT & Ewan GRIGNOUX LEVERT
# coding: utf-8
# Mai 2020
from PIL import ImageTk  # On importe la bibliothèque PIL
import sys 
from tkinter import *
from tkinter.font import *
import random
from tkinter.messagebox import showinfo

# Création de la fenêtre principale
maFenetre = Tk()

listeTresors = [{"image" : "montre.png","valeur" : 2, "poids" : 4, "etat" : "disponible", "ratio" : 0.5},
                {"image" : "statue.png", "valeur" : 4, "poids" : 5.5, "etat" : "disponible", "ratio" : 0.73},
                {"image" : "cloche.png", "valeur" : 3, "poids" : 1.6, "etat" : "disponible", "ratio" : 1.875},
                {"image" : "chaine.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "chandelier.png", "valeur" : 6, "poids" : 3, "etat" : "disponible", "ratio" : 2},
                {"image" : "collier.png", "valeur" : 8, "poids" : 2, "etat" : "disponible", "ratio" : 4},
                {"image" : "coupe.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "couronne.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "horloge.png", "valeur" : 12, "poids" : 3.4, "etat" : "disponible", "ratio" : 3.53},
                {"image" : "anneau.png", "valeur" : 7, "poids" : 0.7, "etat" : "disponible", "ratio" : 10},
                {"image" : "assiette.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "alliances.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "saphir.png", "valeur" : 8, "poids" : 0.8, "etat" : "disponible", "ratio" : 10},
                {"image" : "ange.png", "valeur" : 15, "poids" : 10, "etat" : "disponible", "ratio" : 1.5},
                {"image" : "emeraude.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible", "ratio" : 1.33},
                {"image" : "masque.png", "valeur" : 10, "poids" : 8, "etat" : "disponible", "ratio" : 1.25}]
# Chargement des images
image_sac = ImageTk.PhotoImage(file="sac_a_dos.png")


# Les variables
poids_maxi = 10
poids_sac = 0
valeur_sac = 0
imagesTresors = ''
default_value = StringVar()
default_value.set('10')

# Fonctions
def chargerImages(liste):
    listeImages = []
    for tresor in listeTresors:
        listeImages.append(ImageTk.PhotoImage(file="images/"+tresor["image"]))
    return listeImages

def dessinerTresors(liste):
    '''
    Affiche les trésors disponibles
    Ne pas modifier
    '''
    '''
    Affiche les trésors disponibles
    Ne pas modifier
    '''
    global imagesTresors
    imagesTresors = chargerImages(listeTresors)
    canvas.delete('all')
    etiquette_sac.configure(text = f"{poids_sac} kg   {valeur_sac} €")
    numero = 0
    for tresor in liste:
        if tresor['etat']=="disponible":
            canvas.create_image(60+(numero%4)*140, 70+ (numero//4)*150, image = imagesTresors[numero])
        canvas.create_text(60+(numero%4)*140, 140+(numero//4)*150 , fill="yellow", text = f"{tresor['poids']} kg {tresor['valeur']} €" , font = maPolice)
        numero = numero + 1

def clickChoisir(event):
    numeroTresor = - 1
    if event.x > 0 :
        numeroTresor = (event.x)//140 + 4*(event.y//150)
    if choisirTresor(numeroTresor):
        dessinerTresors(listeTresors)
    
def choisirTresor(numero):
    '''
    réagit au choix d'une objet : à compléter
    cette fonction renvoie True quand l'opération a réussi False sinon
    '''
    global listeTresors, valeur_sac, poids_sac, poids_maxi
    poids_maxi = int(poids_maxi_button.get())
    poids_maxi_button.forget()
    if numero > -1 and listeTresors[numero]['etat'] == 'disponible':
        if listeTresors[numero]['poids'] + poids_sac <= poids_maxi:
            listeTresors[numero]['etat'] = 'pris'
            poids_sac += listeTresors[numero]['poids']
            poids_sac = round(poids_sac,1)
            valeur_sac += listeTresors[numero]['valeur']
            valeur_sac = round(valeur_sac,1)
            dessinerTresors(listeTresors)
            return True

        else:
            return False
    else:
        return False
    
def init():
    global poids_sac, valeur_sac, listeTresors, poids_maxi_button, poids_maxi
    poids_sac = 0
    valeur_sac = 0
    poids_maxi = 10
    poids_maxi_button.grid(row=2,column = 0, padx=5, pady=5)
    for tresor in listeTresors:
        tresor['etat'] = 'disponible'
    dessinerTresors(listeTresors)

def choisir_valeur_maxi():
    global poids_sac, listeTresors, poids_maxi, poids_maxi_button
    poids_maxi = int(poids_maxi_button.get())
    poids_maxi_button.forget()
    init()
    sortir = False
    
    while poids_sac < poids_maxi and not(sortir):
        indice = -1
        maxi = 0
        for i in range(len(listeTresors)):
            if listeTresors[i]['etat'] == "disponible":
                if listeTresors[i]['valeur'] >= maxi:
                    if (listeTresors[i]['poids']+ poids_sac) <= poids_maxi:
                        maxi = listeTresors[i]['valeur']
                        indice = i
        if indice != -1:
            choisirTresor(indice)
        else:
            sortir = True
        """print(listeTresors[indice]['image'])
        print(f"poids: {listeTresors[indice]['poids']}, valeur: {listeTresors[indice]['valeur']}")
        print(f'poids du sac: {poids_sac}')
        print(f"etat: {listeTresors[indice]['etat']}")"""
    
def Choisir_poids_mini():
    global poids_sac, listeTresors, poids_maxi, poids_maxi_button
    poids_maxi = int(poids_maxi_button.get())
    poids_maxi_button.forget()
    init()
    sortir = False
    while poids_sac < poids_maxi and not(sortir):
        indice = -1
        mini = float('inf')
        for i in range(len(listeTresors)):
            if listeTresors[i]['etat'] == "disponible":
                if listeTresors[i]['poids'] <= mini:
                    if (listeTresors[i]['poids']+ poids_sac) <= poids_maxi:
                        mini = listeTresors[i]['poids']
                        indice = i
        if indice != -1:
            choisirTresor(indice)
        else:
            sortir = True
        """print(listeTresors[indice]['image'])
        print(f"poids: {listeTresors[indice]['poids']}, valeur: {listeTresors[indice]['valeur']}")
        print(f'poids du sac: {poids_sac}')
        print(f"etat: {listeTresors[indice]['etat']}")"""

def Choisir_ratio():
    global poids_sac, listeTresors, poids_maxi, poids_maxi_button
    poids_maxi = int(poids_maxi_button.get())
    poids_maxi_button.forget()
    init()
    sortir = False
    while poids_sac < poids_maxi and not(sortir):
        indice = -1
        maxi = 0
        for i in range(len(listeTresors)):
            if listeTresors[i]['etat'] == "disponible":
                if listeTresors[i]['ratio'] >= maxi:
                    if (listeTresors[i]['poids']+ poids_sac) <= poids_maxi:
                        maxi = listeTresors[i]['ratio']
                        indice = i
        if indice != -1:
            choisirTresor(indice)
        else:
            sortir = True
        """print(listeTresors[indice]['image'])
        print(f"poids: {listeTresors[indice]['poids']}, ratio: {listeTresors[indice]['ratio']}")
        print(f'poids du sac: {poids_sac}')
        print(f"etat: {listeTresors[indice]['etat']}")"""

# Réglage des paramètres de la fenêtre
maFenetre.title("Chasse au trésor")  # Le titre
maFenetre.geometry('1090x610+300+50')  # La position
maFenetre.configure(bg = '#44815d')  # la couleur de fond
maPolice = Font(family='Helvetica', size=16)

showinfo('Chasse au Trésor',"Vous êtes chasseur de trésors ! Après de longues heures d’aventure, des dangers évités de justesse, et malgré une armée de pilleurs à vos trousses, vous avez trouvé un énorme trésor. Vous êtes heureux, et sautez de joie ! Finalement vous retrouvez votre calme et commencez à réfléchir vite. Votre sac à dos est assez solide pour n’emporter que 10 kg et le trésor pèse bien plus... Il va vous falloir choisir les objets à emporter. Heureusement vous êtes prévoyant et vous avez la liste des objets présents dans le coffre ainsi que leur poids et leur valeur.")

sac = Label(maFenetre, width=200, image = image_sac, border=0)
sac.grid(row=0,column = 0, padx=5, pady=5)

poids_maxi_label = Label(maFenetre, text='Choisir le poids du sac. \n (Si non définit, vaut 10kg.)', font = maPolice, fg = "yellow", bg="#44815d")
poids_maxi_label.grid(row=1,column = 0, padx=5, pady=5)

poids_maxi_button = Spinbox(from_=1, to=49, textvariable=default_value)
poids_maxi_button.grid(row=2,column = 0, padx=5, pady=5)

etiquette_sac = Label(maFenetre, font = maPolice, fg = "yellow", bg="#44815d")
etiquette_sac.grid(row=3,column = 0, padx=5, pady=5)

maxi_button = Button(maFenetre, text="Prendre ceux qui ont le plus de valeur.", font = maPolice, fg = "yellow", bg="#44815d", command=choisir_valeur_maxi)
maxi_button.grid(row=4, column=0, padx=5, pady=5)

mini_button = Button(maFenetre, text="Prendre ceux qui ont le plus petit poids.", font = maPolice, fg = "yellow", bg="#44815d", command=Choisir_poids_mini)
mini_button.grid(row=5, column=0, padx=5, pady=5)

mini_button = Button(maFenetre, text="Prendre ceux qui ont le meilleur ratio valeur/poids.", font = maPolice, fg = "yellow", bg="#44815d", command=Choisir_ratio)
mini_button.grid(row=6, column=0, padx=5, pady=5)

reinitialisation = Button(maFenetre, text="Réinitialiser", font = maPolice, fg = "yellow", bg="#44815d", command=init)
reinitialisation.grid(row=7, column=0, padx=5, pady=5)

canvas = Canvas(maFenetre, bg="#44815d", width=560, height=600)
canvas.grid(row=0, column = 1,rowspan=8)
canvas.bind('<Button-1>',clickChoisir)

####### PROGRAMME PRINCIPAL

dessinerTresors(listeTresors)

# Lancement du gestionnaire d'événements
maFenetre.mainloop()
sys.exit() 