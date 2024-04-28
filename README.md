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

Another important thing to mention is that Quenya does not have indefinite articles and only has one article which is **i**. This does not change for number, or case.

### Plural rules
To better understand how to form the two different types of plural, here the basic rules will be given for each. 

1. General plural.
   
    a. When a word ends with a vowel (a, i, o, u, ië) the plural is formed by adding an **r** at the end. For example, _Elda_ turns to _Eldar_.
   
    b. When a word ends with a consonant, the plural is formed by adding an **i** at the end of the word. For example _atar_ turns to _atari_.
   
    c. When a word ends with e or ë, the plural is formed by adding an **i** at the end but removing the e in the process. For example _lasse_ turns into _lassi_.
   
2. Partitive Plural:
    Here the plural is formed by just adding **li** at the end of the word. For example _lasse_ turns into _lasseli_.

## Models
The model that will be used is a grammar which can create and validate the plurals that are created in a sentence. But before generating the grammar, here are thw words with the translations that will be used: 

### Nouns
* `lasse:` leaf
* `alda:` tree
* `Elda:` Elf
* `massa:` bread
* `anto` mouth
* `galad` light
* `calma` lamp
* `ered` mountain
* `fin` hair
* `Parma` book
* `taur`forest
* `elen` stars
* `aurë` day
* `aran` king
* `macil` sword

### Verbs
* `martir` to eat
* `hosta` to gather
* `savin` to exist
* `síla` to shine
* `harya` to have

## Grammar
To give some context, Geeks For Geeks (2023) mentions that in a compiler Design, there exist several phases. The first is the lexical analysis, which can be implemented using a DFA. But since this is not the focus of the evidence, I will focus on the next phase which is also called the syntax analysis (also known as parsing). What the parsing does, is check if the input follows the grammar that was assigned to the compiler. A lot of different parsers exist, where some use top-down, and others bottom-up. Inside top-down, backtracking and no backtracking parsers exist. The one I will implement is the LL(1), which has no backtracking and no recursive descent, also making it the simplest to implement. 

What LL parsing does is generate the tree by constructing it from the non-terminals. According to Moreno (2004), to get to an LL(1) parser several steps need to be taken. From an existing grammar, the first thing that needs to be done is to eliminate the ambiguity (meaning that two different trees can't exist for the same input). And after doing this, left recursing also has to be eliminated, which means that the tree can only grow from the left (and not the right). After successfully doing these two steps, we will have an LL(1) parser. 

## References
GeeksForGeeks (19 April, 2023). Introduction to Syntax Analysis in Compiler Design https://www.geeksforgeeks.org/introduction-to-syntax-analysis-in-compiler-design/.

Moreno, M. (December 2, 2004) Elimination of ambiguity. https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node7.html

Moreno, M. (December 2, 2004) Elimination of left recursion https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

LOTR Fandom. (n.d.). Elvish word list. https://lotr.fandom.com/wiki/Elvish_word_list

Princeton (n.d.). LL(1) Parser Visualization. https://www.cs.princeton.edu/courses/archive/spring20/cos320/LL1/

Strack, P. (March 17, 2024). Eldamo - An Elvish Lexicon. https://eldamo.org/index.html

Tolkien Gateway. (n.d). Quenya/Grammar. https://tolkiengateway.net/wiki/Quenya/Grammar

Wikipedia. (January 19, 2024). Quenya. https://en.wikipedia.org/wiki/Quenya

