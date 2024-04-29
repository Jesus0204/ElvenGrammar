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
    for word, replacement in endings.items():
        sentence = sentence.replace(word, replacement)
    return sentence.split()

sentence = input("Please write the sentence to be generated: ")

# Separate and parse each sentence using the custom tokenizer
separated_sentence = separate(sentence)
for tree in elven_parser.parse(separated_sentence):
  tree.pretty_print()
