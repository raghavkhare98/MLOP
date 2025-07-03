import numpy as np


"""

SOME SOLUTIONS HAVE BEEN MADE COMPLEX BECAUSE I WAS WANTED TO USE NUMPY FUNCTIONS INSTEAD OF STANDARD PYTHON FUNCTIONS

NORMAL PYTHON LISTS CAN BE USED FOR BETTER READABILITY, BUT I USED NUMPY ARRAYS, HENCE OUTPUS ARE SOMETHING LIKE THIS - [  2. 150.   2. 155.]

"""


"""
Q1. Select the person who is neither the shortest nor tallest from each group of 5

You have 20 people split into 4 groups of 5. Pick the  (3rd tallest) from each group.

"""

def third_tallest_from_group():

    heights = np.array([160, 170, 180, 150, 165,  
                    175, 165, 185, 160, 170,  
                    155, 165, 160, 170, 180,  
                    180, 190, 185, 175, 160])

    heights = heights.reshape(4,5)
    heights.sort()
    third_tallest = np.array([])
    for i in heights:
       
        third_tallest = np.append(third_tallest, i[2])
    
    return third_tallest

third_tallest_from_group()


"""
Q2. Get top 2 tallest from each group of 4 people
"""

def top_two_tallest():

    heights = np.array([160, 170, 180, 150, 
                        175, 165, 185, 160, 
                        155, 165, 160, 170])

    heights = heights.reshape(3, 4)
    top_two = []
    for i in heights:
        temp = []

        curr_largest_element_index = np.argmax(i)
        temp.append(int(i[curr_largest_element_index]))
        i[curr_largest_element_index] = 0
        
        second_largest_element_index = np.argmax(i)
        temp.append(int(i[second_largest_element_index]))
        top_two.append(temp)
    
    return top_two

top_two_tallest()


"""
Q3. From each group of 3, pick only tallest
"""

def pick_tallest():

    heights = np.array([[160, 170, 180], 
                        [175, 185, 165], 
                        [155, 165, 150]])

    heights = heights.reshape(3, 3)

    talest_arr = np.array([])

    for i in heights:

        talest_arr = np.append(talest_arr, i[np.argmax(i)])
    
    return talest_arr

pick_tallest()

"""
Q4. From each group of 4, return height and original index of the shortest person
"""

def height_and_index_shortest_person():

    heights = np.array([ 
        160, 170, 150, 180, 
        175, 165, 155, 185 
    ])

    heights = heights.reshape(2, 4)

    shortest_person_details_arr = np.array([])

    for i in heights:

        temp_arr = np.array([])
        temp_arr = np.append(temp_arr, np.argmin(i))
        temp_arr = np.append(temp_arr, i[np.argmin(i)])
        shortest_person_details_arr = np.append(shortest_person_details_arr, temp_arr)
    
    return shortest_person_details_arr

height_and_index_shortest_person()

"""
Q5. From each group of 5, return second shortest person
"""

def second_shortest_person():

    heights = np.array([ 
        160, 170, 150, 180, 165, 
        175, 165, 185, 160, 170, 
        155, 165, 160, 170, 180 
    ])

    heights = heights.reshape(3, 5)

    second_shortest_person_arr = np.array([])

    for i in heights:

        second_shortest_person_arr = np.append(second_shortest_person_arr, np.partition(i, 1)[1])
    
    return second_shortest_person_arr

second_shortest_person()

"""
Q6. For each group of 4, return all but the tallest person
"""

heights = np.array([ 
    160, 170, 150, 180, 
    175, 165, 155, 185, 
    165, 150, 155, 160 
])

heights = heights.reshape(3, 4)

"""
Q7. From each group of 6, return the median height
"""

heights = np.array([ 
    160, 170, 150, 180, 165, 155, 
    175, 165, 185, 160, 170, 155 
])

heights = heights.reshape(2, 6)

"""
Q8. From each group of 5, return height gap between tallest and shortest
"""
heights = np.array([ 
    160, 170, 150, 180, 165, 
    175, 185, 155, 160, 170 
])

heights = heights.reshape(2, 5)

"""
Q9. From each group of 3, return person whose height is closest to the group average
"""

heights = np.array([ 
    160, 170, 165, 
    180, 190, 175, 
    155, 160, 150 
])

heights = heights.reshape(3, 3)