# wiki-fetch-tree
\
This project finds the top n links for a given Wikipedia page 'Title' and recursively builds a general tree of adjustable depth d by finding the next n links for each link found. It then prints out the tree.
\
\
Depth is currently set to 3, n_links are set to 2 (because it prints out a nicer tree and it gets quite ugly with anything more)\
Currently this project ignores certain wikis if they start with a digit or start with a "/"\
\
\
\


### Examples
So what the tree looks like for a title like ['Cool'](https://en.wikipedia.org/wiki/Cool) is:\
-Cool \
--{Cool: Bvndit} {Cool: CLIPS} \
---{Bvndit: All caps} {CLIPS: Attempto Controlled English} {CLIPS: Automated planning and scheduling} \
----{All caps: ASCII} {All caps: ASCII table} {Attempto Controlled English: Automated planning and scheduling} {Attempto Controlled English: Automated reasoning} {Automated planning and scheduling: AI boom} {Automated planning and scheduling: AI control problem} 
\
\
Or for something like ['Movie'](https://en.wikipedia.org/wiki/Movie), the output is:\
-Movie \
--{Movie: Film} {Movie: Synonym} \
---{Synonym: -onym} {Synonym: Ancient Greek language} \
----{-onym: Abrahamic faiths} {-onym: Academic degree} {Ancient Greek language: Ancient Greek} {Ancient Greek language: Wikipedia:1} 
\
\
Or for ['Art'](https://en.wikipedia.org/wiki/Art):\
-Art \
--{Art: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} \
---{A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: A Vindication of Natural Society} {A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: Abhinavagupta} \
----{A Vindication of Natural Society: A Conflict of Visions} {A Vindication of Natural Society: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} {Abhinavagupta: A. C. Bhaktivedanta Swami Prabhupada} {Abhinavagupta: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} 

### Comments
Started out as a project to mess around quickly with BeautifulSoup. \
Ended up using the MediaWiki Web service API because of someone on stack overflow and abandoning BeautifulSoup but it's worth coming back to, and I might replace the current API with the BeautifulSoup after all. \
Also would be good to find a prettier way to print out the tree. Rn, it prints out by depth and you can see who the parent is by looking at the key in the key-value pair
