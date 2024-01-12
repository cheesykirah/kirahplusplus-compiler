### KIRAH++ COMPILER
# Version 3.0
# Benötigt: Python 3 oder so





### SCHREIBE HIER DEINEN CODE
kirah_code = """
hören sie mich aus
INT. COMPUTER
Anmerkung: Hier ist eine einfache Hello World Umsetzung.
text = "Hallo Welt"
sag mal bitte uwu text please
please lgbtq rights
another day another victory for the og
"""



### Kirah++ Features
# ifn't
# booln't
# LGBTQ+ freundlich
# Verbesserter Syntax
# Basiert auf Python 3





### Alles hierrunter ist der Compiler, bitte ignorieren.
#
#
#
#
#
#
#
#
#
#

def check_syntax(lines):
    # Check syntax
    if lines[0].strip() != "hören sie mich aus":
        raise SyntaxError("ERROR: Syntax Error. Du hast dein Statement nicht richtig begonnen")
    if lines[1].strip() != "INT. COMPUTER":
        raise SyntaxError("ERROR: Syntax Fehler. Es ist unklar wo der Code ausgeführt werden soll.")
    if lines[-1].strip() != "another day another victory for the og":
        raise SyntaxError("ERROR: Syntax Error. Du hast dein Statement nicht richtig beendet")
    if "lgbtq rights" not in " ".join(lines):
        raise SyntaxError("ERROR: Achtung, du wirst auf Twitter gecancelt weil du dich nicht für LGBTQ+ Rechte einsetzt.")
    for i, line in enumerate(lines):
        if i % 5 == 4 and "please" not in line:
            raise SyntaxError("ERROR: Der PC hat keine Lust. Frag vielleicht netter.")
    # Check if Python was used instead of Kirah++ TODO: BROKEN - idk why - chatgpt cant fix
    #python_keywords = ["print", "if not", "if", "not bool", "import ", "def ", "int ", "float ", "string ", "for", "break"]
    #for line in lines:
    #    if any(keyword in line for keyword in python_keywords):
    #        # More refined check to ignore Kirah++ specific syntax
    #        kirah_keywords = ["sag mal bitte uwu ", "wandere ", "methode ", "integer 2: jetzt erst recht!", "buchstabenkette", "if'nt", "na wenn das so ist", "booln't"]
    #        if not any(kirah_keyword in line for kirah_keyword in kirah_keywords):
    #            raise SyntaxError("ERROR: Syntax Fehler. Stelle sicher in Kirah++ zu schreiben und nicht in Python.")
    #        else:
    #            # If it's a Kirah++ specific line, skip the Python keyword check
    #            continue

def translate_line(line):
    # Replace Kirah++ with Python
    if "sag mal bitte uwu " in line:
        message_start_index = line.find("sag mal bitte uwu ") + len("sag mal bitte uwu ")
        message = line[message_start_index:]
        if message.startswith('"') and message.endswith('"'):
            # Es ist ein Literal
            line = 'print(' + message + ')'
        else:
            # Es ist eine Variable
            line = 'print(' + message + ')'
    else:
        line = line.replace("wandere ", "import ")
        line = line.replace(" ein mit deckname ", " as ")
        line = line.replace("methode ", "def ")
        line = line.replace("integer 2: jetzt erst recht!", "float")
        line = line.replace("integer", "int")
        line = line.replace("buchstabenkette", "string")
        line = line.replace("if'nt", "if not")
        line = line.replace("na wenn das so ist", "if")
        line = line.replace("booln't", "not bool")
        line = line.replace("Anmerkung: ", "# ")
        line = line.replace("Wiederholungsschleife:", "for")
        line = line.replace("SCHLUSS JETZT!", "break")
        line = line.replace("in der Reihe", "in range")
        line = line.replace("forn't", "for not")
    # Check if Negativity appears
    if "-" in line:
        raise SyntaxError("ERROR: Bewahre ein #positivemindset!")
    # Remove Kirah++ to not confuse Python
    line = line.replace("hören sie mich aus", "")
    line = line.replace("INT. COMPUTER", "")
    line = line.replace("please", "")
    line = line.replace("lgbtq rights", "")
    line = line.replace("another day another victory for the og", "")
    return line

def kirah_plus_plus_compiler(code):
    # Compile and Execute Code
    lines = code.strip().split("\n")
    check_syntax(lines)
    python_code = "\n".join(translate_line(line) for line in lines)
    exec(python_code)

# Start Compilation
kirah_plus_plus_compiler(kirah_code)
