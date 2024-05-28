# Evidence: 2 Generating and Cleaning a Restricted Context-Free Grammar
Jesús Alejandro Cedillo Zertuche A01705442

## Description
The language that I chose is the Elven language (also called Quenya) which according to Wikipedia (2024) "is a constructed language, one of those devised by J. R. R. Tolkien for the Elves in his Middle-earth fiction." Tolkien based the language on Finnish, Latin, and Old English. Tolkien has written several synchronic grammars of Quenya, but only one has been fully published in full, which is called The Early Qenya Grammar. 

The language has existed since the books but recently gained popularity because of the movies that have been released. 

### Language structure
The Elven language is complicated, where the nouns can be declined in up to 10 cases. But to reduce the scope of the grammar, what is going to be analyzed is the numbers that nouns use. Most common languages have fairly simple grammar, for example, English, where in most words you just put and s and that's the plural of the word. The difference is that Elven has 3 different types of plurals:

1. General plural
2. Partitive Plural
3. Dual

The General plural is the one that all languages have. For example _lasse_ means leaf, and for this plural, it changes to _lassi_ which means leaves. 
The Partitive plural is one of the main differences. Here the word _lasse_ turns into _lasseli_ which means **some/several/a number of leaves**. 

Like Strack (2024) mentions saying _Eldar matir massa_ means **Elves eat bread**. Here you would be implying that all elves eat bread, but this is not the case, so although it is grammatically correct, it is better to say _Eldali matir massa_ which means **Some elves eat bread**. 

The Dual form will not be analyzed in this text, but to give context it refers to exactly two entities of something. An example is _hendu_ which means two eyes. This will not be analyzed since the grammatical rules vary a bit more than the other two plurals. 

Another important thing to mention is that Quenya does not have indefinite articles and only has one article which is **i**. This does not change for number or case.

### Plural rules
To better understand how to form the two different types of plural, here the basic rules will be given for each. 

1. General plural.
   
    a. When a word ends with a vowel (a, i, o, u, ië) the plural is formed by adding an **r** at the end. For example, _Elda_ turns to _Eldar_.
   
    b. When a word ends with a consonant, the plural is formed by adding an **i** at the end of the word. For example _atar_ turns to _atari_.
   
    c. When a word ends with e or ë, the plural is formed by adding an **i** at the end but removing the e in the process. For example _lasse_ turns into _lassi_.
   
2. Partitive Plural:
    Here the plural is formed by just adding **li** at the end of the word. For example _lasse_ turns into _lasseli_.

## Models
The model that will be used is a grammar which can create and validate the plurals that are created in a sentence. But before generating the grammar, here are the words with the translations that will be used: 

### Nouns
* `lasse:` leaf
* `alda:` tree
* `Elda:` Elf
* `massa:` bread
* `anto:` mouth
* `galad:` light
* `calma:` lamp
* `ered:` mountain
* `fin:` hair
* `parma:` book
* `taur:` forest
* `elen:` stars
* `aurë:` day
* `aran:` king
* `macil:` sword

### Verbs
* `martir:` to eat
* `hosta:` to gather
* `savin:` to exist
* `síla:` to shine
* `harya:` to have

## Grammar
To give some context, Geeks For Geeks (2023) mentions that in a compiler Design, there exist several phases. The first is the lexical analysis, which can be implemented using a DFA. But since this is not the focus of the evidence, I will focus on the next phase which is also called the syntax analysis (also known as parsing). What the parsing does, is check if the input follows the grammar that was assigned to the compiler. A lot of different parsers exist, where some use top-down, and others bottom-up. Inside top-down, backtracking and no backtracking parsers exist. The one I will implement is the LL(1), which has no backtracking and no recursive descent, also making it the simplest to implement. 

