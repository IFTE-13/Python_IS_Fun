from Queue import Queue

graph = {
    "A": {"B": 9, "C": 4, "D": 7},
    "B": {"A": 9, "E": 7},
    "C": {"A": 4, "E": 17, "F": 12},
    "D": {"A": 7, "F": 14},
    "E": {"B": 11, "C": 17, "Z": 5},
    "F": {"C": 12, "D": 14, "Z": 9},
    "Z": {"E": 5, "F": 9}
}

heuristicSLD = {
    "A": 21,
    "B": 14,
    "C": 18,
    "D": 18,
    "E": 5,
    "F": 8,
    "Z": 0
}


class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state = graphProblem.result(self.state, action)
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]


def graph_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)

    explored = set()

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        print("Parent: ", node.state,
              "Childs: ", [child.state for child in node.expand(problem)])

        if problem.goal_test(node.state): return node
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.sortAppend(child, f)

    return None


def uniform_cost_search(problem):
    return graph_search(problem, lambda node: node.path_cost)


def GBFS(problem):
    return graph_search(problem, lambda node: heuristicSLD[node.state])

def A_star(problem):
    return graph_search(problem, lambda node: node.path_cost + heuristicSLD[node.state])


gp = graphProblem("A", "Z", graph)

print("=======================================")
print()
print("----------UCS State Space-------------")

goalNode = uniform_cost_search(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)

print("=======================================")
print()
print("----------GBFS State Space-------------")

goalNode = GBFS(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)

print("=======================================")
print()
print("----------A* State Space-------------")

goalNode = A_star(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)



