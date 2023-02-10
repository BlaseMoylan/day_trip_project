# (5 points): As a developer, I want to make at least three commits
#     with descriptive messages 
# (5 points):  As a developer, I want to store my destinations,
#     restaurants, mode of transportation, and entertainment
#     in their own separate Lists. 
# (5 points): As a user, I want a destination to be randomly selected 
#     for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected 
#     for my day trip
# (5 points): As a user, I want a mode of transportation to be 
#     randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be 
#     randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a 
#     destination, restaurant, mode of transportation, 
#         and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that 
#     my day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip 
#     in the console
# (5 points): Single Responsibility: As a developer, I want 
#     all of my functions to have a Single Responsibility. 
#     Remember, each function should do just one thing! 
import random
def run_day_trip_generator():
    destination_list=['Rome','Spain','China','NewYork','Paris','Hawaii']
    restaurant_list=['JimmyJohns','SteakHouse','Shiki','Hudsons Hamburgers','Sonic']
    entertainment=['Hiking','skiing','snowboarding','skydiving','paragliding']
    transportation=['car','plan','teleportaion','train','boat','bike']
    names_of_options=['destination','restaurant','entertainment','transportation']
    list_of_options=[destination_list,restaurant_list,entertainment,transportation]
    initial=print_out_day_trip(list_of_options,names_of_options)
    user_input=input('do you like what you see? (yes or no) ')
    user_satisfaction=False
    while user_satisfaction==False:
        if user_input=='no':
            # print_out_day_trip(list_of_options)
            to_change=input(f'what so you not like? (please select one of the following: {names_of_options})')
            for item in names_of_options:
                if item==to_change:
                    index=names_of_options.index(item)
                    for item in list_of_options:
                        if list_of_options.index(item)==index:
                            random_num=random.randrange(len(item))
                            name=item[random_num]
                            initial[index]=names_of_options[index]+': '+name

            for item in initial:
                print(item)
            user_input=input('do you like what you see? (yes or no) ')
        elif user_input=='yes':
            print( 'your day trip:')
            user_satisfaction=True
            for item in initial:
                print(item)
            print('Have a nice day')
           
       


def print_out_day_trip(list_options,names):
    # names=['destination','restaurant','entertainment','transportation']
    index=0
    day_trip_list=[]
    for item in list_options:
        random_index=random.randrange(len(item))
        name=item[random_index]      
        #print(f'{names[index]}: {name}')
        day_trip_list.append(f'{names[index]}: {name}')
        index+=1
    for item in day_trip_list:
        print(item)
    return day_trip_list
run_day_trip_generator()