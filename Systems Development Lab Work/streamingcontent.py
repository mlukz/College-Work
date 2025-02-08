class StreamingContent:
    def __init__(self, title, streaming_platform, rating, rt_rating, actors):
        if(rt_rating < 0 or rt_rating > 100):
            rt_rating = 0 
        self.title = title
        self.streaming_platform = streaming_platform
        self.rating = rating
        self.rt_rating = rt_rating 
        self.actors = actors 
