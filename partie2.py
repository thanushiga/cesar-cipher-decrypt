#On va utiliser la classe Counter de la bibliothèque collections pour compter les occurences
#On va utiliser la méthode most.common() pour trier les occurences
from collections import Counter

#On va créer la fonction frq_txt 
def frq_txt(texte):
    #On utilise la classe Counter pour compter les occurences de chaque caractère
    occurrences = Counter(texte)
    
    #On va trier les caractères par fréquence d'occurence (du plus fréquent au moins fréquent)
    sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True) #On covertie l'objet Counter en une liste de tuples items() 
    #On utilise la fonction lambda pour trier le tuple par nombre d'occurrences (x[1]) dans l'ordre décroissant (reverse==True)
    
    #On renvoit une liste de tuples caractère/fréquence
    return sorted_occurrences

#On teste notre fonction sur le contenu du fichier "english_sample.txt"
#On lit le contenu du fichier "english_sample.txt"
#On s'assure que le fichier est dans le même répertoire que notre code python ou on doit préciser le chemin vers le fichier
with open("english_sample.txt") as file:
          texte = file.read()
result = frq_txt(texte)
print(result)

### Voici le résultat lorsqu'on teste notre fonction sur le contenu du fichier "english_sample.txt"
# [(' ', 84), ('e', 64), ('t', 45), ('n', 43), ('i', 41), ('r', 40), ('a', 34), ('o', 32), ('l', 28), ('s', 27), ('h', 26), ('d', 19), ('c', 18), ('g', 15), ('u', 13), ('y', 10), ('m', 8), ('b', 7), ('v', 7), ('p', 6), ('f', 6), (',', 6), ('.', 4), ('\n', 3), ('E', 2), ('x', 2), ('k', 2), ('q', 2), ('w', 2), ('-', 2), ('F', 1), ('T', 1), ('W', 1), ('j', 1)]

#On va utiliser la classe Counter de la bibliothèque collections
#On va utiliser la méthode most.common() pour retourner une liste de tuples contenant chaque octet et son nombre d'occurrences (ordre décroissant)
from collections import Counter

def frq_cpr(byte_sequence): #La fonction frq_cpr prend comme paramètre "byte_sequence" (séquence d'octets)
    occurrences = Counter(byte_sequence) #On compte les occurrences des séquences d'octets
    sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True) #On convertit l'objet Counter en liste de tuples
    #On trie la liste de tuples avec occurrences.items()
    #On utilise key=lambda x: x[1] pour indiquer à sorted() de trier le tuple en utilisant le second élément de chaque tuple comme clé de tri.
    #x[1] représente le nombre d'occurrences de chaque octet
    #On trie en ordre décroissant avec reverse=True
    
    #On renvoit une liste de tuples en ordre décroissant
    return sorted_occurrences

#On teste la fonction sur le fichier "cipher_sample.bin" qui a été placé dans le même répertoire que ce code
#On utilise "rb" pour s'assurer que la lecture du fichier se fasse en mode "lecture" (read) et binaire
with open("cipher_sample.bin", "rb") as file:
    byte_sequence = file.read()
    
result = frq_cpr(byte_sequence)
print(result)

### Voici le résultat lorsqu'on test la fonction frq_cpr sur le fichier "cipher_sample.bin"
# [(155, 84), (1, 64), (253, 45), (49, 43), (9, 41), (92, 40), (243, 34), (208, 32), (74, 28), (122, 27), (154, 26), (143, 19), (193, 18), (72, 15), (22, 13), (25, 10), (62, 8), (103, 7), (110, 7), (211, 6), (57, 6), (215, 6), (36, 4), (31, 3), (196, 2), (94, 2), (56, 2), (84, 2), (108, 2), (127, 2), (227, 1), (176, 1), (99, 1), (13, 1)]

