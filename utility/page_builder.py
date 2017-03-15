#Builds HTML table of flag images from a given JSON file and flag image folder
#JSON file -> country_data.json
#Flags folder -> /flags
#Each row holds five cells, with a flag image in each cell
#id is set to the 2-letter ISO country identifier
#class is set to found/missing which determines image transparency using CSS

import json

#Vars
cells_per_row = 19;


#Open the JSON file and convert it to a list of dictionariest
#One dict for each country, with keys "Name" "Code"
with open("country_data.json", mode='r', encoding='utf-8') as country_json_data:
         country_data = json.load(country_json_data)


#Write to html file
with open('FlagIt.html', mode="w+", encoding="utf-8") as html_page:

    #Doc
    html_page.write("<!DOCTYPE html>\n")

    #Head
    html_page.write("<html>\n")
    html_page.write("\t<head>\n")
    html_page.write("\t\t<meta charset=\"UTF-8\">\n")
    html_page.write("\t\t<link rel=\"stylesheet\" href=\"FlagIt.css\"/>\n")
    html_page.write("\t\t<script type=\"application/javascript\" src=\"browser-polyfill.js\"></script>\n")
    html_page.write("\t</head>\n\n")

    #Body start
    html_page.write("\t<body>\n\n")

    html_page.write("\t\t<table id=\"flag-table\">\n")
    #Cell counter, after 5 cells create a new row
    counter = 1
    #Each image will be assigned a value, 1-248 used to help populate missing/found string
    total = 1

    #Generate table
    for country in country_data:

        #Check for apostrophes and escape
        if "\'" in country["Name"]:
            country["Name"] = country["Name"].replace("'", "\'") #Read up on escaping single quotes - tooltip not showing in FF


        if(counter == 1):
            html_page.write("\t\t\t<tr>\n")

        #Build html string

        #Setup opening <td> and class / id
        #Look into stringbuilder equivalent for python
        html_string  =  "\t\t\t\t\t<td class=\"missing\" id=\""
        html_string +=  country["Code"]
        html_string +=  "\">"

        #Inner img
        html_string += "<img id=\""
        html_string += str(total)
        html_string += "\" src=\"/flags/"
        html_string += country["Code"]
        html_string += ".png\" "
        html_string += "title=\""
        html_string += country["Name"]
        html_string += "\"/>"

        #Close </td>
        html_string += "</td>\n"

        #Write to file
        html_page.write(html_string)

        if(counter > cells_per_row  or country == country_data[-1]):
            html_page.write("\t\t\t</tr>\n")
            counter = 0

        counter+=1
        total+=1

    html_page.write("\t\t</table>\n\n")

    #Hover text
    html_page.write("<p id=\"hover_text\"> </p>")

    #Setup script - for handlers
    html_page.write("\t\t<script type=\"text/javascript\" src=\"FlagIt.js\"></script>\n\n")

    #Body end
    html_page.write("\t</body>\n\n")

    #Page end
    html_page.write("</html>")
