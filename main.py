#############=======<< 0/1 knapsack problem solver with genetic algorithm - sajjad khedmati >>=======##################
import numpy as np
import random

#TODO: CREATE SOURCE DATA TABLE LIKE THIS:
#? input :  data from user -> count + weight + price
#* output:  [ ( id , weight , price ) , ... ]
def create_product_table(size):
    table = []
    w_temp = input()
    p_temp = input()
    w = w_temp.split(' ')
    p = p_temp.split(' ')
    for i in range( 1 , size + 1 ): 
        table.append(tuple((i , w[i-1] , p[i-1])))
    return table
 
#TODO: CREATE INITIAL POPULATION FROM RANDOM INDIVIDUALS (or Chromosomes)
def create_first_population(size):
    first_population = []    
    #? max population size -> if we have n item then 2^n diffrent state will have 
    #* We consider half of the states as the initial population
    POP_MAX = int(2**size / 2)
    for i in range(POP_MAX):
        #? create rendom individuals -> [ zero/one , zero/one , ... ] 
        first_population.append(np.random.randint(0 , 2, size = size))
    return first_population 
 
#TODO: CHECK POPULATION IN EACH EVOLUTION AND RETURN THE BEST INDIVIDUALS IF EXIST
def check_population_to_find_best( population , max_weight , data_table ): 
    temp_len = len(population[0])   
    for i in range(len(population)):
        local_max = 0
        for j in range(temp_len):
            local_max += int(population[i][j]) * int(data_table[j][1])
        #? fitness -> knapsack full! 
        #? also we can use diffrent fitness to return the nearest solution ( use Percentage for each individuals )
        individual_fitness = int((local_max / max_weight) * 100)
        if local_max == max_weight: 
        #? if individual_fitness > 90 and local_max == max_weight:
            return [population[i] , individual_fitness]
    return False

#TODO: CHECK FITNESS PERCENTAGE FOR INDIVIDUAL
def fitness_function( individual , max_weight , data_table ):
    fitness = 0
    weight = 0
    for i in range(len(individual)):
        weight += int(individual[i] * int(data_table[i][1]))
    fitness = int((weight / max_weight) * 100)
    if fitness > 100 :
        return 0
    else: 
        return fitness

#TODO: SELECTED THE RANDOM INDIVIDUAL FROM POPULATION
def random_selection(population , max_weight , data_table):
    while True:
        random_index = random.randint(0 , len(population)-1)
        temp_fit = fitness_function(population[random_index], max_weight, data_table)
        #? better individual => higher chance 
        if temp_fit != 0 and temp_fit > 40 :
            return population[random_index]
        
#TODO: CREATE A NEW INDIVIDUAL ( or child ) FROM TWO PARENTS
def reproduce(first_individual , second_individual):
    length = len(first_individual)
    cross_point = random.randint(1,length-1)
    t1 = first_individual[:cross_point]
    t2 = second_individual[cross_point:]
    individual = [*t1 , *t2]
    return individual

#TODO: SOME INDIVIDUALS MUTATE RENDOMLY 
def mutation(individual):
    random_index = random.randint(0 , len(individual)-1)
    if individual[random_index] == 0 :
        individual[random_index] = 1
    else:
        individual[random_index] = 0
    return individual
    
#! ====================== GENETIC ALGORITHMS - RUSSEL VERSION ===========================
def GENETIC_ALGORITHM( population , max_weight , data_table ):
    new_population = []
    while True :       
        resault = check_population_to_find_best(population, max_weight, data_table)
        if resault:
            print(resault)
            break
        
        for i in range(len(population)) :
            child = ()
            temp_individual_one = random_selection(population , max_weight , data_table)
            temp_individual_two = random_selection(population , max_weight , data_table)
            child = reproduce(temp_individual_one , temp_individual_two)
            if random.randint(0, 100) > 60 :
                child = mutation(child)
            new_population.append(child)
            
        population = population + new_population
#! =======================================================================================
        
def main(): 
    #? the count of all product in the main table
    ARRAY_SIZE = 0
    MAX_KNAPSACK_WEIGHT = 0
    MAX_KNAPSACK_WEIGHT = int(input('maximum knapsack weight?\n'))
    ARRAY_SIZE = int(input('count of product?\n'))
    product_table = create_product_table(ARRAY_SIZE)    
    
    population = create_first_population(ARRAY_SIZE)  
    GENETIC_ALGORITHM( population , MAX_KNAPSACK_WEIGHT , product_table )
    
if __name__ == '__main__':
    main()
    