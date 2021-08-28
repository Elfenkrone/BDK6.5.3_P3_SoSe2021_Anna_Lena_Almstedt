import csv
import datetime
from os import close

"""
ANMERKUNG: Ich habe die Datenbanken der IMDb auf meinem PC gespeichert. Hochladen in meinen Git-Hub konnte ich die Datenbanken NICHT, da sie zu groß sind. Die Datenabanken müssen 
also selbst nochmal installiert werden. Anders lies es sich leider nicht lösen.

Fragestellung 1: Welcher Schauspieler hat bei den meisten Filmen/Serienepisoden mitgespielt? 
Dafür habe ich im ersten Schritt alle Schauspieler aus der name.basics Datenbank extrahiert. 
Im zweiten Schritt wurde von allen extrahierten Schauspielern die Filme und Serienepisoden, in denen sie mitgespielt haben, in der title.principals Datenbank zusammengezählt.
Dabei habe ich darauf geachtet, dass Filme nicht doppelt gezählt wurden. Jede FilmID wurde nur einaml gezählt, indem die FilmID in einer Liste zwischengespeichert 
und mit der aktuellen Zeile verglichen wurde. Alle Ergebnisse habe ich mir dann durch return count zurück geben lassen.
"""
def actor_film_ratio(): 
    count = {}
    with open("Aufgabe 2/Datenbank/name.basics.tsv/data.tsv", encoding="utf8") as f: 
        line = csv.reader(f,delimiter="\t") #in tsv Dateien werden Werte mit einem Tabulator(\t) separiert 
        for i,row in enumerate(line): 
            if i != 0:  #Erste Zeile in Datenbank enthält nur den Aufbau. Deshalb wird sie ignoriert
                jobs = row[4].split(",") #jobs werden in der Datenbank als String gespeichert und durch Kommata separiert 
                for job in jobs: 
                    if job == "actor":
                        count[row[0]] = [[], 0, row[1]]
    f.close()
    with open("Aufgabe 2/Datenbank/title.principals.tsv/data.tsv", encoding="utf8") as f: 
        line = csv.reader(f,delimiter="\t")
        for i,row in enumerate(line): 
            if row[3] == 'actor' and i != 0:
                if count.get(row[2]) is None: #Falls Personen noch nicht vorhanden, füge sie neu hinzu 
                    count[row[2]] = [[row[0]], 1, "unknown"]
                if row[0] not in count.get(row[2])[0]: #zähle Counter hoch und speicher FilmID 
                    tmp = count.get(row[2])
                    tmp[0].append(row[0])
                    tmp[1] += 1

    f.close()
    for i in count: 
        count[i] = count.get(i)[1:3] #entferne Liste von Filmen 
    return count
 
"""
Fragestellung 1: Welcher Schauspieler hat bei den meisten Filmen/Serienepisoden mitgespielt? 
Diese Funktion sucht den oder die Schauspieler die in den meisten Filmen/Serienepsioden mitgespielt haben. 
Gibt dessen ID, die Anzahl der Filme/Serienepsioden und den Namen zurück. 
Ruft dafür actor_film_ratio auf. 
"""
def max_actor():
    count = actor_film_ratio()
    maximum = []
    maximum.append(count.popitem()) #Füge beliebiges Element aus Count in maximum hinzu
    for i in count: 
        tmp = count.get(i)
        if tmp[0] > maximum [0][1][0]: #Falls neuer Counter größer ist
            maximum.clear()            #Leere die Liste 
            maximum.append((i, tmp))   #und füge die neuen Informationen ein (ID, Counter und Name)
        elif tmp[0] == maximum [0][1][0]:#andernfalls, falls Counter gleich hoch ist, 
            maximum.append((i,tmp))     #füge neue Informationen zusätzlich hinzu
    return maximum

"""
Fragestellung 2: Wie alt ist/sind der/die älteste/n eingetragene/n Producer in der IMDb? 
Die Funktion durchsucht die name.basics Datenbank und errechnet mit dem aktuellen Jahr und dem Geburtsjahr der Producer deren Alter und findet so letztendlich den oder die
ältesten Producer, die in der IMDb verzeichnet sind, heraus. Zurückgegeben wird am Ende das aktuelle Alter, die ID und der Name bzw. die Namen, falls es mehrere Producer gibt,
die im selben Jahr geboren wurden. 
"""
def age_producer(): 
    with open("Aufgabe 2/Datenbank/name.basics.tsv/data.tsv", encoding="utf8") as f:
         line = csv.reader(f,delimiter="\t")
         age = 0
         current_year = datetime.datetime.now().year
         producer_name = []
         for i,row in enumerate(line):
             if i != 0 and row[2] != "\\N":
                jobs = row[4].split(",")
                for job in jobs: 
                    if job == "producer":
                        if age < current_year - int (row[2]):
                            producer_name.clear()
                            producer_name.append((row[0], row[1]))
                            age = current_year - int (row[2])
                        elif age == current_year - int (row[2]):
                            producer_name.append((row[0], row[1]))
    f.close()   
    return age, producer_name

"""
Fragestellung 3: Welches ist das häfigste Filmgenre? In welchem Genre gibt es die meisten Filme? 
Die Funktion durchsucht die title.basics Datenbank und zählt von jedem Film das Genre. Am Ende wird wieder das Maximum ermittelt und zurückgegeben. Am Ende erhält man das
Genre, zu welchem es am meisten Filme gibt und die genaue Anzahl an Filmen zu diesem Genre. 
"""

def number_genre(): 
    with open("Aufgabe 2/Datenbank/title.basics.tsv/data.tsv", encoding="utf8") as f:
        line = csv.reader(f,delimiter="\t")
        count = {}
        for i,row in enumerate(line): 

            if row.__len__() < 9:
                    for k, j in enumerate(row):
                        t = str(j).split("\t")
                        if t.__len__() > 1:
                            x = k
                            for s in t:
                                row.insert(x, s)
                                x += 1
                                if j in row:
                                    row.remove(j)

            if i != 0 and row[8] != "\\N": 
                genres = row[8].split(",")
                for genre in genres:
                    if count.get(genre) is None: 
                        count[genre] = 1
                    else: 
                        count[genre] = count.get(genre) + 1
    f.close() 
    maximum = []
    maximum.append(count.popitem())
    for genre in count: 
        if maximum[0][1] == count.get(genre):
            maximum.append((genre, count.get(genre)))
        elif maximum[0][1] < count.get(genre):
            maximum.clear()
            maximum.append((genre, count.get(genre)))
    return maximum



if __name__=="__main__":
    print(max_actor())
    print(age_producer())
    print(number_genre())
 