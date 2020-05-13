# Auteur Pascal VINCENT & Ewan GRIGNOUX LEVERT
# coding: utf-8
# Mai 2020
from PIL import ImageTk  # On importe la bibliothèque PIL
import sys 
from tkinter import *
from tkinter.font import *
import random

# Création de la fenêtre principale
maFenetre = Tk()

listeTresors = [{"image" : "montre.png","valeur" : 2, "poids" : 4, "etat" : "disponible"},
                {"image" : "statue.png", "valeur" : 4, "poids" : 5.5, "etat" : "disponible"},
                {"image" : "cloche.png", "valeur" : 3, "poids" : 1.6, "etat" : "disponible"},
                {"image" : "chaine.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "chandelier.png", "valeur" : 6, "poids" : 3, "etat" : "disponible"},
                {"image" : "collier.png", "valeur" : 8, "poids" : 2, "etat" : "disponible"},
                {"image" : "coupe.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "couronne.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "horloge.png", "valeur" : 12, "poids" : 3.4, "etat" : "disponible"},
                {"image" : "anneau.png", "valeur" : 7, "poids" : 0.7, "etat" : "disponible"},
                {"image" : "assiette.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "alliances.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "saphir.png", "valeur" : 8, "poids" : 0.8, "etat" : "disponible"},
                {"image" : "ange.png", "valeur" : 15, "poids" : 10, "etat" : "disponible"},
                {"image" : "emeraude.png", "valeur" : 2, "poids" : 1.5, "etat" : "disponible"},
                {"image" : "masque.png", "valeur" : 10, "poids" : 8, "etat" : "disponible"}]
# Chargement des images
image_sac = ImageTk.PhotoImage(file="sac_a_dos.png")

def chargerImages(liste):
    listeImages = []
    for tresor in listeTresors:
        listeImages.append(ImageTk.PhotoImage(file="images/"+tresor["image"]))
    return listeImages
    
imagesTresors = chargerImages(listeTresors)

# Les variables
poids_maxi = 10
poids_sac = 0
valeur_sac = 0

# Fonctions
def dessinerTresors(liste):
    '''
    Affiche les trésors disponibles
    Ne pas modifier
    '''
    '''
    Affiche les trésors disponibles
    Ne pas modifier
    '''
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
    global listeTresors
    global poids_sac
    global valeur_sac
    #print(f"poids_sac{poids_sac}")
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
    global poids_sac, valeur_sac, listeTresors
    poids_sac = 0
    valeur_sac = 0
    for tresor in listeTresors:
        tresor['etat'] = 'disponible'
    dessinerTresors(listeTresors)

# Réglage des paramètres de la fenêtre
maFenetre.title("Chasse au trésor")  # Le titre
maFenetre.geometry('780x610+300+50')  # La position
maFenetre.configure(bg = '#44815d')  # la couleur de fond

maPolice = Font(family='Helvetica', size=16)

sac = Label(maFenetre, width=200, image = image_sac, border=0)
sac.grid(row=0,column = 0)

etiquette_sac = Label(maFenetre, font = maPolice, fg = "yellow", bg="#44815d")
etiquette_sac.grid(row=1,column = 0)

reinitialisation = Button(maFenetre, text="Réinitialiser", font = maPolice, fg = "yellow", bg="#44815d", command=init)
reinitialisation.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(maFenetre, bg="#44815d", width=560, height=600)
canvas.grid(row=0, column = 1,rowspan=3)
canvas.bind('<Button-1>',clickChoisir)

####### PROGRAMME PRINCIPAL

dessinerTresors(listeTresors)

# Lancement du gestionnaire d'événements
maFenetre.mainloop()
sys.exit() 