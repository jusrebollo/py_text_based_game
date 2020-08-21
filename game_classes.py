class Path:
    type_of_path = "default"
    animal = "default"

    def __init__(self, weather):
        """
        Constructor for Path
        """

        self.weather = weather
        pass

    def __str__(self):
        """
        insert a method docstring
        """
        # return a string with the name and description of pet so that it
        # matches the sample output from assignment
        return '{} {}'.format("You have chosen the", self.type_of_path)

        pass


class River_path(Path):
    """"""

    animal = 'mountain lion'

    def __str__(self):
        """
        insert a method docstring
        """
        return '{} {}'.format("You have chosen the river path look out for the"
                              "mighy", self.animal)
        pass

    def __repr__(self):
        return repr("It is hard to run from a  " + self.animal)

    def weather(self):
        """

        """

        #
        return '{} {} '.format("The weather is", self.weather)


class Mountain_path(Path):
    """

    """

    animal = 'bear'

    def __init__(self, weather, __treasure_value):
        """
        Constructor for Path
        """
        self.__treasure_value = 0
        self.weather = weather
        pass

    def __str__(self):
        """
        insert a method docstring
        """
        # return the name and description of the house cat so that it matches
        # the sample output from assignment
        return '{} {}'.format("You have chosen the mountain path, look out for"
                              " the", self.animal)

    def __repr__(self):
        return repr("It is hard to run from a " + self.animal)

    def weather(self):
        """

        """

        #
        return '{} {} '.format("The weather is", self.weather)

    def __treasure_private(self, __treasure_value):
        """
            This is private method
        """
        if self.__treasure_value == 1:
            print("You found D.B. Cooper's treasure!!!")
        if self.__treasure_value == 0:
            print("Oops no treasure!")
        return "You did it!"


if __name__ == '__main__':
    # unit test using assert
    mountain = Mountain_path("Warm", 1)
    river = River_path("Warm")
    assert river.weather == "Warm", "Weather not working!"

    assert repr(mountain) == "'It is hard to run from a bear'", "repr is " \
                                                                "not working"
    print("Unit tests are successful!")
