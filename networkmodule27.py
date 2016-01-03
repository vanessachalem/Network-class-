'''
Created on Jun 6, 2013
module exports a Network class in python 2.75
@author: Vanessa
'''

from personmodule27 import Person

#will import sys for user input
import sys 

class Network:
    """
    creates a Network object where people can add friends, remove friends, remove all friends, get the number of friends they have,
    get a list of their friends and get a list of their friends which are their same age 
    """
    
    #creates a dictionary where each Person friend that is added by the user will be stored with their name 
    #keys will be the friend object
    #value will be string of the friend's name
    dictionaryOfFriends = {}
    
    def __init__(self):
        """constructor - initializes a network object"""      
            
    def user_choice(self):
        """asks for the user's choice and returns the user's input"""
        print
        print "Would you like to add friends, remove friends, remove all friends, get number of friends, get friends, get friends of same age or sign out?"       
        print "Please choose by typing your preference exactly as it is written above: "
        userInput = sys.stdin.readline()
        return userInput 

    def user_info(self):
        """prompts the user for his information and returns a user Person"""
        print "What is your name: "
        userName = sys.stdin.readline()
        print "What is your age:"
        userAge = sys.stdin.readline()
        #create user Person with that name and age
        user = Person(userName, userAge)
        return user
    
    def friend_info(self):
        """interacts with the user asking for his friend's information and returns a friend Person"""
        print "Please enter your friend's name:"
        friendName = sys.stdin.readline()
        print "Please enter their age"
        friendAge = sys.stdin.readline() 
        #create friend Person with that name and age
        friend = Person(friendName, friendAge)
        return friend
        
    def add_friend(self):
        """prompts the user for his friend's info and adds it to the dictionary of the user's friends with its name"""
        friend = socialNetwork.friend_info()
        #adds friend to the dictionary with the key being the friend object and the value being its name
        self.dictionaryOfFriends[friend] = friend.get_name()
        print friend.get_name(), " was added"
    
    def friend_to_remove(self, friend):
        """takes a friend Person as parameters, then 
        iterates through the dictionary of friends and returns f, the friend with the given name and age"""
        for f in self.dictionaryOfFriends.keys():
            if(f.get_name() == friend.get_name() and f.get_age()== friend.get_age()):
                return f
        
    def remove_friend(self):
        """prompts the user for his friend's info and removes it from the dictionary of the user's friends"""
        friend = socialNetwork.friend_info()
        friendToRemove = socialNetwork.friend_to_remove(friend)
       
        if not friendToRemove:
            print "this person isn't within your set of friends"
        else:
            del self.dictionaryOfFriends[friendToRemove]
            print friendToRemove.get_name(), "was removed"
        
    def remove_all_friends(self):
        """ removes all of the user's friends""" 
        self.dictionaryOfFriends.clear()
        print "All of your friends have been removed. You currently have no friends"
        
    def get_number_of_friends(self):
        """prints the number of friends that the user has"""
        if self.dictionaryOfFriends.__len__() == 1:
            print "you have", self.dictionaryOfFriends.__len__(), "friend"
        else:
            print "you have", self.dictionaryOfFriends.__len__(), "friends"
        
    def get_friends(self):
        """print a set of the names of all of the user's friends"""
        if not self.dictionaryOfFriends:
            print "you have no friends"
        else:
            print "these are your friends:", self.dictionaryOfFriends.values()
    
    def get_friends_same_age(self):
        """prints a set of user's friends of the same age"""
        friendsSameAge = set()
        #for all friends in the dictionary whose age = the user's age
        for friend in self.dictionaryOfFriends:
            if friend.get_age() == user.get_age():
                #adds the friend's name to the set friendsSameAge
                friendsSameAge.add(self.dictionaryOfFriends.get(friend))
        if not friendsSameAge:
            print "You have no friends of your same age"
        else:
            print "these are your friends of your same age:", friendsSameAge
    
    def change_string(self, word):
        """
        Takes a word and returns the word without white space before/after the word and in lower case 
        and without an 's' at the end of the word since this is a letter that can accidentally be typed or missed in the end of several of these words
        - this is done in order to remove space and caps sensitivity on user input in the main method
        """
        return word.lower().strip().rstrip('s')
    

#creates a network object   
socialNetwork = Network()
 
print"Welcome to the Social Network!"
    
#prompts user for his info - will save the Person object that is return by the method under the variable user
user = socialNetwork.user_info()
    
    
def main(socialNetwork):
    """main method - interacts with the user and calls the other methods using a dictionary"""
    
    #creates a dictionary with the keys being the possible user inputs and the values being the methods that will be called
    dict = {"add friend": socialNetwork.add_friend, "remove friend": socialNetwork.remove_friend, "remove all friend": socialNetwork.remove_all_friends, "get number of friend": socialNetwork.get_number_of_friends, "get friend": socialNetwork.get_friends, "get friends of same age": socialNetwork.get_friends_same_age}

    #asks user what he would like to do      
    userOption = socialNetwork.user_choice()
    
    #as long as user doesn't want to sign out             
    while (socialNetwork.change_string(userOption)!="sign out"):
        #determines which function to call based on the user's choice and it's value in the dictionary
        functionToCall = dict[socialNetwork.change_string(userOption)]
        #calls the function
        functionToCall()
        #asks the user again what he would like to do
        userOption = socialNetwork.user_choice()
        

    #if user types "sign out"
    print
    print"Signing out. Thank you for visiting the social network, come again to acquire more friends!"
    #will exit the program
    return
    


#in order to call the main method
if __name__ == "__main__":
    main(socialNetwork)         