Author @ Marcel Riederer                Date @ 4th June 2017

Viagogo Intern/Graduate Developer Test
Written in Python

--------------------------------------------------------------------------------------------------------------------------------

To Run in Terminal:

    python viagogo.py

Running the script will create a random grid. The script can use a seed by uncommenting: 

    #random.seed(20)  # uncomment to stop randomising

from line 12.


Commands once running:

    map         view randomly generated map (id, tickets available)
    event x,y	view event and tickets at coordinate x and y
    find x,y	find nearest events from coordinate x and y
    help		show commands
    exit		terminate program


My Assumptions:

	An event can only have a maximum of 50 tickets.
	A Ticket can only cost between $1 and $100.
	There are only 25 to 50 events at any given time.

These assumptions have been met in the code but can be changed to allow more events, more tickets and more expensive tickets.

--------------------------------------------------------------------------------------------------------------------------------

How might you change your program if you needed to support multiple events at the same location?

If there were multiple events at the same location, I could hold a list of events at each point in the grid. These could be accessed when examining each node, each of these events would have the same distance.
Although there may be multiple events at a given location because they are scheduled for different days. If this is the case than an extra axis could be used to signify days, this could be a constraint when searching or can be part of the search if the user wishes to search using nearest date and nearest location. 


Larger World Size:

If the world was much larger I would implement an Iterative Deepening Search, which functions like Depth First Search (DFS) but only searches to a limited depth. This is because of the exponential space complexity that Breadth First Search O(b^d) has, whereas DFS only has a linear complexity O(bd). Iterating the depth of DFS ensures that the nearest events are found first unlike regular DFS. 
In this scenario Iterative Deepening Search can be envisioned as a radar that only searches to a distance of 1, on each full cycle it increases its strength by an extra 1. Doing so we can be sure to find the nearest objects first by not looking too far ahead at the start. 

--------------------------------------------------------------------------------------------------------------------------------

Example Program Run:

    $ python viagogo.py

    Command     Description
    map         view randomly generated map
    event x,y   view event and tickets at coordinate
    find x,y    find nearest events from coordinate
    help        show commands
    exit        terminate program

    > find 1,2
    Event 39 - $34.78, Distance 3
    Event 30 - $14.88, Distance 4
    Event 7 - No Tickets, Distance 4
    Event 40 - $5.75, Distance 5
    Event 13 - $6.42, Distance 5

    > find 12,3
    
    > find -5,4
    Event 17 - $1.75, Distance 0
    Event 26 - $6.29, Distance 1
    Event 11 - $11.86, Distance 2
    Event 19 - $2.41, Distance 3
    Event 14 - $3.96, Distance 3
