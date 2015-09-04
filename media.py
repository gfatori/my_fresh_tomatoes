import webbrowser


class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url, release_date, cast):
		self.movie_title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.release_date = release_date
		self.cast = cast

	def show_trailer(self):
		webbrowser.open(self.trailer_link)