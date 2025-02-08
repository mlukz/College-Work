import streamedmovie
import streamedtvshow
import streaming_platform
import rating

movie = streamedmovie.StreamedMovie("Top Gun: Maverick", streaming_platform.Streaming_Platform.PARAMOUNT, rating.Rating._12, 2022, 130 , "Joseph Kosinski", 96, {"Tom Cruise", "Jennifer Connelly", "Miles Teller"})
print (movie.__str__())

tvshow = streamedtvshow.StreamedTVShow("Succession", streaming_platform.Streaming_Platform.NOW, rating.Rating._15, 94, {"Brian Cox", "Jeremy Strong", "Kieran Culkin", "Sarah Snook"}, {1 : 10,2 : 10,3 : 10,4 : 10}, "Jesse Armstrong")
print (tvshow.__str__())