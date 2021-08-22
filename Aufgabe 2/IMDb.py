import csv

def test():
    with open("Aufgabe 2/Datenbank/title.principals.tsv/data.tsv") as f: 
        line = csv.reader(f,delimiter="\t")
        for i,row in enumerate(line): 
            if i <= 100 :
                print(row)
                print(row[1])
            else: 
                break
        f.close()

def actor_film_ratio():
    count = {}
    with open("Aufgabe 2/Datenbank/name.basics.tsv/data.tsv", encoding="utf8") as f: 
        line = csv.reader(f,delimiter="\t")
        for i,row in enumerate(line): 
            if i != 0: 
                jobs = row[4]
                for job in jobs: 
                    if job == "actor":
                        count[row[0]] = [[], 0, row[1]]
    f.close()
    with open("Aufgabe 2/Datenbank/title.principals.tsv/data.tsv", encoding="utf8") as f: 
        line = csv.reader(f,delimiter="\t")
        for i,row in enumerate(line):
            if row[3] == 'actor' and i != 0:
                if count.get(row[2]) is None: 
                    count[row[2]] = [[row[0]], 1, "unknown"]
                if row[0] not in count.get(row[2])[0]:
                     #count[row[2]] = (count.get(row[2])[0].append(row[0]), count.get(row[2])[1] +1)
                    tmp = count.get(row[2])
                    tmp[0].append(row[0])
                    tmp[1] += 1

    f.close()
    for i in count: 
        count[i] = count.get(i)[1:3]
    return count

def max_actor():
    count = actor_film_ratio()
    maximum = []
    maximum.append(count.popitem())
    for i in count: 
        tmp = count.get(i)
        #print(tmp, "\n", maximum)
        if tmp[0] > maximum [0][1][0]:
            maximum.clear()
            maximum.append((i, tmp))
        elif tmp[0] == maximum [0][1][0]:
            maximum.append((i,tmp))
    return maximum


if __name__=="__main__": 
    #max_actor()
    print(max_actor())
    #test()
