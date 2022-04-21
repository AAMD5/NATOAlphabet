"""You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet). 
Input: 
If, you can read? 
Output: 
India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ? """

NATO = {"A": "Alpha",
        "B": "Beta",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
        ",": ",",
        "?": "?",
        "!": "!",
        }


def phon(string):

    words = []
    for letter in string:
        if letter == " ":
            continue
        words.append(NATO[letter.upper()])
        
    Sentence = ' '.join(words)
    
    return Sentence

#print(phon(String)) if you want to test the code above

def NATOsentence(filename):
    file = open(filename, "r")
    String = file.read()
    print(String)
    file.close()
    
    file = open(filename, "w")
    file.write(str(phon(String)))
    file.close()
    
    file = open(filename, "r")
    String = file.read()
    print(String)
    file.close()
    
NATOsentence("NATO Alphabet.txt")