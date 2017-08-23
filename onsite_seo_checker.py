import pandas as pd
import numpy as np
import requests
import csv
import re
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from onsite_optimization import get_title, get_meta_description, get_h1, get_alt, get_image_name, check_occurence

list_of_programs = open("program_pages1", 'r').readlines()
export_list = []
final_export_list = []

all_programs = len(list_of_programs)
cnter = 0

for program in list_of_programs:
	try:
		probe = "http://api.semrush.com/?type=url_organic&key={Insert your API key here}&display_limit=100&export_columns=Ph,Po,Nq,Cp,Co,Tr,Tc,Nr,Td&url=" + program.strip() + "&database=us"

		cnter += 1
		print "Checking program page {0} of {1}".format(cnter, all_programs)

		#print probe
		print program

		semrush = requests.get(probe)
		for line in semrush.text.split("\n")[1:]:

			#print line
			#print program
			#export_list.append(line)
			x = line.split(';')
			#export_list.append(x)
			line_1 = [program, x[0], x[1], x[2]]
			
			export_list.append([program.strip(), x[0], x[1], x[2]])
	    	
	except:
		print "ERROR WHEN QUERYING SEMRUSH"
		pass


		

	
#print export_list

for item in export_list:
	#print item
	if int(item[2]) > 10 and int(item[2]) < 21:
		print item
		url = item[0]
		keyword = item[1]



		#check if the keyword is in Title, Meta Description, H1, alt tag, image name.
		print url
		result = requests.get(url).text.lower()
		#print result

		print '\n'
		retrieved_title = get_title(result)
		retrieved_meta_description = get_meta_description(result)
		retrieved_h1 = get_h1(result)
		retrieved_alts = get_alt(result)
		retrieved_image_names = get_image_name(result)

		z = check_occurence(keyword, retrieved_title, retrieved_meta_description, retrieved_h1, retrieved_alts, retrieved_image_names)
		print z
		final_export_list.append([url, keyword, item[2], item[3], str(z[1])+'%', z[2], z[3], z[4], z[5], z[6]])

for i in final_export_list:
	print i


with open('onsite_seo_results.csv', 'wb') as csvfile:
    x_writer = csv.writer(csvfile, delimiter=',')
    x_writer.writerow(['URL','Keyword','Position','Search Volume','Level of Optimization','KW in Title', 'KW in Meta Description', 'KW in h1', 'KW in Image Name', 'KW in Image Alts']) #writing headers
    for final_export_data in final_export_list:
    	#print export_data
        x_writer.writerow(final_export_data)

