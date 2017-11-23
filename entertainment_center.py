import media
import fresh_tomatoes
# entertainment_center.py file uses the content of media.py
# to define class movie
harry_potter = media.Movie("Harry Potter 1",
                        "Harry Potter, an eleven-year-old orphan,\
                        discovers that he is a wizard and is\
                        invited to study at Hogwarts. Even as\
                        he escapes a dreary life and enters a\
                        world of magic, he finds trouble awaiting him.",
                        "http://www.impawards.com/2001/posters/harry_potter_and_the_sorcerers_stone_ver5_xlg.jpg",  # noqa
                        "https://www.youtube.com/watch?v=VyHV0BRtdxo")

transformers = media.Movie("Transformers 1",
                        "a teenager who gets caught up in a war\
                        between the heroic Autobots and the villainous\
                        Decepticons",
                        "http://www.impawards.com/2007/posters/transformers_ver4_xlg.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KrUhwet0ngg")


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

cars = media.Movie("Cars",
                   "Follows a group of autos as they travel Route 66.",
                   "http://www.impawards.com/2006/posters/cars_ver2.jpg",
                   "https://www.youtube.com/watch?v=WGByijP0Leo")

incredibles = media.Movie("The Incredibles",
                          "Family of superheroes who are forced to hide \
                          their powers and live a quiet suburban life.",
                          "http://www.impawards.com/2004/posters/incredibles_ver2.jpg",  # noqa
                          "https://www.youtube.com/watch?v=eZbzbC9285I")

movies = [harry_potter, toy_story, incredibles, transformers, avatar, cars]
fresh_tomatoes.open_movies_page(movies)
