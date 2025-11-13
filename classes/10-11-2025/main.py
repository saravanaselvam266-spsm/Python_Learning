class MovieTickets:
    # constructor
    def __init__(self):
        self.movies = []

    # methods
    def add_movie(self, title, price, seat):
        # current movie
        current_movie = {"title": title, "price": price, "seats": seat}
        # appending the movie to existing movies list
        self.movies.append(current_movie)
        print(f"Admin has added the movie - {title}")

    def book_ticket(self, curr_show, friends_count):
        # count - {seat} = revised_count
        for el in self.movies:
            # finding title of movie
            if el["title"] == curr_show:
                # seat - decrease
                if friends_count > el["seats"]:
                    return "Invalid Ticket count"
                else:
                    el["seats"] -= friends_count
                    print(f"{curr_show} - tickets {friends_count} sold out ")

    def cancel_ticket(self, title, count):
        pass

    def check_availability(self, title):
        result = 0
        for el in self.movies:
            if title == el["title"]:
                result = el["seats"]
        print(f"{title} - current seat is {result}")

    # extra method
    def print_movies(self):
        print(self.movies)


# bsr mall
mall_bsr = MovieTickets()
mall_bsr.add_movie(title="Interstellar", price=200, seat=100)
mall_bsr.add_movie(title="Tenet", price=250, seat=150)

# print entire movies
mall_bsr.print_movies()

# check availability
mall_bsr.check_availability("Tenet")

# ticket booking
mall_bsr.book_ticket(curr_show="Interstellar", friends_count=20)
mall_bsr.print_movies()
mall_bsr.book_ticket(curr_show="Interstellar", friends_count=30)
mall_bsr.check_availability(title="Interstellar")
