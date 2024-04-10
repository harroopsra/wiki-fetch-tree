#Find 5 articles that link to the original article
#Add them to the tree
import requests
from urllib.parse import quote, unquote
from arbitrarytree import *

links = [] #For debugging, not used anymore

def find_articles(givenTitle, root, depth = 3, n_links = 2): #skips the first one

    if root == None:
        return None

    #if (givenTitle.startswith("{")):
    #    givenTitle = cleanbrackets(givenTitle)

    givenTitle = quote(givenTitle)

    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&list=&meta=&titles={givenTitle}&formatversion=2&pllimit={n_links}")
    data = response.json()
    print(f"Entered the function for this {givenTitle}. The data currently shown is", data["query"])
    links = data["query"]["pages"][0]["links"]

    #print("\nEntered for ",givenTitle)
    #print("----------------")
    
    for link in links:
        this_depth = depth
        title=link["title"]
        
        #Remove the weird ones. Also remove the year pages i.e. the ones that start with digits which keep leading to other year-related pages
        if (title.startswith("/") or title[0].isdigit()):
            continue

        #List containing all the links - this was for debugging
        #links.append(title)

        print(title)
        nodeTitle = "{" + unquote(givenTitle) + ": " + title + "}"


        #Depth check
        if (this_depth > 1):
            this_depth -= 1

            #Tree
            child = newNode(nodeTitle)
            #print("Child: ", child)
            #print("Child data: ", child.data)
            (root.children).append(child)
            #print("Children: ",root.children)
            newroot = root.children[-1] #latest appended
            find_articles(title, root = newroot, depth = this_depth)
        else:
            #Tree
            #print(f"This root is {root.data}", end = "\n\n")
            (root.children).append(newNode(nodeTitle))
        
    return root

def main():
    original_parent_title = "Art"
    root = newNode(original_parent_title)
    root = find_articles(original_parent_title, root=root)

    print("Level Order Traversal\n")
    print(LevelOrderTraversal(root))
    
    
if __name__ == "__main__":
    main()
