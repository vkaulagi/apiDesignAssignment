import library_pb2 as library_pb2


book1 = library_pb2.Book()
book1.title = "first_book"
book1.publishing_year = 1910
book1.isbn = 100
book1.author = "alpha"
book1.genre = library_pb2.SCIENCE_FICTION

book2 = library_pb2.Book()
book2.title = "second_book"
book2.publishing_year = 1920
book2.isbn = 200
book2.author = "beta"
book2.genre = library_pb2.FANTASY

book3 = library_pb2.Book()
book3.title = "third_book"
book3.publishing_year = 1930
book3.isbn = 300
book3.author = "gamma"
book3.genre = library_pb2.SELF_HELP

bookList = [book1, book2, book3]
