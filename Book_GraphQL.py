import collections

from graphene import ObjectType, String, Schema, Int, Field

Book = collections.namedtuple("Book", ['title', 'author', 'pages'])

data = {
    1: Book("To Kill a Mockingbird", "Harper Lee", 56),
    2: Book("1984", "George Orwell", 63),
    3: Book("The Catcher in the Rye", "J.D. Salinger", 76)
}

class BookType(ObjectType):
    title = String()
    author = String()
    pages = Int()

    def resolve_titlee(person, info):
        return person.title

    def resolve_author(person, info):
        return person.author

    def resolve_pages(person, info):
        return person.pages

class Query(ObjectType):
    book = Field(BookType)

    def resolve_book(root, info):
        return data[2]

schema = Schema(query=Query)

query = '{book {title author pages} }'

result = schema.execute(query)

# Print the result
print(result.data)


# selected

query1 = '{book {title author} }'

result = schema.execute(query1)

# Print the result
print(result.data)
