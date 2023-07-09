# Artificial Intelligence for Business - Case Study 2
# Building the Environment

# importing the libraries
import numpy as np

# BUILDING THE ENVIRONMENT IN A CLASS

class Environment(object):

    # INTRODUCING AND INITIALIZING ALL THE PARAMETERS AND VARIABLES OF THE ENVIRONMENT
    def __init__(self, optimal_temperature = (18.0, 24.0), initial_month=0, initial_number_users = 10, initial_rate_data = 60):
        self.monthly_atmospheric_temperatures = [1.0, 5.0, 7.0, 10.0, 11.0, 20.0, 23.0, 24.0, 22.0, 10.0, 5.0, 1.0]
        self.initial_month = initial_month
        self.atmospheric_temperature = self.monthly_atmospheric_temperatures[initial_month]
        self.optimal_temperature = optimal_temperature
        self.min_temperature = -20
        self.max_temperature = 80
        self.min_number_users = 10
        self.max_number_users = 100
        self.max_update_users = 5
        self.min_rate_data = 20
        self.max_rate_data = 300
        self.max_update_data = 10
        self.initial_number_users = initial_number_users
        self.current_number_users = initial_number_users
        self.initial_rate_data = initial_rate_data
        self.current_rate_data = initial_rate_data
        self.intrinsic_temperature = self.atmospheric_temperature + 1.25 * self.current_number_users + 1.25 * self.current_rate_data
        self.temperature_ai = self.intrinsic_temperature
        self.temperature_noai = (self.optimal_temperature[0] + self.optimal_temperature[1]) / 2.0
        self.total_energy_ai = 0.0
        self.total_eneryg_noai = 0.0
        self.reward = 0.0
        self.game_over = 0
        self.train = 1

    # MAKING A METHOD THAT UPDATES THE ENVIRONMENT RIGHT AFTER THE AI PLAYS AN ACTION
    def update_env(self, direction, energy_ai, month):

        # GETTING THE REWARD

        # Computing the energy spent by the server's cooling sysetm when there is no AI
        energy_noai = 0
        if (self.temperature_noai < self.optimal_temperature[0]):
            energy_noai = self.optimal_temperature[0] - self.temperature_noai
            self.temperature_noai = self.optimal_temperature[0]
        elif (self.temperature_noai > self.optimal_temperature[1]):
            energy_noai = self.temperature_noai - self.optimal_temperature[1]
            self.temperature_noai = self.optimal_temperature[1]
        # Computing the Reward
        self.reward = energy_noai - energy_ai
        # Scaling the Reward
        '''
        stabalizing the deep q learning computations
        '''
        self.reward = 1e-3 * self.reward

        # GETTING THE NEXT STATE

        # Updating the atmospheric temperature
        self.atmospheric_temperature = self.monthly_atmospheric_temperatures[month]        
        # Updating the number of users
        self.current_number_users += np.random.randint(-self.max_number_users, self.max_number_users)
        if (self.current_number_users > self.max_number_users):
            self.current_number_users = self.max_number_users
        elif (self.current_number_users < self.min_number_users):
            self.current_number_users = self.min_number_users
        # Updating the rate of data
        self.current_rate_data += np.random.randint(-self.max_rate_data, self.max_rate_data)
        if (self.current_rate_data > self.max_rate_data):
            self.current_rate_data = self.max_rate_data
        elif (self.current_rate_data < self.min_rate_data):
            self.current_rate_data = self.min_rate_data
        # Computing the Delta of Interinsic Temperature
        past_intrinsic_temperature = self.intrinsic_temperature
        self.intrinsic_temperature = self.atmospheric_temperature + 1.25 * self.current_number_users + 1.25 * self.current_rate_data
        delta_intrinsic_temperature = self.intrinsic_temperature - past_intrinsic_temperature

        # Computing the Delta of Temperature caused by the AI
        if direction == -1:
            delta_temperature_ai = -energy_ai
        elif direction == 1:
            delta_temperature_ai = energy_ai

        # Updating the new servers temperature when there is AI
        self.temperature_ai += delta_intrinsic_temperature +  delta_temperature_ai

        # Updating the new servers temperature when there is no AI
        self.temperature_noai += delta_intrinsic_temperature 
        
        # GETTING GAME OVER


        # UPDATING THE SCORES

        # Updating the Total Every Spent by the AI

        # Updating the Total Every spent by the server's cooling system when there is no AI

        
        # SCALING THE NEXT STATE


        # RETURNING THE NEXT STATE, THE REWARD, AND GAME OVER



    # MAKING A METHOD THAT RESETS THE ENVIRONMENT


    # MAKING A METHOD THAT GIVES US AT ANY TIME THE CURRENT STATE, THE LAST REWARD AND WHETHER THE GAME IS OVER
