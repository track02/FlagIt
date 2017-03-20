#Builds HTML table of flag images from a given JSON file and flag image folder
#JSON file -> country_data.json
#Flags folder -> /flags
#Each row holds five cells, with a flag image in each cell
#id is set to the 2-letter ISO country identifier
#class is set to found/missing which determines image transparency using CSS

import json
import os

#Vars
cells_per_row = 19;


#Open the JSON file and convert it to a list of dictionaries
#One dict for each country, with keys "Name" "Code"
with open("country_data.json", mode='r', encoding='utf-8') as country_json_data:

    country_data = json.load(country_json_data)

    for country in country_data:
        #If country exists - find the image file and rename it to the country name
        print(country)
        print("../World Flags/{0}.png".format(country["Code"].lower()))
        print(os.path.isfile("../World Flags/{0}.png".format(country["Code"].lower())))
        if(os.path.isfile("../World Flags/{0}.png".format(country["Code"].lower()))):
            os.rename("../World Flags/{0}.png".format(country["Code"].lower()), "../World Flags/{0}.png".format(country["Name"]))

