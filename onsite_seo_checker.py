# https://moz.com/ugc/how-i-built-an-online-community-from-0-to-1500-members

import pandas as pd
import numpy as np
import requests
import re
from onsite_optimization import get_title, get_meta_description, get_h1, get_alt, get_image_name, check_occurence

url = raw_input("Enter URL to check: ")
keyword = raw_input("Enter Keyword to check: ")

#check if the keyword is in Title, Meta Description, H1, alt tag, image name.




result = requests.get(url).text


print '\n'
retrieved_title = get_title(result)
retrieved_meta_description = get_meta_description(result)
retrieved_h1 = get_h1(result)
retrieved_alts = get_alt(result)
retrieved_image_names = get_image_name(result)

check_occurence(keyword, retrieved_title, retrieved_meta_description, retrieved_h1, retrieved_alts, retrieved_image_names)
#check_occurence(keyword, retrieved_title, retrieved_meta_description)
