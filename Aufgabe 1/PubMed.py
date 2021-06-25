# import urllib.request, json 
# with urllib.request.urlopen("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=27708327") as url:
#     data = json.loads(url.read().decode())
#     print(data)
import pandas
IDs = [31452104, 31437182, 31455877, 31535994]
for element in IDs:
    data = pandas.read_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + str(element))
    print("Titel:", data["result"][str(element)]["title"], "\nPublikationsdatum:", data["result"][str(element)]["pubdate"], "\n")
    