# wiki-fetch-tree

Started out as a project to mess around quickly with BeautifulSoup
Ended up learning the MediaWiki Web service API and abandoning BeautifulSoup

This project finds the top n links for a given Wikipedia page 'Title' and recursively builds a general tree of adjustable depth d by finding the next n links for each link found. It then prints out the tree.

So what the tree looks like for a title like ['Cool'](https://en.wikipedia.org/wiki/Cool) is:
-Cool 
--{Cool: Bvndit} {Cool: CLIPS} 
---{Bvndit: All caps} {CLIPS: Attempto Controlled English} {CLIPS: Automated planning and scheduling} 
----{All caps: ASCII} {All caps: ASCII table} {Attempto Controlled English: Automated planning and scheduling} {Attempto Controlled English: Automated reasoning} {Automated planning and scheduling: AI boom} {Automated planning and scheduling: AI control problem} 

Or for something like ['Movie'](https://en.wikipedia.org/wiki/Movie), the output is:
-Movie 
--{Movie: Film} {Movie: Synonym} 
---{Synonym: -onym} {Synonym: Ancient Greek language} 
----{-onym: Abrahamic faiths} {-onym: Academic degree} {Ancient Greek language: Ancient Greek} {Ancient Greek language: Wikipedia:1} 

Or for ['Art'](https://en.wikipedia.org/wiki/Art)
-Art 
--{Art: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} 
---{A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: A Vindication of Natural Society} {A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful: Abhinavagupta} 
----{A Vindication of Natural Society: A Conflict of Visions} {A Vindication of Natural Society: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} {Abhinavagupta: A. C. Bhaktivedanta Swami Prabhupada} {Abhinavagupta: A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful} 

Interesting, I'd like to come back to it someday
