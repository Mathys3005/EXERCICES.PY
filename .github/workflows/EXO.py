"""
Exo 1 : ecrire une fonction pairs qui affiche les nombres pairs entre 0 et 20 (compris)
"""

def pair(n):
    for i in range(n+1):
        if i%2==0:
            print(i)
pair(20)


"""	
Exo 2: ecrire une fonction filter(liste, v) qui prend en argument 
une liste de nombre et renvoie  une liste ne contenant que les nombres superieurs ou egaux a v
"""

def filter(liste,v):
    out=[]
    for e in liste:
        if e>=v:
            out.append(e)
    return out
filter([1,2,3,4,5,65,34],2)

"""
Exo 3 : ecrire une fonction maxi(liste) qui prend comme argument une liste liste de doublets (a,b) (exemple : [(1,5), (4,8), (2,6), (3,2)], 
et qui renvoie la valeur a du doublet de la liste qui a la plus grande valeur b
"""
def maxi(liste):
    max=0
    val=0
    for e in liste:
        if e[1]>max:
            max=e[1]
            val=e[0]
    return val
maxi([(1,5), (4,8), (2,6), (3,2)])


"""
 creer une fonction moyenne qui prend une liste de nombres et renvoie la moyenne de cette liste
Exo 4 : ecrire une fonction bulletin(eleves) qui prend comme argument une liste de dictionnaires 
representant des eleves et leurs notes sous la forme d'un dictionnaire 
(pour chaque eleve : {"eleve": "BOZO Le Clown", "notes": [12,13,11]}). Cette fonction doit renvoyer un dictionnaire ayant 
chaque eleve comme clef et sa moyenne comme valeur (exemple : {"BOZO Le Clown": 12, "MACHIN Truc": 14.5})
"""
def moyenne(liste):
    res=0
    for i in liste:
        res+=i
    res=res/len(liste)
    return res
def bulletin(eleves):
    dico=[]
    for i in eleves:
        dico.append((i['eleve'],moyenne(i['notes'])))
    return dict(dico)
        
bulletin([
   {"eleve": "BOZO Le Clown", "notes": [12,13,11]},
   {"eleve": "MACHIN Truc", "notes": [14,15]},
   {"eleve": "ZEBEST Eleve", "notes": [19,20,19,20]}
])

"""
Exo 5 : ecrire une classe Cellule comportant les attributs nom et vie. L'attribut nom est defini par l'utilisateur lors de la creation de l'instance, 
et la vie est initialement egale a 100. Ecrire une methode mange qui prend en argument un nombre aliments et qui rajoute le tiers des aliments à la vie, 
une methode viellis qui enleve 3 de vie a la cellule a chaque fois qu'elle est appelee, ainsi qu'une methode dead qui renvoie True si la vie est negative 
ou nulle et False sinon

Creere une instance de Cellule appelee "marcel" et faire une boucle pour 30 jours de vie en lui donnant a manger 
tous les jours entre 1 et 10 aliments de maniere aleatoire et qui affiche a chaque tour si Marcel est en vie et quelle est sa vitalite. 
Si Marcel meurt, la boucle doit stopper.
"""
from random import randint
class Cellule:
    def __init__(self,nom:str,vie=100):
        self.nom=nom
        self.vie=vie
    def mange(self,nombre_aliments):
        self.vie+=0.3*nombre_aliments
    def viellis(self):
        self.vie-=3
    def dead(self):
        if self.vie<=0:
            return True
        return False
perso=Cellule("marcel")
n=randint(1,10)
for i in range (30):
    perso.mange(n)
    print("Jour ",i,":",perso.dead(),perso.vie)
    if perso.dead()==True:
        break
