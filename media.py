#!/usr/bin/env python
import webbrowser
"""
This file contains the movie class and its functions.
"""


class Movie():

    """
    Describes a movie object.
    """

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url, release_date, cast):
        """
        Initializes the movie object
        """
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
        self.cast = cast

    def show_trailer(self):
        """
        Opens the trailer in a web browser using the trailer_link
        attribute of the movie object.
        """
        webbrowser.open(self.trailer_link)
