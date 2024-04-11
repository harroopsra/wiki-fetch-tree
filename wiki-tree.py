#Find 5 articles that link to the original article
#Add them to the tree
import requests
from urllib.parse import quote, unquote
from arbitrarytree import *
from bs4 import BeautifulSoup
import random
import time

##GLOBAL
random.seed(1)

def find_articles(givenTitle, root, depth = 2, n_links = 3): #skips the first one

    if root == None:
        return None
    
    #time.sleep(1) #Wikipedia keeps catching me making requests

    givenTitle = quote(givenTitle)

    #Using Wikimedia API instead of Beautiful Soup. 
    #The problem is that the API gives data pre-sorted and then imposes a limit on 
    #how many links you can access. So it's entirely possible you get fairly nonsense links instead of useful ones
    #I.e. JK Rowling might link to internal wikipedia useful links like "Categories:People born in the UK" instead of something more meaningful 
    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&list=&meta=&titles={givenTitle}&formatversion=2&pllimit=max")
    data = response.json()
    #print(f"Entered the function for this {givenTitle}. The data currently shown is", data["query"])
    links = data["query"]["pages"][0]["links"]
    #response = requests.get(f"https://en.wikipedia.org/wiki/{givenTitle}")

    #soup = BeautifulSoup(response.content, "html.parser")
    #links = soup.findAll("a")
    

    #links = links[5:20]
    links = random.sample(links,n_links)

    print(f"Entered the function for this {givenTitle}. The data currently shown is under links")

    print("\nEntered for ",givenTitle)
    #print("----------------")
    
    for link in links:
        this_depth = depth
        title=link["title"]

        #time.sleep(1) #to evade the wikipedia ip flagging
        #title = link.get('title')

        #There's only so many conditions because I think wikipedia detected I was using beautiful soup
        if title == None or title.startswith("ISBN") or title.lower().startswith("special") or title.lower().startswith("categor") or title.lower().startswith("you are") or title.lower().startswith("how to contact") or title.lower().startswith("search wikipedia") or title.lower().startswith("support us")or title.lower().startswith("add images") or title.lower().startswith("learn how to edit"):
            continue
        
        #Remove the weird ones. Also remove the year pages which keep leading to other years
        #if (title.startswith("/") or title[0].isdigit()):
        #    continue

        #List containing all the links - this was for debugging
        #links.append(title)

        print(title)
        #nodeTitle = "{" + unquote(givenTitle) + ": " + title + "}"


        #Depth check
        if (this_depth > 1):
            this_depth -= 1

            #Tree
            #child = newNode(nodeTitle)
            child = newNode(title)
            #print("Child: ", child)
            #print("Child data: ", child.data)
            (root.children).append(child)
            #print("Children: ",root.children)
            newroot = root.children[-1] #latest appended
            find_articles(title, root = newroot, depth = this_depth)
        else:
            #Tree
            #print(f"This root is {root.data}", end = "\n\n")
            #(root.children).append(newNode(nodeTitle))
            (root.children).append(newNode(title))
    
    return root

def main():

    original_parent_title = "Incendies"
    root = newNode(original_parent_title)
    root = find_articles(original_parent_title, root=root)

    print(root)

    #print("Level Order Traversal\n")
    #print(LevelOrderTraversal(root))

    if root == None:
        print ("IP blocked or no links found")
    else:
        print("\n\nNicer prettier print")
        print(root.printPretty("", True))
    
    
if __name__ == "__main__":
    main()
