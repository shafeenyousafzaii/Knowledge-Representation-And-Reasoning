import csv
from rdflib import Graph, URIRef, Literal, Namespace

# Create a graph and a namespace
g = Graph()
EX = Namespace("http://example.org/")

# Open your CSV file
with open('planets.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # Create a URI for each row (book)
        book_uri = URIRef(f"http://example.org/book/{row['planet']}")

        # Add triples to the graph
        g.add((book_uri, EX.hasTitle, Literal(row['title'])))
        g.add((book_uri, EX.hasAuthor, Literal(row['author'])))
        g.add((book_uri, EX.hasGenre, Literal(row['genre'])))

# Serialize the RDF to a file
g.serialize('books.rdf', format='xml')
