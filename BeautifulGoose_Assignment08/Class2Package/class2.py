


class Headphones(object):
    """
    Model of headphones and how they play music
    """
    def __init__(self, model): 
        """
        Constructor
        @param model String: The model of headphones being used   
        """
        self.__model = model
        
    def get_model(self): 
        """
        @return String: The model of the current object
        """
        return self.__model
    
    def set_model(self, model):
        """
        Assign a value to the model of the current object
        @param model String: The model to be assigned.
        """
        self.__model = model

    def playedMusic(song):  
        """
        @param song String: The song that is played through the headphones
        """
        print("The song that was played is " + song)
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        """
        return "model: " + self.__model

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Headphones('{self.__model}')"    

    