What LL parsing does is generate the tree by constructing it from the non-terminals. According to Moreno (2004), to get to an LL(1) parser several steps need to be taken. From an existing grammar, the first thing that needs to be done is to eliminate the ambiguity (meaning that two different trees can't exist for the same input). After doing this, left recursion also has to be eliminated, which means that the tree can only grow from the left (not the right). After successfully doing these two steps, we will have an LL(1) parser. 

## Grammar that recognizes the language
Here is the grammar of the language, with the verbs and nouns that I chose, and the grammar dictating how the plurals are formed. 
```python
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
```
The explanation of the grammar is the following: 
1. `S -> NS VS NS | NS VS:` A sentence has a noun part, a verb, and a noun again, or only a noun and a verb.
2. `NS -> Vo | E | C:` A noun can either end with a vowel that is not e, it can end with e, or end with a consonant.
3. `Vo -> VoR VoE:` A vowel noun has a vowel root word, and the vowel ending (which includes the singular and the plurals).
4. `E -> ER EE:` An E noun has an E root word, and the E ending (which includes the singular and the plurals).
5. `C -> CR CE:` A consonant noun has a consonant root word, and the consonant ending (which includes the singular and the plurals).
6. `VoR -> 'elda' | 'massa' | 'alda' | 'parma' | 'calma':` Words which are vowel nouns.
7. `ER -> 'lass' | 'aur':` Words which are e words. 
8. `CR -> 'atar' | 'galad' | 'ered' | 'fin' | 'taur' | 'elen' | 'aran' | 'macil':` Words which are consonant nouns.
9. `VoE -> 'r' | PP | Empty:` The ending of a vowel noun which is -r for plural, the ending of the Partitive plural, or singular. 
10. `EE -> 'i' | 'e'PP | 'e' | 'ë':` The ending of an e noun which is -i for plural, the ending of the Partitive plural, or singular (add an e to the end since the singular ends in e). 
11. `CE -> 'i' | PP | Empty:` The ending of a consonant noun which is -i for plural the ending of the Partitive plural, or singular.
12. `Empty ->:` If the word is singular then it ends empty without adding anything. 
13. `PP -> 'li':` The ending of the Partitive plural, which is always -li.
14. `VS -> 'martir' | 'harya' | 'hosta' | 'savin' | 'síla':` Verbs in Elven language that are used with the nouns.

After checking the grammar, this grammar is ready to be an LL(1) parser since it has no ambiguity. There is no way to get two different trees for the same input. It can't also grow infinitely to the left, so there is no left recursion. Because of this, no extra steps need to be taken to clean the grammar and get it ready to be an LL(1) parser. 

## Implementation
To test this grammar, a simple Python program was made, where the program asks for input (a sentence) or runs automatized tests and generates the tree if valid. If the grammar does not accept the sentence, it prints that the sentence is not valid. Here are some sentences or tests that can be run on the program: 

### Correct Sentences
1. `Eldar martir massa`: All elves eat bread.
2. `Eldali martir massa`: Some elves eat bread.
3. `Aldar harya lassi`: Trees have leaves.
4. `Aldar harya lasseli`: Trees have some leaves.
5. `Aldali harya lasseli`: Some trees have some leaves.
6. `Eredli harya aldar`: Some mountains have trees.
7. `Aranli harya macili`: Some kings have swords.
8. `Elenli síla`: Some stars shine.
9. `Eldali hosta lassi`: Some elves gather leaves.
10. `Eldali hosta parmar`: Some elves gather books.
11. `Calmar síla`: Lamps shine.

### Incorrect Sentences
1. `Aldai harya lassi`: Trees have leaves.
2. `Aldar harya lassli`: Trees have some leaves.
3. `Eldali martir massai`: Some elves eat bread.
4. `Eredli harya aldai`: Some mountains have trees.
5. `Aranli hara macili`: Some kings have swords.

### Running the program
To run the code just type `python elven_grammar.py`. Two options can be taken. The first is to run the above tests, to compare if the program yields the correct results. The second is to try to write your sentence based on the vocabulary and grammar rules, to see if the plurals used are accurate. 

It is important to mention that the grammar will accept other sentences that don't make that much sense because the grammar is checking mostly the plurals, not the verb conjugation or if the sentence makes sense. So more sentences can be created, and the tree will be generated if the plurals are correct. You are welcome to test these words, as they should work too. 

### Correct sentences Trees
Here are some trees of the sentences above, which is the program's output. 

<img width="551" alt="Screenshot 2024-04-28 at 21 09 00" src="https://github.com/Jesus0204/ElvenGrammar/assets/65917649/8c73e857-32a9-4d26-ba14-e77ee27c21b7">
<br>

<img width="296" alt="Screenshot 2024-04-28 at 21 10 37" src="https://github.com/Jesus0204/ElvenGrammar/assets/65917649/9bf99fea-54ac-48c4-b9ec-0e062b73782a">
<img width="284" alt="Screenshot 2024-04-28 at 21 11 13" src="https://github.com/Jesus0204/ElvenGrammar/assets/65917649/40d59c7d-9534-40e8-9ec7-03835ecf28a2">
<img width="282" alt="Screenshot 2024-04-28 at 21 12 33" src="https://github.com/Jesus0204/ElvenGrammar/assets/65917649/68797070-de55-4006-8bc0-ce88aa7d0a7f">
<img width="170" alt="Screenshot 2024-04-28 at 21 13 34" src="https://github.com/Jesus0204/ElvenGrammar/assets/65917649/ff41b70a-b9b0-4f0f-952e-cf8d4516dcfe">

## Analysis
### Asymptotic Analysis
First of all, the important thing to mention is that even though a word is _Eldar_ for example, in the grammar I had to separate it with the root of the word and the ending. Because of this, I have a for loop, that checks the user input and replaces the word that the user put (_Eldar_) to _Elda r_, so the grammar can detect it as correct. This is a process that iterates over each of the words to change it, so it becomes O(n). Additionally, I have a for loop that iterates over each sentence (when running the automatized tests) and a nested loop that prints each tree. Yet, since this is an LL(1) parser and there is no ambiguity, only one tree can be generated with the grammar, so this loop is O(1). The other two loops are not nested, so it remains O(n), the best solution possible.  

### Type of Grammar
Now regarding the Chomsky Hierarchy Extended Level, the grammar that I created is a Context-Free Grammar. First of all, this is because all of the left sides are variables and not terminals (thus not making it a Context-Sensitive Grammar or any level higher than that), but the right side has both variables and terminals. It is also important to mention that it is not Regular grammar since Regular Grammar has the right side consisting of a single terminal or a terminal followed by a non-terminal. The grammar that was designed has more than one variable on the right side, thus it is also not on a lower level. Because of these reasons, it is defined as a Context-Free Grammar. 

### Other Methods
Now as for a different solution, another language could be used such as Javascript and a library called Nearly or TreeGrammar. Yet the Natural Language Toolkit is a very simple way to parse the grammar, so this was the option that was selected for ease of use. 

## References
GeeksForGeeks (19 April, 2023). Introduction to Syntax Analysis in Compiler Design https://www.geeksforgeeks.org/introduction-to-syntax-analysis-in-compiler-design/.

Moreno, M. (December 2, 2004) Elimination of ambiguity. https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node7.html

Moreno, M. (December 2, 2004) Elimination of left recursion https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

LOTR Fandom. (n.d.). Elvish word list. https://lotr.fandom.com/wiki/Elvish_word_list

Princeton (n.d.). LL(1) Parser Visualization. https://www.cs.princeton.edu/courses/archive/spring20/cos320/LL1/

Strack, P. (March 17, 2024). Eldamo - An Elvish Lexicon. https://eldamo.org/index.html

Tolkien Gateway. (n.d). Quenya/Grammar. https://tolkiengateway.net/wiki/Quenya/Grammar

Wikipedia. (January 19, 2024). Quenya. https://en.wikipedia.org/wiki/Quenya

