import random

class Agent:
    def __init__(self):
        def program(percept): abstract

        self.program = program


loc_A, loc_B, loc_C, loc_D = 'A', 'B', 'C', 'D'


class reflexVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

        action = ' '

        def program(percept):
            location = percept[0]
            status = percept[1]
            if status == 'Dirty':
                action = 'Suck'
            elif location == loc_A:
                action = 'Right'
            elif location == loc_B:
                action = 'Down'
            elif location == loc_D:
                action = 'Left'
            elif location == loc_C:
                action = 'Up'

            percept = (location, status)
            print('Agent perceives %s and does %s' % (percept, action))
            return action

        self.program = program


class vaccumEnvironment():
    def __init__(self):
        self.status = {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty']),
                       loc_C: random.choice(['Clean', 'Dirty']),
                       loc_D: random.choice(['Clean', 'Dirty'])
                       }

    def add_object(self, object, location=None):
        object.location = location or self.default_location(object)

    def default_location(self, object):
        return random.choice([loc_A, loc_B, loc_D, loc_C])

    def percept(self, agent):
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        if action == 'Right':
            agent.location = loc_B
        elif action == 'Down':
            agent.location = loc_D
        elif action == 'Left':
            agent.location = loc_C
        elif action == 'Suck':
            # if self.status[agent.location]=='Dirty'
            self.status[agent.location] = 'Clean'


Ragent = reflexVaccumAgent()
env = vaccumEnvironment()
env.add_object(Ragent)

for steps in range(5):
    print(env.percept(Ragent))
    action = Ragent.program(env.percept(Ragent))
    env.execute_action(Ragent, action)
