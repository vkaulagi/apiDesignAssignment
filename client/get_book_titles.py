import logging
import inventory_client


def getBookTitles(clientObj, isbnList):
    titlesList = clientObj.getTitles(isbnList)
    print(titlesList)


if __name__ == '__main__':
    logging.basicConfig()
    clientObj = inventory_client.Client()
    isbnList = [100, 200]
    getBookTitles(clientObj, isbnList)
