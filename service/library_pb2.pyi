from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: Status
DESCRIPTOR: _descriptor.FileDescriptor
FANTASY: Genre
SCIENCE_FICTION: Genre
SELF_HELP: Genre
TAKEN: Status

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishing_year", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: int
    publishing_year: int
    title: str
    def __init__(self, title: _Optional[str] = ..., publishing_year: _Optional[int] = ..., genre: _Optional[_Union[Genre, str]] = ..., author: _Optional[str] = ..., isbn: _Optional[int] = ...) -> None: ...

class BookRequestIsbn(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: int
    def __init__(self, isbn: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book1", "inventory_number"]
    BOOK1_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    book1: Book
    inventory_number: int
    def __init__(self, inventory_number: _Optional[int] = ..., book1: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
