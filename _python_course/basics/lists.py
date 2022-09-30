# import loading animation
from loading_animation import loading_animation
# import required components
import time



def app():
    # Clear Console Window before code
    print('\033c')
    
    # # Define Array(List) 
    # # accepts all data types
    # # friends=['Max', 2]
    # friends=['Max', 'Alistair', 'Chris']

    # # Access elements from indexed position with positive and negative values
    # print(friends[-1]) #prints 'Chris'
    # print(friends[0]) #prints 'Max'

    # # Selec trailing elements at specified index position in reverse or sequential order
    # print(friends[1:])
    # print(friends[:-1])


    # # Define more friends for range example
    # friends=['Max', 'Alistair', 'Chris', 'Tyson', 'Bryce', 'Georgia']

    # # Select a range of elements in the list
    # print(friends[1:6])

    # ******** Using functions with Lists example ********
    # Define more friends for example
    
    friends=['Max', 'Alistair', 'Chris', 'Tyson', 'Bryce', 'Georgia']
    # define restore friends function:
    def restore_friends(opt):
        nonlocal friends
        if opt: 
            friends=['Max', 'Alistair', 'Chris', 'Tyson', 'Bryce', 'Georgia']
            return friends
        friends.clear()

    # Define Numbers List
    lucky_numbers=[4, 8, 15, 16, 32, 42]

    # using the extend function to add an addtional list to the end of the list
    # friends.extend(lucky_numbers)

    # using append function to add an element to the end of a list
    # friends.append('Ben')

    # using the insert function to insert an element at the specified index position
    friends.insert(1, 'Ben')

    # using the remove function to remove the matching string element from the list
    friends.remove('Georgia')
    friends.remove('Bryce')

    # using the clear function to empty the list
    # friends.clear()

    # using the pop function to remove an element from the end of a list
    friends.pop()

    # using the index function to find an element at the specified index within the list
    # print('\033cHere is the indexed position within the friends list of my boss, Ben:',friends.index("Ben"))

    # using the count function to count how many times the specified string is stated in the list
    friends.clear()
    addfriends=['Max']
    multiplier=5
    friends.extend(addfriends*multiplier)
    # print('friends.extend(addfriends*multiplier) Output: ')
    # print('Here is my modified list of work friends:',friends)
    # print('Here is how many times Max is specified in this list:',friends.count('Max'))

    # using the count function to count how many times the specified string is stated in the list
    
    # Print Results

    loading_animation('load', 'Restoring Friends List..', 'Restore Complete.')
    time.sleep(1.6)
    restore_friends(True)
    print('Here is my full list of work friends:',friends)
    # Exit Code
    loading_animation('exit')
# Run main app code
app()