# Artificial Intelligence for Business
# Optimizing warehouse Flows with Q-Learning

# Importing the libraries
import numpy as np

# Setting the Parameters gamma and alpha for the Q-Learning
# the discount rate - future rewards are worth less than immediate rewards
gamma = 0.75
# how fast the ai learns
alpha = 0.9

# PART 1 - DEFINING THE ENVIRONMENT

# Defining the states
location_to_state = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11}

# Defining the actions
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# Defining the rewards
R = np.array([
    [0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0],
    [0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,1,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,1],
    [0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,0,1,0]])

# making a mapping from the states to the locations
state_to_location = {state: location for location, state in location_to_state.items()}

# making the final function that will return the optimal route
def route(starting_location, ending_location):
    
    R_new = np.copy(R)
    R_new[location_to_state[ending_location], location_to_state[ending_location]] = 1000

    Q = np.array(np.zeros([12,12]))
    for i in range(1000):
        # select random state from the 12 possible states
        current_state = np.random.randint(0,12)
        # random action that can lead to a possible state from 0 - 11
        playable_actions = []
        for j in range(12):
            if R_new[current_state, j] > 0:
                playable_actions.append(j)

        # reach the next state by playing the action
        next_state = np.random.choice(playable_actions)

        # compute the temporal difference
        TD = R_new[current_state, next_state] + gamma*Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]

        Q[current_state, next_state] = Q[current_state, next_state] + alpha*TD

    route = [starting_location]
    
    next_location = starting_location
    
    while(next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

# printing the final route
print('Route: ' + str(route('E', 'G')))
