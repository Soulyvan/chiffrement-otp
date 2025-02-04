import random
import string

# Fonction pour générer une clé aléatoire avec les lettres de l'alphabet (a-z)
def generate_key(message):
    key = ''.join(random.choice(string.ascii_lowercase) if char.isalpha() else char for char in message)
    return key

# Fonction pour chiffrer un message avec la clé
def encrypt(message, key):
    encrypted_message = []
    for m, k in zip(message, key):
        if m.isalpha():
            # Chiffrement par décalage de César uniquement pour les lettres
            encrypted_char = chr(((ord(m.lower()) - ord('a') + ord(k) - ord('a')) % 26) + ord('a'))
            # Si le caractère initial était en majuscule, on remet le chiffrement en majuscule
            if m.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_message.append(encrypted_char)
        else:
            # Si le caractère n'est pas une lettre, on le garde tel quel
            encrypted_message.append(m)
    return ''.join(encrypted_message)

# Fonction pour déchiffrer un message avec la clé
def decrypt(encrypted_message, key):
    decrypted_message = []
    for m, k in zip(encrypted_message, key):
        if m.isalpha():
            # Déchiffrement par inverse du décalage de César uniquement pour les lettres
            decrypted_char = chr(((ord(m.lower()) - ord('a') - (ord(k) - ord('a'))) % 26) + ord('a'))
            # Si le caractère initial était en majuscule, on remet le déchiffrement en majuscule
            if m.isupper():
                decrypted_char = decrypted_char.upper()
            decrypted_message.append(decrypted_char)
        else:
            # Si le caractère n'est pas une lettre, on le garde tel quel
            decrypted_message.append(m)
    return ''.join(decrypted_message)


# Demander à l'utilisateur d'entrer un message
message = input("Entrez un message à chiffrer: ")

# Générer la clé de la même longueur que le message (sans affecter les caractères non alphabétiques)
key = generate_key(message)
print(f"Clé générée : {key}")

# Chiffrer le message
encrypted_message = encrypt(message, key)
print(f"Message chiffré : {encrypted_message}")

# Déchiffrer le message
decrypted_message = decrypt(encrypted_message, key)
print(f"Message déchiffré : {decrypted_message}")

