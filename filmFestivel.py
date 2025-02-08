from abc import ABC, abstractmethod
from datetime import date

# Actor Class
class Actor:
    def __init__(self, name, origin, dob):
        self._name = name
        self._origin = origin
        self._dob = dob

    def get_name(self):
        return self._name
    def get_origin(self):
        return self._origin
    def get_dob(self):
        return self._dob


# Abstract Film Class
class Film(ABC):
    def __init__(self, title, director, film_length):
        self._title = title
        self._director = director if director else "Unknown Director"
        self._film_length = film_length

        self._score = 0
        self._status = "Under_Review"

    def get_title(self):
        return self._title
    def get_director(self):
        return self._director
    def get_film_length(self):
        return self._film_length

    def get_score(self):
        return self._score
    def set_score(self, input):
        if input > 0 and input < 11:
            self._score = input
        else:
            print("Invalid score. Must be between 1 and 10.")

    def get_status(self):
        return self._status
    def set_status(self, input):
        statusList = ["Under_Review", "Approved", "Rejected"]
        if input in statusList:
            self._status = input
        else:
            print("Invalid status. Allowed values: Under_Review, Approved, Declined.")

    @abstractmethod
    def showDetails(self):
        pass


# Feature_Film Class
class Feature_Film(Film):
    _NUMFEATURES = 0

    def __init__(self, title, director, film_length, genre, actor_list):
        super().__init__(title, director, film_length)
        genreList = ["Action", "Comedy", "Drama"]
        self._genre = genre if genre in genreList else ["Unknown Genre"]
        self._actor_list = actor_list
        Feature_Film._NUMFEATURES += 1

    def get_genre(self):
        return self._genre

    def set_genre(self, input):
        genreList = ["Action", "Comedy", "Drama"]
        if input in genreList:
            self._genre = input
        else:
            print("Invalid genre. Must be Action, Comedy, or Drama.")

    def get_actor_list(self):
        return self._actor_list

    @classmethod
    def get_NUMFEATURES(cls):
        return cls._NUMFEATURES

    def submitScore(self, score):
        self.set_score(score)
        if score > 6:
            self.set_status("Approved")
        else:
            self.set_status("Declined")

    def showDetails(self):
        print("Feature Film: ",self.get_title())
        print("\tDirector: ", self.get_director())
        print("\tLength (mins): ", self.get_film_length())
        print("\tGenre: ", self.get_genre())
        print("\tScore: ", self.get_score())
        print("\tStatus: ", self.get_status())
        print("\tActors:")
        for index, actor in enumerate(self._actor_list, start=1):
            print("\t\tActor #", index)
            print("\t\tName: ", actor.get_name())
            print("\t\tCountry: ", actor.get_origin())
            print("\t\tDOB: ",actor.get_dob())


# Main Program
actor1 = Actor("Toni Servillo", "Italy", date(1959, 1, 25))
actor2 = Actor("Sabrina Ferilli", "Italy", date(1964, 6, 28))

feature1 = Feature_Film("La Grande Belezza", "Paolo Sorrentino", 141, "Drama", [actor1, actor2])

feature1.submitScore(7)
feature1.showDetails()
print()
print("Total number of feature films:", Feature_Film.get_NUMFEATURES())
