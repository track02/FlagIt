#Given a folder containing a flag_list.txt file and associated images
#Produce a HTML table with each cell holding a flag image
#
import sys;
import os;

#Vars
cells_per_row = 19;
master_directory = sys.argv[1]; #Second parameter is directory to process

with open("Window/FlagIt.html", mode="w+", encoding="utf-8") as main_page:


	main_page.write("<!DOCTYPE html>")
	main_page.write("\n<html>")
	main_page.write("\n\t<head>")
	main_page.write("\n\t\t<meta charset=\"UTF-8\">")
	main_page.write("\n\t\t<link rel=\"stylesheet\" href=\"/CSS/FlagIt.css\"/>")		
	main_page.write("n\t</head>")

	main_page.write("\n\n\t<body>")
	main_page.write("\n\t\t<ol>")
	


	for directory in os.listdir(master_directory):
		
		dirname = os.path.split(directory)[1]
		total = 0

		#Write to html file
		with open("Pages/{0}.html".format(dirname), mode="w+", encoding="utf-8") as html_page:

			#Doc
			html_page.write("<!DOCTYPE html>\n")

			#Head
			html_page.write("<html>\n")
			html_page.write("\t<head>\n")
			html_page.write("\t\t<meta charset=\"UTF-8\">\n")
			html_page.write("\t\t<link rel=\"stylesheet\" href=\"/CSS/FlagIt.css\"/>\n")
			html_page.write("\t\t<script type=\"application/javascript\" src=\"/Scripts/browser-polyfill.js\"></script>\n")
			#Setup script - for handlers
			html_page.write("\t\t<script type=\"text/javascript\" src=\"/Scripts/FlagIt.js\"></script>\n\n")
			html_page.write("\t</head>\n\n")
			#Body start
			html_page.write("\t<body>\n\n")
			html_page.write("\t\t<table id=\"flag-table\">\n")
			#Cell counter, after 5 cells create a new row
			counter = 1
			#Each image will be assigned a value, 1-248 used to help populate missing/found string
			total = 1

			#Generate table
			for flag in os.listdir("{0}\\{1}\\".format(master_directory, directory)):
				
				#print(flag)
				filename = flag
				countryname = os.path.splitext(flag)[0]

				#Check for apostrophes and escape
				if "\'" in countryname:
					countryname = countryname.replace("'", "\'") #Read up on escaping single quotes - tooltip not showing in FF
				if(counter == 1):
					html_page.write("\t\t\t<tr>\n")

				#Build html string

				#Setup opening <td> and class / id
				#Look into stringbuilder equivalent for python
				html_string  =  "\t\t\t\t\t<td class=\"missing\" id=\"{0}\">".format(countryname)

				#Inner img
				html_string += "<img id=\""
				html_string += str(total)
				html_string += "\" src=\"/flags/"
				html_string += dirname
				html_string += "/"
				html_string += filename
				html_string += "\" title=\""
				html_string += countryname
				html_string += "\"/>"

				#Close </td>
				html_string += "</td>\n"

				#Write to file
				html_page.write(html_string)

				if(counter > cells_per_row) or flag == os.listdir("{0}\\{1}\\".format(master_directory, directory))[-1]:
					html_page.write("\t\t\t</tr>\n")
					counter = 0

				counter+=1
				total+=1

			html_page.write("\t\t</table>\n\n")

			#Hover text
			html_page.write("<p id=\"hover_text\"> </p>")

			#Setup script - initialises setup defined in FlagIt.js
			#Will need to be generated alongside HTML
			html_page.write("\t\t<script type=\"text/javascript\" src=\"/Scripts/{0}.js\"></script>\n\n".format(dirname))

			#Body end
			html_page.write("\t</body>\n\n")

			#Page end
			html_page.write("</html>")

			#Write JS initialisation script
			#Write to html file
			
		with open("Scripts/{0}.js".format(dirname), mode="w+", encoding="utf-8") as js_script:
			js_script.write("init_setup(\"{0}\", {1})".format(dirname, total));

		main_page.write("\n\t\t\t<li><a href=\"/Pages/{0}.html\">{1}</a></li>".format(dirname, dirname))
	
	main_page.write("\n\t\t</ol>")
	main_page.write("\n\n\t</body>")
	main_page.write("\n</html>")
	