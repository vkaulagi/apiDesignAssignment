# from __future__ import print_function

import grpc
from service import library_pb2 as pb2
from service import library_pb2_grpc as pb2_grpc


class Client:

    def __init__(self):
        self.server = 'localhost:50051'
    
    def getTitles(self, isbnList):
        titleList = []
        with grpc.insecure_channel(self.server) as channel:
            stub = pb2_grpc.InventoryServiceStub(channel)
            for isbn in isbnList:
                response = stub.GetBook(pb2.BookRequestIsbn(isbn=isbn))
                titleList.append(response.title)
        return titleList

