import streamingcontent
import rating 
import streaming_platform

class StreamedMovie(streamingcontent.StreamingContent):

    def __init__(self, title, streaming_platform, rating, year_of_release, running_time, director, rt_rating, actors):
        super().__init__(title, streaming_platform, rating, rt_rating, actors)
        self.year_of_release = year_of_release
        self.running_time = running_time
        self.director = director

    def __str__(self):
        streaming_platformStr = ""

        if self.streaming_platform == streaming_platform.Streaming_Platform.NETFLIX:
            streaming_platformStr = "Netflix"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.DISNEY:
            streaming_platformStr = "Disney"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.AMAZON:
            streaming_platformStr = "Amazon"
        elif self.streaming_platform == streaming_platform.Streaming_Platform.APPLE:
            streaming_platformStr = "Apple"
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

        return f"""Movie Details\n\tTitle: {self.title}
        \n\tStreaming Platform: {self.streaming_platform}
        Rating: {ratingStr}\n\tRotten Tomatoes Rating: {self.rt_rating}%
        \n\tActors: {actorStr} 
        Year of Release: {self.year_of_release}\n\tRunning Time: {self.running_time}
        Director: {self.director}"""
    