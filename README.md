# wiki-fetch-tree

This project finds the top n links for a given Wikipedia page 'Title' and recursively builds a general tree of adjustable depth d by finding the next n links for each link found. It then prints out the tree.  


The idea is to build little graphs to see relationships between different topics.  

  
Depth is currently set to 3, n_links are set to 2  
Currently this project ignores certain wikis if they start with a digit or start with a "/"  
Random is seeded at 1, we get max

### Examples
So what the tree looks like for a title like ['Cool'](https://en.wikipedia.org/wiki/Cool) is:
```
-Cool \
--{Cool: Bvndit} {Cool: CLIPS} 
---{Bvndit: All caps} {CLIPS: Attempto Controlled English} {CLIPS: Automated planning and scheduling} 
----{All caps: ASCII} {All caps: ASCII table} {Attempto Controlled English: Automated planning and scheduling} {Attempto Controlled English: Automated reasoning} {Automated planning and scheduling: AI boom} {Automated planning and scheduling: AI control problem} 
```

Or for something like ['Movie'](https://en.wikipedia.org/wiki/Movie), the output is:
```
-Movie 
--{Movie: Film} {Movie: Synonym} 
---{Synonym: -onym} {Synonym: Ancient Greek language} 
----{-onym: Abrahamic faiths} {-onym: Academic degree} {Ancient Greek language: Ancient Greek} {Ancient Greek language: Wikipedia:1}
```

Or for ['Art'](https://en.wikipedia.org/wiki/Art):
```
-Art \
--{Art: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} \
---{A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: A Vindication of Natural Society} {A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: Abhinavagupta} \
----{A Vindication of Natural Society: A Conflict of Visions} {A Vindication of Natural Society: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} {Abhinavagupta: A. C. Bhaktivedanta Swami Prabhupada} {Abhinavagupta: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} 
```

###Update  
Added a nicer print format so it's much less of a hassle to figure out the parents of each node. Also can print with more links:  
```
\-Cough
  |-K'aja – Aymara
  | |-Guides to browsing Wikipedia
  | | |-wikiversity:Special:Search/Guides to browsing Wikipedia
  | | \-Case sensitivity
  | \-Articles related to current events
  \-Hyperpnea
    |-Respiratory arrest
    | |-Hypercapnia
    | \-Stethoscope
    \-Shortness of breath
      |-Heart failure
      \-Nefes darlığı – Turkish
```
[Desperado (film)]()
```
\-Desperado (film)
  |-Chicano rock
  | |-Mexicans in Kansas
  | |-Merengue music
  | \-Argentine cumbia
  |-Quentin Tarantino
  | |-Bertrand Tavernier
  | |-All-American Girl (TV series)
  | \-Curdled (film)
  \-Tito & Tarantula
    |-Salma Hayek
    \-Stoner rock
```
French film [Incendies](https://en.wikipedia.org/wiki/Incendies)  
```
\-Incendies
  |-C.R.A.Z.Y.
  | |-Bedouin
  | |-Inconvenient Indian
  | \-Canadian Screen Award for Best Sound Editing
  |-Shoplifters (film)
  | |-I, Daniel Blake
  | |-National Board of Review Awards 2018
  | \-Guldbagge Awards
  \-Template talk:Canadian submission for Academy Awards
    \-Portal:Canada
```
### Comments
~~Project to mess around quickly with BeautifulSoup and build cool relationships.~~\
But I ended up using the MediaWiki Web service API and abandoning BeautifulSoup. I replaced the BeautifulSoup with the MediaWiki API because I think Wikipedia flagged my IP and would mostly send me results with recommendations to log in\
~~Also would be good to find a prettier way to print out the tree. Rn, it prints out by depth and you can see who the parent is by looking at the key in the key-value pair~~  \
  Replaced the previous print with a prettier print function so now relationships are clearer to trace