#Pour identifier des correspondances entre les deux textes, on relie les caractères les plus fréquents du texte en clair aux symboles les plus fréquents du texte chiffré.
#La comparaison des fréquences permet d'inférer les relations probables entre les caractères du texte en clair et leurs équivalents chiffrés.
#Ceci permet donc d'interpréter le texte chiffré.
#On peut voir dans ce cas qu'il y a une relation entre l'espace (' ') qui est le caractère le plus fréquent dans le texte en clair et la séquence d'octets 155 du texte chiffré puisqu'ils apparaissent le même nombre de fois dans les deux textes (84 fois).
#On peut faire la même corrélation pour le "e" dans le texte en clair et la séquence d'octe '1', qui apparaissent tous deux 64 fois.

#On va créer une fonction build_dec_key qui va recouvrir la clé de déchiffrage partielle
def build_dec_key(encryption_key): 
    #Pour chaque paire clé/valeur dans la clé de chiffrement, on va inverser la relation en faisant des valeurs (en octets) les clés et des clés (caractères chiffrés) les valeurs
    decryption_key = {value: key for key, value in encryption_key.items()}
    return decryption_key

#On va d'abord construire une clé de déchiffrement partielle à partir des résultats des questions 7-8.
#On va associer les caractères les plus fréquents du texte en clair avec les octets correspondants du texte chiffré.
#Voici les réponses des tests des questions 7-8 en format de listes de tuples
frq_txt_result = [
    (' ', 84), ('e', 64), ('t', 45), ('n', 43), ('i', 41), ('r', 40), ('a', 34), ('o', 32), ('l', 28), ('s', 27), ('h', 26),
    ('d', 19), ('c', 18), ('g', 15), ('u', 13), ('y', 10), ('m', 8), ('b', 7), ('v', 7), ('p', 6), ('f', 6), (',', 6),
    ('.', 4), ('\n', 3), ('E', 2), ('x', 2), ('k', 2), ('q', 2), ('w', 2), ('-', 2), ('F', 1), ('T', 1), ('W', 1), ('j', 1)
]

frq_cpr_result = [
    (155, 84), (1, 64), (253, 45), (49, 43), (9, 41), (92, 40), (243, 34), (208, 32), (74, 28), (122, 27), (154, 26),
    (143, 19), (193, 18), (72, 15), (22, 13), (25, 10), (62, 8), (103, 7), (110, 7), (211, 6), (57, 6), (215, 6), (36, 4),
    (31, 3), (196, 2), (94, 2), (56, 2), (84, 2), (108, 2), (127, 2), (227, 1), (176, 1), (99, 1), (13, 1)
]

#On va créer la clé de déchiffrement partielle en faisant l'association des caractères les plus fréquents
decrypt_key_partial = {}
#On va corréler les caractères les plus fréquents des deux textes à chaque itération
for i in range(len(frq_txt_result)):
    char_frq = frq_txt_result[i]
    byte_sequence_frq = frq_cpr_result[i]
    #On associe l'octet au caractère correspondant dans la clé de déchiffrement partielle
    decrypt_key_partial[byte_sequence_frq[0]] = char_frq[0]
print(decrypt_key_partial)

### Voici le résultat, soit la clé de déchiffrement partielle:
#{155: ' ', 1: 'e', 253: 't', 49: 'n', 9: 'i', 92: 'r', 243: 'a', 208: 'o', 74: 'l', 122: 's', 154: 'h', 143: 'd', 193: 'c', 72: 'g', 22: 'u', 25: 'y', 62: 'm', 103: 'b', 110: 'v', 211: 'p', 57: 'f', 215: ',', 36: '.', 31: '\n', 196: 'E', 94: 'x', 56: 'k', 84: 'q', 108: 'w', 127: '-', 227: 'F', 176: 'T', 99: 'W', 13: 'j'}

#On va ensuite créer la fonction guess_txt qui va prendre comme entrées le texte chiffré et une clé de déchiffrement partielle basée sur les occurrences des caractères du texte en anglais
#encrypted_txt est le texte chiffré qu'on doit déchiffrer

