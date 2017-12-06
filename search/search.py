# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sets

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    fronteir = util.Stack()
    fronteir.push((problem.getStartState(), [], 0))
    prev = []
    
    while not fronteir.isEmpty():

        nowState, history, nowCost = fronteir.pop()
        if problem.isGoalState(nowState):
            return history

        if not nowState in prev:
            prev.append(nowState)
            for state, direc, cost in problem.getSuccessors(nowState):
                fronteir.push( (state, history+[direc], cost+nowCost) )
    return []
     
def breadthFirstSearch(problem):
    fronteir = util.Queue()
    fronteir.push((problem.getStartState(), [], 0))
    prev = []
    
    while not fronteir.isEmpty():
        
        nowState, history, nowCost = fronteir.pop()
        if problem.isGoalState(nowState):
            return history

        if not nowState in prev:
            prev.append(nowState)
            for state, direc, cost in problem.getSuccessors(nowState):
                fronteir.push( (state, history+[direc], cost+nowCost) )
    return []

# def depthFirstSearch(problem):
#     return generalSearch(problem, util.Stack())
     
# def breadthFirstSearch(problem):
#     return generalSearch(problem, util.Queue())
    
# "Currently ony for DFS and BFS, needs a parameter for the way it is pushed to the stack"
# def generalSearch(problem, datastructure):
#     fronteir = datastructure
#     fronteir.push((problem.getStartState(), [], 0))
#     prev = [problem.getStartState()]
    
#     while not fronteir.isEmpty():
#         nowState, history, nowCost = fronteir.pop()
#         for state, direc, cost in problem.getSuccessors(nowState):
#             if problem.isGoalState(nowState):
#                 return history
#             prev.append(nowState)
#             if not state in prev:
#                 fronteir.push( (state, history+[direc], cost+nowCost) )
#     return []


def uniformCostSearch(problem):
    return aStarSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    # fronteir = util.PriorityQueue()
    # fronteir.push((problem.getStartState(), [], 0), 0)
    # prev = []
    
    # while not fronteir.isEmpty():
        
    #     nowState, history, nowCost = fronteir.pop()
    #     if problem.isGoalState(nowState):
    #         return history

    #     if not nowState in prev:
    #         prev.append(nowState)
    #         for state, direc, cost in problem.getSuccessors(nowState):
    #             fronteir.push((state, history+[direc], cost+nowCost), cost+nowCost + heuristic(state, problem))
    # return []
    fronteir = util.PriorityQueue()
    prev = sets.Set()   
    fronteir.push((problem.getStartState(), [], 0), 0)

    while not fronteir.isEmpty():
        nowState, history, currentCost = fronteir.pop()
        "Return if the goal state was reached"
        if problem.isGoalState(nowState):
            return history

        "Otherwise iterate through the succesors and push the unseen ones onto the fronteir"
        if(nowState not in prev):
            prev.add(nowState)
            for state, direc, cost in problem.getSuccessors(nowState):
                fronteir.push((state, history+[direc], cost+currentCost), cost+currentCost + heuristic(state, problem))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
