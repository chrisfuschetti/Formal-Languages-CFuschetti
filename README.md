# Formal-Languages-CFuschetti

Important note:

This program uses Graphviz, while the python project does contain the library your computer will also need it.

you can find information on installing here: https://graphviz.gitlab.io/download/

for windows you will need to put something like this "C:\Program Files (x86)\Graphviz2.38\bin" in your system's path variable 
if you search on windows 10 to edit environmental variables and then click on the path variable under "system variables" you can add a new path like the example above

There are a lot of tutorials on this regardless of platform, python will even tell you graphviz could not find its path if that is the issue


Next I would like to link to various online resources I used when learning many of these concepts

First off I used jetbrains PyCharm which is really great at telling you if you are off syntax or naming convention 

I used a a technique of converting regex into postfix form then to an NFA through Thompson's construction, finally after using subset construction I ran the results through Graphviz to produce the nfa and dfa.
This was acomplished with the help of these resources:

https://news.ycombinator.com/item?id=3202313
https://github.com/osandov/pylex/blob/master/pylex.py
https://xysun.github.io/posts/regex-parsing-thompsons-algorithm.html
https://cs.stackexchange.com/questions/76488/thompsons-construction-transforming-a-regular-expression-into-an-equivalent-nf
https://swtch.com/~rsc/regexp/regexp1.html
https://codereview.stackexchange.com/questions/116974/infix-to-postfix-implementation-using-a-stack
https://www.youtube.com/watch?v=NI0Bpm9HcL4
https://www.ics.uci.edu/~eppstein/PADS/Automata.py

There where others including many stackoverflow pages, but those are the main helpful sources 

To run:

run the Grephy.py  with the regex first using | * () thena after a space the file to be tested is stated, the default being input.txt

the -n and -d options can be followed by names for the nfa and dfa output pdfs, they defualt to nfa and dfa if this is not specified

