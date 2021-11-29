import string, random

print("Erstellt bei ZANDER FISCH. \n")

alle_zeichen = []

sonder = ["^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",",";",   ":",  "-", "_", "{", "}", "[", "]", "~"]

i = 1

n = int(input("Wieviele Passwörter sollen generiert werden? "))

lenght = 0

l = int(input("Wie lang sollen die Passwörter sein? "))

f = input("Wie soll der Dateiname für die Passwörter sein? ")

p = input("Welche Zeichen sollen verwendet werden? \n 1 = Buchstaben \n 2 = Zahlen \n 3 = Sonderzeichen \n 4 = Zahlen + Buchstaben \n 5 = Buchstaben + Sonderzeichen \n 6 = Zahlen + Sonderzeichen \n 7 = Alles \n")

if p == "1":
    alle_zeichen.extend(string.ascii_letters)

if p == "2":
    alle_zeichen.extend(string.digits)
    
if p == "3":
    alle_zeichen.extend(sonder)

if p == "4":
    alle_zeichen.extend(string.ascii_letters)
    alle_zeichen.extend(string.digits)

if p == "5":
    alle_zeichen.extend(string.ascii_letters)
    alle_zeichen.extend(sonder)

if p == "6":
    alle_zeichen.extend(string.digits)
    alle_zeichen.extend(sonder)

if p == "7":
    alle_zeichen.extend(string.ascii_letters)
    alle_zeichen.extend(string.digits)
    alle_zeichen.extend(sonder)

v = input("Sollen die Passwörter angezeigt werden[j/N]? ")

while i <= n:
    i = i + 1
    lenght += 1
    print(round(lenght/n*100,2), "%", end='\r')
    def erstelle_passwort():
        wort = ''.join(random.choice(alle_zeichen) for i in range(l))
        return wort
    
    def main():
        wort = erstelle_passwort()
        text = (wort + "\n")    
        with open(f + ".txt",'a+') as pw_datei:
            pw_datei.write(text + "\n")
            pw_datei.close()
        if v == "j":
            print((wort) + "\n")
    
    main() 
    
print("Passwörter in",(f + ".txt") + " gespeichert.")