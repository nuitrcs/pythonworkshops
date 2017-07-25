from csv import DictReader 
import requests # install this before importing

fileurl = "https://raw.githubusercontent.com/nuitrcs/pythonworkshops/master/intropython/Part_4/exercise_input_files/fbi_crime_statistics.csv"
# wrote the above as a variable just for formatting

fbidata = requests.get(fileurl) # fbidata is a Response object
dr = DictReader(fbidata.text.splitlines()) #DictReader wants to be able to iterate over lines of text

# The rest is the same as the less challenging exercise:
for row in dr:
    violent_crimes = int(row["Violent crime"].replace(',', ''))
    population = int(row["Population"].replace(',', ''))
    violent_crime_ratio = (violent_crimes / population)

    print("The violent crime rate in", row["Year"], "was", violent_crime_ratio)