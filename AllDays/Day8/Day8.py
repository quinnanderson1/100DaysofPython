# The goal of this project is to create a caesar cipher program

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
restart = "y"


def caesar(text, shift, direction):
    if direction == "encode":
        encodeText = ""
        for letter in text:
            if letter not in alphabet:
                encodeText += letter
                continue
            indexNum = (int(alphabet.index(letter)) + shift) % 26
            encodeText += alphabet[indexNum]
        print(encodeText)
    elif direction == "decode":
        decodeText = ""
        for letter in text:
            if letter not in alphabet:
                decodeText += letter
                continue
            indexNum = (int(alphabet.index(letter)) - shift) % 26
            decodeText += alphabet[indexNum]
        print(decodeText)


while restart == "y":
    direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower())
    while direction != "encode" and direction != "decode":
        print("Invalid option. Please type encode or decode.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = str(input("Type your message: ").lower())

    try:
        shift = int(input("Type the shift number: "))
    except:
        print("Invalid integer. Please try again.")
        shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)
    restart = input("Would you like to do another? (Y/N) ").lower()

    while restart != "y" and restart != "n":
        print("Invalid option. Please type Y or N.")
        restart = input("Would you like to do another? (Y/N) ").lower()

if restart == "n":
    print()
    print("Thanks for coding with us!")