def guess_txt(encrypted_txt, decrypt_key_partial):
    decrypted_txt = '' #On initialise une chaîne de caractère vide pour stocker le text déchiffré
    count = 0 #On initialise un compteur pour suivre le nombre de caractères déchiffrés
    for byte in encrypted_txt: #On parcourt chaque caractère du texte
        if byte in decrypt_key_partial: #On vérifie si le caractère est présent dans la clé de déchiffrement partielle
            decrypted_txt += decrypt_key_partial[byte] #Si le caractère est présent, on utilise la clé pour déchiffré le caractère
            count += 1 #On incrémente le compteur de caractères déchiffrés
            #On vérifie si 17 caractères ont été déchiffré et on arrête la boucle si c'est le cas
            if count == 17:
                break 
        else:
            #Si le caractère n'est pas déchiffré on remplace par $
            decrypted_txt += '$'
    return decrypted_txt

#On va tester la fonction de la question 11 sur le fichier cipher_sample.bin
with open('cipher_sample.bin', 'rb') as file:
    encrypted_txt = file.read()
decrypted_result = guess_txt(encrypted_txt, decrypt_key_partial)
print(decrypted_result)

#En répondant au point précédent, on a pu trouver la clé de déchiffrement partielle suivante: Exploring the bre.
#En analysant le texte english_sample.txt on peut complété le mot "bre"  à "breathtaking". 
#Si on enlève la condition if count == 17 break de la fonction guess_txt, on peut retester la fonction et voir qu'il s'agit en fait du texte en clair english_sample.txt.
#On va retester les fonctions de la questions 11-12 sans la condition:
decrypt_key_partial = {}
for i in range(len(frq_txt_result)):
    char_frq = frq_txt_result[i]
    byte_sequence_frq = frq_cpr_result[i]
    decrypt_key_partial[byte_sequence_frq[0]] = char_frq[0]

def guess_txt(encrypted_txt, decrypt_key_partial):
    decrypted_txt = '' 
    count = 0 
    for byte in encrypted_txt:
        if byte in decrypt_key_partial: 
            decrypted_txt += decrypt_key_partial[byte] 
            count += 1 
        else:
            decrypted_txt += '$'
    return decrypted_txt
with open('cipher_sample.bin', 'rb') as file:
    encrypted_txt = file.read()
decrypted_result = guess_txt(encrypted_txt, decrypt_key_partial)
print(decrypted_result)

#La clé de déchiffrement est donc: 
# Exploring the breathtaking landscapes of the English countryside is truly a remarkable experience.
# From the rolling hills covered in vibrant green to the charming little villages nestled along meandering rivers, there is an undeniable sense of tranquility and beauty.
# The picturesque scenery, combined with the rich history and culture, creates a perfect blend of old-world charm and modern-day allure.
# Whether you choose to stroll through the enchanting gardens, visit historic castles, or indulge in traditional afternoon tea, there is something for everyone to enjoy in this captivating destination.

#On va refaire le test en utilisant la clé de déchiffrage sur le fichier "test.bin"
#On va lire le contenu du fichier "test.bin" en binaire
with open('test.bin', 'rb') as file:
    encrypted_txt = file.read()
#On applique notre clé de déchiffrement
decrypted_txt = '' #On va stocker le texte déchiffré dans cette variable
#On parcourt chaque octet du texte
for byte in encrypted_txt:
    #On vérifie si l'octet existe dans la clé de déchiffrement
    #Si oui, on ajoute au texte déchiffré la valeur qui correspont à l'octet dans la clé de déchiffrement
    if byte in decrypt_key_partial:
        decrypted_txt += decrypt_key_partial[byte]
    #Sinon on ajoute '$' si l'octet n'est pas trouvé
    else: decrypted_txt += '$'
print(decrypted_txt)

### Voici la sortie:
# $ello there$ $ hope you are having a wonderful day.
# $ wanted to take a moment to express my gratitude for your presence here.
# $t is truly a pleasure to assist you with any questions or tasks you may have.
# Whether it is providing information, helping you find solutions, or simply engaging in a friendly conversation, $$m here to make your experience enjoyable and stress-free.
# Feel free to reach out to me anytime, and $$ll be more than glad to lend a helping hand. Take care and have a fantastic day ahead$