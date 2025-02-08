import streamingcontent
import rating
import streaming_platform

class StreamedTVShow (streamingcontent.StreamingContent):
    def __init__(self, title, streaming_platform, rating, rt_rating, actors, seasons, show_runner):
        super().__init__(title, streaming_platform, rating, rt_rating, actors)
        self.seasons = seasons
        self.show_runner = show_runner

    def __str__(self):

        streaming_platformStr = ""

        if self.streaming_platform == streaming_platform.Streaming_Platform.NETFLIX:
            streaming_platformStr = "Netflix"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.DISNEY:
            streaming_platformStr = "Disney"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.AMAZON:
            streaming_platformStr = "Amazon"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.PARAMOUNT:
            streaming_platformStr = "Paramount"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.NOW:
            streaming_platformStr = "NOW"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.MUBI:
            streaming_platformStr = "MUBI"

        ratingStr = ""
        if self.rating == rating.Rating.G:
            ratingStr = "G"
        elif self.rating == rating.Rating.PG:
            ratingStr = "PG"
        if self.rating == rating.Rating._12:
            ratingStr = "12"
        elif self.rating == rating.Rating._15:
            ratingStr = "15"
        elif self.rating == rating.Rating._16:
            ratingStr = "16"
        elif self.rating == rating.Rating._18:
            ratingStr = "18"

        actorStr = ""
        i = 0 
        for actor in self.actors:
            actorStr += actor 
            i += 1
            if i != len(self.actors):
                actorStr += ", "

        seasonStr = ""
        for key, value in self.seasons.items():
            seasonStr += "\n\tSeason: {} Number of Episodes: {}".format(key,value)

        return f"""TV Show Details\n\tTitle: {self.title}
        \n\tStreaming Platform: {streaming_platformStr}
        Rating: {ratingStr}\n\tRotten Tomatoes Rating {self.rt_rating}%\n\tActors: {actorStr}
        Show Runner: {self.show_runner}\n\tSeason Details: {seasonStr}"""



    #def __str__(self):
       # seasonsStr = ""
        #for key,value in self.seasons.items():
            #seasonsStr += "\n\tSeason: {} Number of Episodes: {}".format(key,value)
        #return f"""TV Show Details\n\tTitle: {self.title}\n\tStreaming PLatform: {self.streaming_platform}
        #Rating: {self.rating}\n\tShow Runner: {self.show_runner}\n\tSeason Details: {seasonsStr}"""
    