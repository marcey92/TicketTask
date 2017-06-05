"""
Author @ Marcel Riederer                Date @ 4th June 2017
Viagogo Task:
    Breadth First Search on 21x21 grid.
    Random Event Placement and Ticket Pricing.
    Finds nearest 5 events and shows cheapest ticket price.
"""
import random
from ast import literal_eval as make_tuple
#random.seed(20)  # uncomment to stop randomising


class EventMap(object):
    """
    Holds grid for events and methods to access
    """
    # constraints for size of grid
    x_values = 21
    y_values = 21
    x_min = -10
    y_min = -10
    # constraints for no of events
    event_min = 25
    event_max = 50
    # constraints for no of tickets
    ticket_min = 0
    ticket_max = 10
    # constraints for ticket price in cents
    price_min = 100
    price_max = 10000

    def __init__(self):
        """
        Randomly creates events for grid
        """
        self.grid = []
        # initialize empty grid
        grid_line = [None] * ((self.x_values))
        for i in range(self.y_min, self.y_min + self.y_values):
            self.grid.append(list(grid_line))
        # add events to grid
        n_events = random.randint(self.event_min, self.event_max)
        for i in range(0, n_events):
            x = random.randint(0, self.x_values - 1)
            y = random.randint(0, self.y_values - 1)
            while self.grid[y][x] != None:  # if event exists get new coordinate
                x = random.randint(0, self.x_values - 1)
                y = random.randint(0, self.y_values - 1)
            self.grid[y][x] = self.__random_event(i + 1)

    def __random_event(self, idx):
        """
        Returns dictionary of an event with a random list of tickets
        """
        event = {}
        tickets = []
        n_tickets = random.randint(self.ticket_min, self.ticket_max)
        for i in range(0, n_tickets):
            price = random.randint(self.price_min, self.price_max)
            tickets.append(price)
        event['id'] = idx
        event['tickets'] = tickets
        return event

    def print_grid(self):
        """
        Prints the grid in nice format
        """
        axis = range(self.x_min, self.x_min + self.x_values)
        axis = [str(x) for x in axis]
        print '\t' + '\t'.join(axis)
        # reversed for graph like representation
        axis = list(reversed(axis))
        reversed_grid = list(reversed(self.grid))
        for i, row in enumerate(reversed_grid):
            nice_line = [axis[i]]
            for event in row:
                if event is None:
                    nice_line.append('x')
                else:
                    nice_event = "(" + str(event['id']) + \
                        "," + str(len(event['tickets'])) + ")"
                    nice_line.append(nice_event)
            print '\t'.join(nice_line)

    def __get_index(self, x, y):
        """
        Convertes coordinates to indexes for array
        """
        return (x - self.x_min), (y - self.y_min)

    def valid_coordinate(self, xy):
        x = xy[0]
        y = xy[1]
        if x < self.x_min or x >= (self.x_min + self.x_values):
            return False
        if y < self.y_min or y >= (self.y_min + self.y_values):
            return False
        return True

    def is_event(self, xy):
        x, y = self.__get_index(xy[0], xy[1])
        if self.grid[y][x] == None:
            return False
        else:
            return True

    def get_event(self, xy):
        x, y = self.__get_index(xy[0], xy[1])
        return self.grid[y][x]

    def get_tickets(self, xy):
        x, y = self.__get_index(xy[0], xy[1])
        return self.grid[y][x]['tickets']

    def get_id(self, xy):
        x, y = self.__get_index(xy[0], xy[1])
        return self.grid[y][x]['id']


def distance_between(a, b):
    """
    Manhatten distance between a(x,y) and b(x,y)
    """
    x_distance = abs(a[0] - b[0])
    y_distance = abs(a[1] - b[1])
    return x_distance + y_distance


def expand(coordinate):
    """
    Return North, South, East and West of Coordinate
    """
    x = coordinate[0]
    y = coordinate[1]
    neighbors = []
    neighbors.append((x + 1, y))
    neighbors.append((x - 1, y))
    neighbors.append((x, y + 1))
    neighbors.append((x, y - 1))
    return neighbors


def find_nearest(eventmap, start_node, n_events):
    """
    Finds nearest events using breadth first search.
    Does not visit seen coordinates
    Returns a list of tupples of event and coordinate found
    """
    nearest_events = []
    nodes = [start_node]
    visited_nodes = set()
    # until all nodes visited or until n_events found
    while len(nodes) > 0 and len(nearest_events) < n_events:
        front_node = nodes.pop()
        # if coordinate is valid and node not visited
        if eventmap.valid_coordinate(front_node) and not front_node in visited_nodes:
            visited_nodes.add(front_node)
            # if node is an event
            if eventmap.is_event(front_node):
                event = eventmap.get_event(front_node)
                nearest_events.append((event, front_node))
            # expand node
            nodes = expand(front_node) + nodes
    return nearest_events


def print_nice_event(nearest_events, user_coordinate):
    """
    Prints nice the nearest events with distance
    """
    for event in nearest_events:
        idx = event[0]['id']
        tickets = event[0]['tickets']
        event_coordinate = event[1]
        if len(tickets) == 0:
            price = 'No Tickets'
        else:
            price = sorted(tickets)[0]
            price = '$' + str(price)[:-2] + '.' + str(price)[-2:]
        distance = distance_between(event_coordinate, user_coordinate)
        print 'Event {0} - {1}, Distance {2}'.format(idx, price, distance)


def main():
    """
    Runs a loop for user to give commands
    """
    eventmap = EventMap()
    commands = """\
Command\tDescription
map\tview randomly generated map
event x,y\tview event and tickets at coordinate
find x,y\tfind nearest events from coordinate
help\tshow commands
exit\tterminate program"""

    print commands
    user_input = raw_input('> ')
    while user_input != 'exit':
        raw = user_input.split(' ')
        # print grid
        if raw[0] == 'map':
            eventmap.print_grid()
        # help commands
        elif raw[0] == 'help':
            print commands
        # show event at coordinate
        elif raw[0] == 'event':
            user_tupple = make_tuple(raw[1])
            if eventmap.is_event(user_tupple):
                idx = eventmap.get_id(user_tupple)
                tixs = eventmap.get_tickets(user_tupple)
                # add currency format to integers
                print 'id: {0} tickets: {1}'.format(idx, ['$' + str(t)[:-2] + '.' + str(t)[-2:] for t in tixs])
            else:
                print 'no event at ' + str(user_tupple)
        elif raw[0] == 'find':  # find nearest events
            user_tupple = make_tuple(raw[1])
            nearest_events = find_nearest(eventmap, user_tupple, 5)
            print_nice_event(nearest_events, user_tupple)
        user_input = raw_input('> ')
    # end input loop


if __name__ == '__main__':
    main()
