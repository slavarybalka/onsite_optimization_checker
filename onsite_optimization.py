import re

def get_title(page_url):

  title = re.findall('<title>([\s\S]+)<\/title>', page_url)[0] 
  

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
    h1 = re.findall('<h1.?>([\s\S]+)<\/h1', page_url)

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

def check_occurence(keyword, retrieved_title, retrieved_meta_description, retrieved_h1, retrieved_alts, retrieved_image_names):
  global counter
  counter = 0

  try:
    if keyword in retrieved_title.lower():
      counter += 20
      print "Keyword found in title (exact match)"
      

    if keyword in retrieved_meta_description.lower():
      counter += 20
      print "Keyword found in meta description (exact match)"
      

    if retrieved_h1:   
      
      if any(keyword in b.lower().replace('-', ' ') for b in retrieved_h1):
        counter += 20
        print "Keyword found in h1 (exact match)"
      

    if retrieved_alts:

      if any(keyword in i.lower().replace('-', ' ').replace('_', ' ') for i in retrieved_alts):
        counter += 20
        print "Keyword found in image alt tags (exact match)"
      

    if retrieved_image_names:
      
      if any(keyword in z.lower().replace('-', ' ') for z in retrieved_image_names):
        counter += 20
        print "Keyword found in image name (exact match)"
      

  except: 
    print "Write something."    
  

  print "Onsite optimization for '{0}': {1}".format(keyword, counter) + '%' 
  return counter



