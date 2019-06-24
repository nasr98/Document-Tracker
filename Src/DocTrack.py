import tkinter
from tkinter import *
from collections import Counter
import json
import matplotlib.pyplot as plt
import numpy as np
import pycountry_convert
from graphviz import Digraph

#import os
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
# 'C:/Users/nasr1/Desktop/issuu_cw2.json'

######################################################DEFINITIONS######################################################
# TASK 2A
def viewCountryH():
    FileName = FileEntry.get()
    DocumentID = FileEntry2.get()
    jsonDataList = []
    countryList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
                # jsonDataList.append(pd.read_json(i, typ='series')) #MUCH SLOWER
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["env_doc_id"]
                    if env == DocumentID:
                        visit = j["visitor_country"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            countryList.append(x)
                    else:
                        print("Document not found,please enter a valid document")
                        break


        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"

        y = np.array(countryList)
        plt.hist(y);
        plt.xlabel('Country')
        plt.ylabel('Occurence')
        plt.show()


# TASK 2B
def viewContinentH():
    FileName = FileEntry.get()
    DocumentID = FileEntry2.get()
    jsonDataList = []
    countryList = []
    continentList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["env_doc_id"]
                    if env == DocumentID:
                        visit = j["visitor_country"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            countryList.append(x)
                    else:
                        print("Document not found,please enter a valid document")
                        break
            for i in (countryList):
                continentList.append(pycountry_convert.country_alpha2_to_continent_code(i))
        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"

        y = np.array(continentList)
        plt.hist(y);
        plt.xlabel('Continent')
        plt.ylabel('Occurence')
        plt.show()

# TASK 3A
# *********************
def viewBrowserH():
    FileName = FileEntry.get()
    jsonDataList = []
    browserList = []
    occurrence = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                user = j["visitor_useragent"]
                if user in counter.keys():
                    counter[user] += 1
                else:
                    counter[user] = 1
            for x in counter:
                browserList.append(x)
                occurrence.append(counter[x])

        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"

        # y = np.array(browserList) #TOO BIG FOR ARRAY
        plt.bar(browserList, occurrence)
        plt.xlabel("Browser")
        plt.ylabel("Occurrences")
        plt.show()


# TASK 3B
def viewBrowserNameH():
    FileName = FileEntry.get()
    jsonDataList = []
    browserList = []
    browserListShort = []
    browserListShorter = []
    occurrence = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                user = j["visitor_useragent"]
                if user in counter.keys():
                    counter[user] += 1
                else:
                    counter[user] = 1
            for x in counter:
                browserList.append(x)
                occurrence.append(counter[x])
            for i in browserList:
                browserListShort.append(i.split("/"))
            for i in browserListShort:
                browserListShorter.append(i[0])

        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"

        plt.bar(browserListShorter, occurrence)
        plt.xlabel("Browser")
        plt.ylabel("Occurrences")
        plt.show()


# EXTRA
def viewBrowserNameDOCH():
    FileName = FileEntry.get()
    DocumentID = FileEntry2.get()
    jsonDataList = []
    browserList = []
    browserListShort = []
    browserListShorter = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["env_doc_id"]
                    if env == DocumentID:
                        user = j["visitor_useragent"]
                        if user in counter.keys():
                            counter[user] += 1
                        else:
                            counter[user] = 1
                        for x in counter:
                            browserList.append(x)
            for i in browserList:
                browserListShort.append(i.split("/"))
            for i in browserListShort:
                browserListShorter.append(i[0])

        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"

        y = np.array(browserListShorter)
        plt.hist(y);
        plt.xlabel('Browser')
        plt.ylabel('Occurence')
        plt.show()


# TASK 4A
def docID2visID():
    FileName = FileEntry.get()
    DocumentID = FileEntry2.get()
    jsonDataList = []
    visitIDList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["env_doc_id"]
                    if env == DocumentID:
                        visit = j["visitor_uuid"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            visitIDList.append(x)
                            print(list(set(visitIDList)))
                    else:
                        print("Document not found,please enter a valid document")
                        break
            return list(set(visitIDList))
        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"


# FOR ALSOLIKES
def docID2visIDF(DocID, FileName):
    jsonDataList = []
    visitIDList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["env_doc_id"]
                    if env == DocID:
                        visit = j["visitor_uuid"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            visitIDList.append(x)
            print(list(set(visitIDList)))
            return list(set(visitIDList))
        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"


# TASK 4B
def visID2docID():
    FileName = FileEntry.get()
    VisitorID = FileEntry3.get()
    jsonDataList = []
    docIDList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["visitor_uuid"]
                    if env == VisitorID:
                        visit = j["env_doc_id"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            docIDList.append(x)
                    else:
                        print("Visitor not found,please enter a valid visitor id")
                        break

            print(list(set(docIDList)))
            return list(set(docIDList))

        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"


# FOR ALSO LIKES
def visID2docIDF(VisID, FileName):
    jsonDataList = []
    docIDList = []
    counter = Counter()
    with open(FileName) as file_get:
        try:
            for i in file_get:
                jsonDataList.append(json.loads(i))
            for j in jsonDataList:
                if "env_doc_id" in j.keys():
                    env = j["visitor_uuid"]
                    if env == VisID:
                        visit = j["env_doc_id"]
                        if visit in counter.keys():
                            counter[visit] += 1
                        else:
                            counter[visit] = 1
                        for x in counter:
                            docIDList.append(x)
                            print(list(set(docIDList)))
            return list(set(docIDList))

        except TypeError:
            "TYPE ERROR"
        except KeyError:
            "KEY ERROR"


# TASK 4C
def alsoLikes(sorting_Func):
    DocumentID = FileEntry2.get()
    jsonDataList = []
    counter = Counter()
    FileName = FileEntry.get()
    with open(FileName) as file_get:
        for i in file_get:
            jsonDataList.append(json.loads(i))
            for visitor in docID2visIDF(DocumentID, FileName):
                for document in visID2docIDF(visitor, FileName):
                    if document != DocumentID:
                        if document in counter.keys():
                            counter[document] += 1
                        else:
                            counter[document] = 1
            break
        alsoIDList = [(v, k) for k, v in counter.items()]
        print("Readers also liked:")
        print(alsoIDList)
        return sorting_Func(alsoIDList)


# TASK 4D

def sortDown(L):
    return L.sort(key=lambda x: x[1])


def alsoLikeList():
    return alsoLikes(sortDown)


# TASK 5
def alsoLikeGraph():
    dot = Digraph(comment='The Round Table')
    dot.format = 'svg'
    FileName = FileEntry.get()
    DocumentID = FileEntry2.get()
    VisitorID = FileEntry3.get()
    jsonDataList = []
    with open(FileName) as file_get:
        for i in file_get:
            jsonDataList.append(json.loads(i))
        for visitor in docID2visIDF(DocumentID, FileName):
            if visitor == VisitorID:
                dot.attr('node', shape='rectangle', color='green', style="filled")
                dot.node(visitor[-4:])
                dot.attr('node', shape='circle', color='green', style="filled")
                dot.node(DocumentID[-4:])
                dot.edge(visitor[-4:], DocumentID[-4:])
            else:
                for document in visID2docIDF(visitor, FileName):
                    dot.attr('node', shape='rectangle', color='red', style="filled")
                    dot.node(visitor[-4:])
                    dot.attr('node', shape='circle', color='red', style="filled")
                    dot.node(document[-4:])
                    dot.edge(visitor[-4:], document[-4:])
        dot.render('graph.gv', view=True)


######################################################DEFINITIONS######################################################

##########################################################GUI##########################################################


gui = tkinter.Tk()
gui.title("Document Tracker")

InfoLabel = tkinter.Label(gui, text="Please enter the desired file directory")
FileEntry = tkinter.Entry(gui, bd=10)
InfoLabel2 = tkinter.Label(gui, text="Please enter the desired document UUID")
FileEntry2 = tkinter.Entry(gui, bd=10)
InfoLabel3 = tkinter.Label(gui, text="Please enter the desired visitor UUID")
FileEntry3 = tkinter.Entry(gui, bd=10)
viewCountryHH = tkinter.Button(gui, text="t2a: View Histogram of countries", command=viewCountryH)
viewContinentHH = tkinter.Button(gui, text="t2b: View Histogram of continents", command=viewContinentH)
viewBrowserHH = tkinter.Button(gui, text="t3a: View Histogram of user browsers", command=viewBrowserH)
viewBrowserNameHH = tkinter.Button(gui, text="t3b: View Histogram of user browsers name", command=viewBrowserNameH)
viewBrowserNameDOCHH = tkinter.Button(gui, text="View Histogram of user browsers for a doc",command=viewBrowserNameDOCH)
doc2visit = tkinter.Button(gui, text="t4a: View visitors of this document", command=docID2visID)
visit2doc = tkinter.Button(gui, text="t4b: View documents visited", command=visID2docID)
alsoLL = tkinter.Button(gui, text="t4c/d: Also liked descending list", command=alsoLikeList)
produceALD = tkinter.Button(gui, text="t5: Also liked Digraph", command=alsoLikeGraph)

InfoLabel.pack()
FileEntry.pack()
InfoLabel2.pack()
FileEntry2.pack()
InfoLabel3.pack()
FileEntry3.pack()
viewCountryHH.pack(side=TOP)
viewContinentHH.pack(side=TOP)
viewBrowserHH.pack(side=TOP)
viewBrowserNameHH.pack(side=TOP)
doc2visit.pack(side=TOP)
visit2doc.pack(side=TOP)
alsoLL.pack(side=TOP)
produceALD.pack(side=TOP)
viewBrowserNameDOCHH.pack(side=TOP)
gui.mainloop()

##########################################################GUI##########################################################
