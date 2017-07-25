from csv import DictReader # First import `DictReader` class from csv 
with open("fbi_crime_statistics.csv", 'r') as f:
    # This creates a csv "DictReader" object that will let us access individual
    # fields in the csv file by name.
    dr = DictReader(f)

    # DictReader objects can be looped over just like file objects.
    for row in dr:
        # The values in this csv contain commas, so we have to strip those out
        # and then convert to integer (by default every field will be read in as
        # a string).
        violent_crimes = int(row["Violent crime"].replace(',', ''))
        population = int(row["Population"].replace(',', ''))
        violent_crime_ratio = (violent_crimes / population)

        print("The violent crime rate in", row["Year"], "was", violent_crime_ratio)