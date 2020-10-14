#ceci est un commentaire, il ne sera pas exécuté par la machine

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on appel la fonction print pour écrire dans la console
    print("hello World")
    #on definit la taille de la fenêtre
    size(400, 400)
    #on définit la couleur avec laquelle on va remplir les formes suivantes
    fill(128, 0, 0)
    #vide la fenêtre
    clear()
    #dessine une ellipse avec les paramètres suivant x, y, largeur , hauteur
    ellipse(200, 200, 50, 100)
    #on change le frameRate de l'application
    frameRate(60)
    
# La fonction draw est une fonction qui se répéte en boucle
def draw():
    clear()
    fill(255)
    #on récupère les coordonnés de la souris avec les coordonne X et Y
    ellipse(mouseX, mouseY, 80, 80)
    #on fait une ellipse au centre en divisant par deux la longeure et largeure total
    ellipse(width/2 + cos(millis() *0.001) * 100, height/2 + cos(millis()*0.002) * 100, 40, 40)
                                    
