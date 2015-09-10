#!/usr/bin/env python
"""
This file contains instances of movie objects.
By running this file you will have the page rendered with all
movie instances on the webpage.
"""
import fresh_tomatoes
import media

pans_labyrinth = media.Movie("Pan's Labyrinth",
                             "Story about a little girl who ventures a"
                             " crazy world.",
                             "https://upload.wikimedia.org/wikipedia/"
                             "en/6/67/Pan%27s_Labyrinth.jpg",
                             "https://www.youtube.com/watch?v=4Evmr2ZCjWc",
                             "2003",
                             "Ivana Baquero, Sergi Lopez")

fight_club = media.Movie("Fight Club",
                         "First rule about the fight club is: "
                         "You do not talk about fight club.",
                         "https://upload.wikimedia.org/wikipedia"
                         "/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "1999",
                         "Brad Pitt, Edward Norton")

the_avengers = media.Movie("The Avengers",
                           "Group of super hero badasses try to "
                           "save humanity.",
                           "https://upload.wikimedia.org/wikipedia"
                           "/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=zatgnqdIefs",
                           "2012",
                           "Scarllet Johanson, Robert Downey Jr.")

ted = media.Movie("Ted",
                  "Toy teddy bear comes to life and gets crazy.",
                  "https://upload.wikimedia.org/wikipedia"
                  "/en/6/62/Ted_poster.jpg",
                  "https://www.youtube.com/watch?v=8YBlnHxkCJc",
                  "2012",
                  "Mark Walberg")


movies = [pans_labyrinth, fight_club, the_avengers, ted]

fresh_tomatoes.open_movies_page(movies)
