# https://moz.com/ugc/how-i-built-an-online-community-from-0-to-1500-members
import requests
import re

url = raw_input("Enter URL to check: ")
keyword = raw_input("Enter Keyword to check: ")

#check if the keyword is in Title, Meta Description, H1, alt tag, image name.


def get_title(page_url):
  try:
    title = re.findall('<title>\n?(.+)\n?<\/title>', page_url)[0]
  except:
    return "Some error with title"
    pass
  return title

def get_meta_description(page_url):
  try:
    description = re.findall('name="description"\scontent="(.+)"', page_url)[0]
   
  except:
    return "Some error retrieving description"
    pass
  return description

def get_h1(page_url):
  try:
    h1 = re.findall('h1.+>(.+)<\/h1', page_url)[0]
  except:
    return "h1 not found"
    pass
  return h1


def get_alt(page_url):
  try:
    alt = re.findall('alt="(.+)">', page_url)
  except:
    return "alt not found"
    pass
  return alt

def get_image_name(page_url):
  try:
    img_name = re.findall('img.+?src="(.+)"\s', page_url)
  except:
    return "img not found"
    pass
  return img_name

def check_occurence(keyword, *args):
  global counter
  counter = 0
  try:
    
    if keyword in retrieved_title.lower():
      counter += 20
    
    if keyword in retrieved_meta_description.lower():
      counter += 20

    if keyword in retrieved_h1.lower():
      counter += 20
    
    if any(keyword in i.lower() for i in retrieved_alts):
      counter += 20
    
    if any(keyword in z.lower() for z in retrieved_image_names):
      counter += 20
      
  
  except:
    pass
  print "Onsite optimization for '{0}': {1}".format(keyword, counter) + '%' 
  return counter

result = requests.get(url).text

print '\n'
retrieved_title = get_title(result)
retrieved_meta_description = get_meta_description(result)
retrieved_h1 = get_h1(result)
retrieved_alts = get_alt(result)
retrieved_image_names = get_image_name(result)

check_occurence(keyword, retrieved_title, retrieved_meta_description, retrieved_h1, retrieved_alts, retrieved_image_names)

