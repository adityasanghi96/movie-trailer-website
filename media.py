import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Attributes shared by all Movies

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # noqa
        """This method creates a new movie

        :param movie_title: title
        :type movie_title: str
        :param movie_storyline: storyline
        :type movie_storyline: str
        :param poster_image: poster imageUrl
        :type poster_image: str
        :param trailer_youtube: youtube trailer
        :type trailer_youtube: str
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method checks current movie trailer in the Class object.

        :returns: str -- the movie trailer, and opens the youtube movie preview
        """
        webbrowser.open(self.trailer_youtube_url)
