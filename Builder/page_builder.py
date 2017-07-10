#Given a folder containing a flag_list.txt file and associated images
#Produce a HTML table with each cell holding a flag image
#Create a country selection page for each letter
#Generate a home page listing A..Z and linking to relevant selection page
import sys;
import os;

#Vars
cells_per_row = 6
master_directory = sys.argv[1] #Second parameter is directory to process

if (sys.argv[2].lower() == "true"):
	chrome_build = True
else:
	chrome_build = False



#Alphabetical dictionary used to build content pages
country_dict = dict();
start_char = "a"

#Init to empty lists
for a in range(0,26):
    country_dict[start_char] = []
    start_char = chr(ord(start_char) + 1)

#for each sub-directory
for directory in sorted(os.listdir(master_directory)):

    #Get the directory name
    dirname = os.path.split(directory)[1]

    #Total no. regions - use to dynamically determine a nice no. of cells per row [TODO]
    dirtotal = len(os.listdir(master_directory))

    #First character - determine if a new contents page is needed
    firstchar = dirname[0]

    #Add country to dict - unless world flags
    if(dirname != "World Flags"):
        country_dict[firstchar.lower()].append(dirname)
        cells_per_row = 6
    else:
        cells_per_row = 15

    #total regions in the country
    total = 0

    #Write to html file
    with open("Pages/{0}.html".format(dirname), mode="w+", encoding="utf-8") as html_page:

        html_page.write("<!DOCTYPE html>\n\n")

        #Head
        html_page.write("<html>\n\n")
        html_page.write("\t<head>\n")

        html_page.write("\t\t<meta charset=\"UTF-8\">\n")
        html_page.write("\t\t<link rel=\"stylesheet\" href=\"/CSS/FlagIt.css\"/>\n")

        #Setup script - for handlers
        html_page.write("\t\t<script type=\"text/javascript\" src=\"/Scripts/FlagIt.js\"></script>\n")
        if(chrome_build):
            html_page.write("\t\t<script type=\"text/javascript\" src=\"/Chrome_Polyfill/browser-polyfill.js\"></script>\n")
		
        html_page.write("\t</head>\n\n")
        #Body start
        html_page.write("\t<body>\n")
        html_page.write("\t\t<h2>{0}</h2>\n".format(dirname))
        html_page.write("\t\t<table id=\"flag-table\">\n")
        #Cell counter, after n cells create a new row
        counter = 1
        #Each image will be assigned a value, 1-248 used to help populate missing/found string
        total = 1

        #Generate table - flag for each region
        for flag in sorted(os.listdir("{0}/{1}/".format(master_directory, directory))):

            filename = flag
            region = os.path.splitext(flag)[0]

            #Check for apostrophes and escape
            if "\'" in region:
                region = region.replace("'", "\'") #Read up on escaping single quotes - tooltip not showing in FF
            if(counter == 1):
                html_page.write("\t\t\t<tr>\n")

            #Build html string

            #Setup opening <td> and class / id
            #Look into stringbuilder equivalent for python
            html_string  =  "\t\t\t\t\t<td class=\"missing\" id=\"{0}\">".format(region)

            #Inner img
            html_string += "<img id=\""
            html_string += str(total)
            html_string += "\" src=\"/flags/"
            html_string += dirname
            html_string += "/"
            html_string += filename
            html_string += "\" title=\""
            html_string += region
            html_string += "\"/>"

            #Close </td>
            html_string += "</td>\n"

            #Write to file
            html_page.write(html_string)

            if(counter > cells_per_row) or flag == sorted(os.listdir("{0}/{1}/".format(master_directory, directory)))[-1]:
                html_page.write("\t\t\t</tr>\n")
                counter = 0

            counter+=1
            total+=1

        html_page.write("\t\t</table>\n")

        #Hover text
        html_page.write("\t\t<p id=\"hover_text\">&nbsp;</p>")

        #Back
        if (dirname != "World Flags"):
            html_page.write("\n\t\t<p><a class=\"back\" href={0}_Contents.html>Back</a></p>".format(firstchar))
        else:
            html_page.write("\n\t\t<p><a class=\"back\" href=/Window/FlagIt.html>Back</a></p>")

        #Setup script - initialises setup defined in FlagIt.js
        #Will need to be generated alongside HTML
        html_page.write("\n\t\t<script type=\"text/javascript\" src=\"/Scripts/{0}.js\"></script>\n".format(dirname))

        #Body end
        html_page.write("\t</body>\n\n")

        #Page end
        html_page.write("</html>")

        #Write JS initialisation script
        #Write to html file

        with open("Scripts/{0}.js".format(dirname), mode="w+", encoding="utf-8") as js_script:
            js_script.write("init_setup(\"{0}\", {1});".format(dirname, total))


#Build content pages
start_char = "a"


#Build front page
with open("Window/FlagIt.html", mode="w+", encoding="utf-8") as main_page:
    main_page.write("<!DOCTYPE html>")
    main_page.write("\n<html>")
    main_page.write("\n\n\t<head>")
    main_page.write("\n\t\t<meta charset=\"UTF-8\">")
    main_page.write("\n\t\t<link rel=\"stylesheet\" href=\"/CSS/FlagIt.css\"/>")
    main_page.write("\n\t</head>")
    main_page.write("\n\n\t<body>")
    main_page.write("\n\t\t<h2>FlagIt - Flag Checklist</h2>")

    main_page.write("\n\t\t<h3>Flags of the World</h3>")
    main_page.write("\n\t\t<a href=\"/Pages/World Flags.html\">World Flags</a>")

    main_page.write("\n\t\t<h3>Country Regions</h3>\n")
    main_page.write("\t\t<p>")



    for a in range(0, 26):

        with open("Pages/{0}_Contents.html".format(start_char.upper()), mode="w+", encoding="utf-8") as contents_page:
            contents_page.write("<!DOCTYPE html>")
            contents_page.write("\n<html>")
            contents_page.write("\n\n\t<head>")
            contents_page.write("\n\t\t<meta charset=\"UTF-8\">")
            contents_page.write("\n\t\t<link rel=\"stylesheet\" href=\"/CSS/FlagIt.css\"/>")
            contents_page.write("\n\t</head>")
            contents_page.write("\n\n\t<body>")
            contents_page.write("\n\t\t<h2>{0} - Countries</h2>".format(start_char.upper()))
            contents_page.write("\n\t\t<ul>")

            for country in country_dict[start_char]:
                contents_page.write("\n\t\t\t<li><a href=\"/Pages/{0}.html\">{0}</a></li>".format(country))

            contents_page.write("\n\t\t</ul>")
            contents_page.write("\n\t\t<a class=\"back\" href=\"/Window/FlagIt.html\">Back</a>")
            contents_page.write("\n\t</body>")
            contents_page.write("\n\n</html>")
            main_page.write("\n\t\t\t<a href=\"/Pages/{0}_Contents.html\">{0}</a>".format(start_char.upper()))

        start_char = chr(ord(start_char) + 1)

    main_page.write("\n\t\t</p>")
    main_page.write("\n\t</body>")
    main_page.write("\n\n</html>")

#Build World Flags Page
