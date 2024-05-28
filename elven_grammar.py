import nltk
from nltk import CFG

# The grammar to create different sentences and plurals is created
elven_grammar = CFG.fromstring("""
    S -> NS VS NS | NS VS
    NS -> Vo | E | C
    Vo -> VoR VoE
    E -> ER EE
    C -> CR CE
    VoR -> 'elda' | 'massa' | 'alda' | 'parma' | 'calma'
    ER -> 'lass' | 'aur'
    CR -> 'atar' | 'galad' | 'ered' | 'fin' | 'taur' | 'elen' | 'aran' | 'macil'
    VoE -> 'r' | PP | Empty
    EE -> 'i' | 'e' PP | 'e' | 'ë'
    CE -> 'i' | PP | Empty
    Empty ->
    PP -> 'li'
    VS -> 'martir' | 'harya' | 'hosta' | 'savin' | 'síla'
""")

# Create a parser with the defined grammar
elven_parser = nltk.ChartParser(elven_grammar)

# Define a custom tokenizer for Na'vi language
def separate(sentence):
    sentence = sentence.lower()

    # Since the grammar has the endings separate from the words,
    # they need to be separated so the tree gan be generated correctly
    endings = {
        'eldar': 'elda r',
        'eldali': 'elda li',
        'lasseli': 'lass e li',
        'lasse': 'lass e',
        'lassi': 'lass i',
        'aurë': 'aur ë',
        'auri': 'aur i',
        'aureli': 'aur e li',
        'aldar': 'alda r',
        'aldali': 'alda li',
        'eredi': 'ered i',
        'eredli': 'ered li',
        'eleni': 'elen i',
        'elenli': 'elen li',
        'macili': 'macil i',
        'macilli': 'macil li',
        'massar': 'massa r',
        'massali': 'massa li',
        'antor': 'anto r',
        'antoli': 'anto li',
        'galadi': 'galad i',
        'galadli': 'galad li',
        'calmar': 'calma r',
        'calmali': 'calma li',
        'fini': 'fin i',
        'finli': 'fin li',
        'parmar': 'parma r',
        'parmali': 'parma li',
        'tauri': 'taur i',
        'taurli': 'taur li',
        'arani': 'aran i',
        'aranli': 'aran li',
    }

    for originalWord, newEnding in endings.items():
        sentence = sentence.replace(originalWord, newEnding)
    return sentence.split()

sentences = [
    "Eldar martir massa",
    "Eldali martir massa", 
    "Aldar harya lassli",
    "Aldar harya lassi", 
    "Aldar harya lasseli", 
    "Aldali harya lasseli", 
    "Aldai harya lassi", 
    "Eredli harya aldar", 
    "Eredli harya aldai", 
    "Eldali martir massai", 
    "Aranli harya macili", 
    "Aranli hara macili",
    "Elenli síla", 
    "Eldali hosta lassi", 
    "Eldali hosta parmar", 
    "Calmar síla", 
]

print("------------")
print("Welcome to the elven Grammar Tree!")
print("------------")
print("In this program you can run automatized tests, or input your own sentence.")
print("------------")
print("To run an automatized test please type 1. To input your own sentence type 2.")
print("------------")

while True:
        try:
            decision = int(input("Choose your option: "))
        except ValueError:
            print("\nPlease write a number :)")
            continue
        if decision <= 0 or decision >= 3:
            print("\nPlease type 1 o 2.\n")
            continue
        else:
            break

if decision == 1:
  for sentence in sentences:
    try:
      # Separate and parse each sentence using the custom tokenizer
      separated_sentence = separate(sentence)
      for tree in elven_parser.parse(separated_sentence):
        # Since I made the grammar unambiguous only one tree is printed.
        print("\nThe sentence " + "\033[1m" + sentence + "\033[0m" + " has the following tree: ")
        tree.pretty_print()
        print()
    except:
      print("The sentence " + "\033[1m" + sentence + "\033[0m" + " is not correct. \n" +
            "One or both of the words has an incorrect plural, so the tree can't be printed for this sentence. \n")
elif decision == 2:
  sentence = input("Please write the sentence to be generated: ")
  try:
    # Separate and parse each sentence using the custom tokenizer
    separated_sentence = separate(sentence)
    for tree in elven_parser.parse(separated_sentence):
      print("\nThe sentence " + "\033[1m" + sentence + "\033[0m" + " has the following tree: ")
      tree.pretty_print()
      print()
  except:
      print("\nThe sentence " + "\033[1m" + sentence + "\033[0m" + " is not correct. \n" +
            "One or both of the words has an incorrect plural, so the tree can't be printed for this sentence. \n")
