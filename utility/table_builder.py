#Builds HTML table of flag images from a given JSON file and flag image folder
#JSON file -> country_data.json
#Flags folder -> /flags
#Each row holds five cells, with a flag image in each cell
#id is set to the 2-letter ISO country identifier
#class is set to found/missing which determines image transparency using CSS

import json

#Open the JSON file and convert it to a list of dictionariest
#One dict for each country, with keys "Name" "Code"
with open('country_data.json') as country_json_data:
         country_data = json.load(country_json_data)

print(country_data[0]["Code"])

#Write table to a html file
with open('table_gen.html', "w+") as table_html:
    table_html.write("<table id='flag-table'>\n")
    #Cell counter, after 5 cells create a new row
    counter = 1

    #Generate table
    for country in country_data:

        #Check for apostrophes and escape
        if "\'" in country["Name"]:
            country["Name"] = country["Name"].replace("'", "\'")


        if(counter == 1):
            table_html.write("<tr>\n")

        #Build html string

        #Setup opening <td> and class / id
        #Look into stringbuilder equivalent for python
        html_string  =  "<td class=\"missing\" id=\""
        html_string +=  country["Code"]
        html_string +=  "\">"

        #Inner img
        html_string += "<img src=\"/flags/"
        html_string += country["Code"]
        html_string += ".png\" "
        html_string += "title=\""
        html_string += country["Name"]
        html_string += "\"/>"

        #Close </td>
        html_string += "</td>\n"

        #Write to file
        table_html.write(html_string)

        if(counter > 5 or country == country_data[-1]):
            table_html.write("</tr>\n")
            counter = 0

        counter+=1

    table_html.write("</table>")
