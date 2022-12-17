from concurrent import futures

from google.protobuf import struct_pb2

import logging
import grpc
import library_pb2 as library_pb2
import library_pb2_grpc as library_pb2_grpc
import database as database


class InventoryService(library_pb2_grpc.InventoryServiceServicer):
    # store = inventory.Inventory()

    # def __init__(self, store):
    #     self._store = store

    def CreateBook(self, request, context):
        return struct_pb2.Value()

    def GetBook(self, request, context):
        # return library_pb2.Book(title=database.book1.title, publishing_year=database.book1.publishing_year,
        # authors=database.book1.authors, isbns=database.book1.isbns)
        reqIsbn = request.isbn
        for book in database.bookList:
            if book.isbn == reqIsbn:
                return book
        return library_pb2.Book

        # return self._store.get_book(request.isbn)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store = InventoryService
    library_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
