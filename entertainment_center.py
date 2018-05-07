import media, fresh_tomatoes

# my movies
black_panther = media.Movie("Black Panther",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

infinity_war = media.Movie("Infinity War",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

operation_red_sea = media.Movie("Operation Red Sea",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Operation_Red_Sea_poster.jpg/220px-Operation_Red_Sea_poster.jpg",
                                "https://www.youtube.com/watch?v=7sOD1Qc0O4M")

ready_player_one = media.Movie("Ready Player One",
                               "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
                               "https://www.youtube.com/watch?v=cSp1dM2Vj48")

detective_chinatown_2 = media.Movie("Detective Chinatown 2",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/DetectiveChina2.jpeg/220px-DetectiveChina2.jpeg",
                                    "https://www.youtube.com/watch?v=0tTiuploPMM")

rampage = media.Movie("Rampage",
                      "https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg",
                      "https://www.youtube.com/watch?v=SaZNFH4OORg")

# make a list of the movies and create the web page
movies = [black_panther, infinity_war, operation_red_sea, ready_player_one, detective_chinatown_2, rampage]
fresh_tomatoes.open_movies_page(movies)
