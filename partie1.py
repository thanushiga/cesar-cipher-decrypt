#Fonction qui parcourt chaque caractere minuscule du texte et effectue un decalage selon la cle donnee
def encrypt(texte, cle):
    texte_chiffre= "" #On déclare la variable texte_chiffre comme une chaîne de caractère vide afin de stocker le texte chiffré
    #On parcourt chaque caractère dans le texte en clair
    for caractere in texte:
        if caractere.islower(): #On vérifie si le caractère est une lettre minuscule
            #Pour trouver la position du caractère dans l'alphabet avec 26 caractère (indexées de 0-25)
            #La fonction ord() renvoie la valeur ASCII du caractère
            #En soustrayant la valeur ASCII par la valeur 'a' on obtient un nombre qui représente la position du caractère dans l'alphabet
            position_caractere = ord(caractere) - ord('a')
            #On applique le décalage de la clé au caractère actuel
            #On ajoute la clé au numéro de position du caractère et on utilise l'opérateur module pour que le résultat reste dans la plage d'index 0-25
            #On ajoute 'a' à la valeur résultante pour ramener la position 
            #On reconvertit la position calculée en un caractère ASCII des lettres minuscules en ajouter la valeur ASCII de 'a' au résultat
            nouveau_caractere = chr((position_caractere + cle) % 26 + ord('a'))
            #On ajoute le caractère chiffré à la chaîne texte_chiffre
            #Le processus est itéré pour chaque caractère présent dans le texte en clair afin de chiffré l'ensemble du texte selon la clé
            texte_chiffre += nouveau_caractere
        else:
            #Si le caractère n'est pas une lettre minuscule on le garde tel quel
            texte_chiffre += caractere
    return texte_chiffre

#Fonction qui prend comme entrée un texte chiffré et une clé et déchiffre le texte en utilisant le code de César pour retourner le texte en clair
def decrypt(texte_chiffre, cle):
    texte_clair = "" #On déclare la variable texte_clair comme une chaîne de caractère vide pour stocker le texte en clair
    #On parcourt chaque caractère dans le texte chiffré
    for caractere in texte_chiffre:
        if caractere.islower(): #On vérifie si le caractère est une lettre minuscule
            #Pour trouver la position du caractère dans l'alphabet avec 26 caractère (indexées 0-25)
            #La fonction ord() renvoie la veleur ASCII du caractère
            #On soustrait la valeur ASCII par la valeur 'a' pour obtenir le nombre représentant l'index du caractère dans l'alphabet
            position_caractere = ord(caractere) - ord('a')
            #Pour déchiffre, on soustrait la clé à la position du caractère dans l'alphabet (avec l'opérateur modulo pour rester dans la plage de lettres)
            #On reconvertit le résultat en caractère ASCII minuscule
            nouveau_caractere = chr((position_caractere + cle) % 26 + ord('a'))
            #On ajoute le caractère déchiffré à la chaine texte_clair
            #Le processus est itéré pour chaque caractère présent dans le texte chiffré afin d'appliquer le déchiffrement à l'ensemble du texte selon la clé spécifiée 
            texte_clair += nouveau_caractere
        else:
            #Si le caractère n'est pas une lettre minuscule on le garde tel quel
            texte_clair += caractere
    return texte_clair

#On utilise le module argparse
import argparse

def encrypt(texte,cle):
    texte_chiffre= "" #On initialise la variable texte_chiffre comme une chaîne de caractère vide afin de stocker le texte chiffré

    #On implémente l'algorithme de chiffrement de César

    return texte_chiffre

#On vérifie si le fichier Python est exécuté directement en tant que programme principle
#Si c'est le cas, le code contenu dans ce bloc sera exécuté
if __name__ == "__main__":
    #On configure le parser pour qu'il puissent lire les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Chiffrement de texte")
    parser.add_argument("texte", help="Texte a chiffrer ou chemin vers fichier contenant du texte") #On spécifie le texte à chiffrer ou le chemin vers un fichier contenant du texte
    parser.add_argument("cle", type=int, help="Cle de dechiffrement") #On spécifie la clé

    #On récupère les arguments saisis par l'usager via la console de ligne de commande
    args = parser.parse_args()

    #On essaie d'ouvrir le fichier s'il s'agit d'un chemin
    try:
        with open(args.texte, 'r') as file: #On ouvre le fichier en mode lecture (read)
            texte = file.read()
    #S'il ne s'agit pas d'un fichier, on utilise directement le texte
    except FileNotFoundError:
        texte = args.texte

    #Pour appeler la fonction de chiffrement avec le texte et la clé
    texte_chiffre = encrypt(texte, args.cle)

    #Pour afficher le texte chiffré
    print("Texte chiffre:", texte_chiffre)

#On ajoute la fonction brute_force à notre script
def brute_force(texte_chiffre):
    resultats = {} #Début de la création du dictionnaire pour stocker les résultats
    #On itère sur toutes les clés possibles (0-25 pour le chiffrement)
    for cle in range(26):
        texte_clair = decrypt(texte_chiffre, cle) #On déchiffre avec la clé actuelle
        resultats[cle] = texte_clair #On va stocker du texte en clair dans le dictionnaire avec la clé qui y correspond
    return resultats #On retourne le dictionnaire avec les résultats

#On va déduire la valeur de la clé et le message en clair du message suivant:
#Message = “gpkyfe zj r kilcp nfeuviwlc crexlrxv”
#On va utiliser la fonction brute_force

texte_chiffre = "gpkyfe zj r kilcp nfeuviwlc crexlrxv"
resultats_brute_force = brute_force(texte_chiffre) #On appelle la fonction brute_force avec le message intercepté

#On affiche les résultats pour la clé et le texte déchiffré
for cle, texte_clair in resultats_brute_force.items():
    print(f"Cle: {cle}, Texte dechiffre: {texte_clair}")