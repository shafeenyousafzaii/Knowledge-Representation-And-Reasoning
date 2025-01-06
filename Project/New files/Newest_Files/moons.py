import pandas as pd

# Read the moons data into a DataFrame
moons_data = pd.read_csv('/content/drive/My Drive/satellites.csv')

# Function to generate Turtle data
def generate_turtle_moons(data):
    turtle_data = """
    @prefix : <http://example.org/solarsystem#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    ### New Moon Class
    :Moon rdf:type rdfs:Class ;
        rdfs:label "Moon" ;
        rdfs:comment "A natural satellite orbiting a planet." .

    ### Property linking planets with moons
    :hasMoon rdf:type rdf:Property ;
        rdfs:label "has Moon" ;
        rdfs:domain :Planet ;
        rdfs:range :Moon ;
        rdfs:comment "Links a planet to its moons." .

    ### Properties for moons
    :gm rdf:type rdf:Property ;
        rdfs:label "Gravitational parameter" ;
        rdfs:domain :Moon ;
        rdfs:range xsd:string ;
        rdfs:comment "The gravitational parameter of the moon." .

    :radius rdf:type rdf:Property ;
        rdfs:label "Radius" ;
        rdfs:domain :Moon ;
        rdfs:range xsd:string ;
        rdfs:comment "The radius of the moon in kilometers." .

    :density rdf:type rdf:Property ;
        rdfs:label "Density" ;
        rdfs:domain :Moon ;
        rdfs:range xsd:string ;
        rdfs:comment "The density of the moon in g/cm^3." .

    :magnitude rdf:type rdf:Property ;
        rdfs:label "Apparent Magnitude" ;
        rdfs:domain :Moon ;
        rdfs:range xsd:string ;
        rdfs:comment "The apparent magnitude of the moon." .

    :albedo rdf:type rdf:Property ;
        rdfs:label "Albedo" ;
        rdfs:domain :Moon ;
        rdfs:range xsd:string ;
        rdfs:comment "The reflectivity of the moon." .
    """
    planet_moon_links = ""
    for _, row in data.iterrows():
        moon_uri = f":{row['name'].replace(' ', '_')}"
        planet_uri = f":{row['planet']}"
        turtle_data += f"""
    ### Moon: {row['name']}
    {moon_uri} rdf:type :Moon ;
        rdfs:label "{row['name']}" ;
        :gm "{row['gm']}" ;
        :radius "{row['radius']}" ;
        :density "{row['density']}" ;
        :magnitude "{row['magnitude']}" ;
        :albedo "{row['albedo']}" ;
        :hasMoon {planet_uri} .  # Linking moon to its planet
    """

        planet_moon_links += f"{planet_uri} :hasMoon {moon_uri} .\n"

    turtle_data += f"\n### Planet-Moon Links\n{planet_moon_links}"
    return turtle_data

# Generate the Turtle content for the dataset
turtle_content = generate_turtle_moons(moons_data)

# Save the generated Turtle data to a file
output_path = '/content/drive/My Drive/moons.ttl'
with open(output_path, "w") as file:
    file.write(turtle_content)

output_path
