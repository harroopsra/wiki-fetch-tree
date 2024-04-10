class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

def newNode(data):
    temp = Node(data)
    return temp

def LevelOrderTraversal(root):

    if (root == None):
        return
    
    #Standard level order traversal using queue
    #Create a queue
    q = []
    q.append(root)

    count = 1
    while(len(q)!= 0):

        n = len(q)

        #If this node has children
        s = "-"
        s*= count
        count+=1
        print(s,end="")
        while n>0:
            #Dequeue an item and print it
            p = q[0]
            q.pop(0)
            print(p.data, end = " ")

            #Enqueue all the children of the dequeued item
            for i in range(len(p.children)):
                q.append(p.children[i])
            
            n -= 1
        print()

    