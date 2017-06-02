
import json
import random
random.seed(20)

event_1 = '{"type": 1, "tickets": [10, 15, 15]}'
event_2 = '{"type": 2, "tickets": [20, 25, 20]}'
event_3 = '{"type": 3, "tickets": [30, 35, 25]}'
event_4 = '{"type": 1, "tickets": [40, 15, 20]}'
event_5 = '{"type": 2, "tickets": [50, 25, 10]}'
event_6 = '{"type": 3, "tickets": [60, 35, 40]}'

EVENT_TRANSCRIPT = """\
x-x-x-x-x-x-x-x-x-x
x-{0}-x-x-x-x-x-x-x-x
x-x-x-{1}-x-x-x-x-x-x
x-x-x-x-x-x-x-x-x-x
x-x-x-x-x-x-x-x-x-x
x-x-x-x-x-{2}-x-x-x-x
x-{3}-x-x-x-x-x-x-x-x
x-x-x-x-{4}-x-x-x-x-x
x-x-x-x-x-x-{5}-x-x-x
x-x-x-x-x-x-x-x-x-x""".format(event_1, event_2, event_3, event_4, event_5, event_6)


class EventMap(object):
    """ detail
    """

    x_values = 21
    y_values = 21
    x_min = -10
    y_min = -10

    event_min = 5
    event_max = 10

    ticket_min = 0
    ticket_max = 10

    price_min = 1000
    price_max = 10000


    grid = []

    def __init__(self, transcript):
        """ detail
        """
        grid_line = [None] * ((self.x_values))
        #create grid
        for i in range(self.y_min, self.y_min+self.y_values):
            self.grid.append(list(grid_line))

        #no of events
        events_exist = random.randint(self.event_min, self.event_max)
        for i in range(0, events_exist+1):
            x = random.randint(0, self.x_values)
            y = random.randint(0, self.y_values)
            print 'x <-' + str(x)
            print 'y <-' + str(y)

            while self.grid[y][x] != None:
                x = random.randint(0, self.x_values)
                y = random.randint(0, self.y_values)

            self.grid[y][x] = self.random_event()

    def print_grid(self):
        """
        Prints the grid in a nice format
        """
        print str(self.x_min) + " " + str(self.x_values - self.x_min)

        axis = range(self.x_min, self.x_min + self.x_values)
        axis = [str(x) for x in axis]
        print '\t' + '\t'.join(axis)

        for i, line in enumerate(self.grid):
            nice_line = [axis[i]]
            for event in line:
                if event is None:
                    nice_line.append('x')
                else:
                    nice_event = "("+ str(event['type'])+","+str(len(event['tickets']))+")"
                    nice_line.append(nice_event)
            print '\t'.join(nice_line)

    def random_event(self):
        """
        Returns dictionary of an event of random type and with a random list of tickets
        """
        event = {}
        event['type'] = random.randint(1, 3)
        tickets = []
        ticket_exist = random.randint(self.ticket_min, self.ticket_max)
        for i in range(0, ticket_exist):
            price = random.randint(self.price_min, self.price_max)
            tickets.append(price)
        event['tickets'] = tickets
        return event

    def get_event_obj(self, x, y):
        """
        Returns event object at coordinates
        """
        return self.grid[y][x]

    def get_event_type(self, x, y):
        """
        Returns event type at coordinates
        """
        return self.grid[y][x]['type']

    def get_event_tickets(self, x, y):
        """
        Returns event tickets at coordinates
        """
        return self.grid[y][x]['tickets']

    def get_event_tickets_sorted(self, x, y):
        #to sort
        """
        Returns event tickets sorted at coordinates
        """
        return self.grid[y][x]['tickets']

    def is_event(self, x, y):
        """
        Returns event tickets at coordinates
        """
        if self.grid[y][x] == None:
            return False
        else:
            return True


def find_nearest_three():

    return [1,2,3]


if __name__ == '__main__':
    """
    """
    eventmap = EventMap(EVENT_TRANSCRIPT)
    eventmap.print_grid()

    print find_nearest_three()


