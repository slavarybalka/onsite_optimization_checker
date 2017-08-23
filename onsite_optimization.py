import re




# retrieve page title
def get_title(page_url):

  title = re.findall('<title>[\n\s]*(.+)[\s\n]*<\/title>', page_url)[0]

  print title
  return title



# retrieve page meta description
def get_meta_description(page_url):
  try:
    description = re.findall('name="description"\scontent="([\s\S]+?)"', page_url)[0]
    
  except:
    return "Some error retrieving description"
    pass
  return description



# retrieve h1 tags
def get_h1(page_url):
  try:
    h1 = re.findall('<h1.+>(.+)<\/h1>', page_url)

  except:
    return "h1 not found"
    pass
  return h1


# retrieve image alt tags
def get_alt(page_url):
  try:
    alt = re.findall('alt="(.+?)"', page_url)
  except:
    return "alt not found"
    pass
  return alt



# retrieve image names
def get_image_name(page_url):
  try:
    img_name = re.findall('<img.+?src="(.+?)"', page_url)
  except:
    return "img not found"
    pass
  return img_name



# check if the keyword is found in the retrieved page elements
def check_occurence(keyword, retrieved_title, retrieved_meta_description, retrieved_h1, retrieved_alts, retrieved_image_names):
  global counter
  counter = 0


  # Check if keyword is in title
  if keyword in retrieved_title.lower():
    counter += 20
    print "Keyword found in title (exact match)", retrieved_title
    title_marker = 'yes'
  else:
    print "Keyword '{0}' not found in title: {1}".format(keyword, retrieved_title.strip())
    title_marker = 'no'

  # Check if keyword is in meta description
  if keyword in retrieved_meta_description.lower():
    counter += 20
    print "Keyword found in meta description (exact match)", retrieved_meta_description
    meta_desc_marker = 'yes'
  else:
    print "Keyword '{0}'' not found in meta description: {1}".format(keyword, retrieved_meta_description.strip())
    meta_desc_marker = 'no'

  # Check if keyword is in h1
  if retrieved_h1:
      
    if len(retrieved_h1) > 1:
      
      if any(keyword in b.lower().replace('-', ' ') for b in retrieved_h1):
        counter += 20
        print "Keyword found in h1 (exact match)", retrieved_h1
        h1_marker = 'yes'
      else:
        print "Keyword '{0}'' not found in h1: {1}".format(keyword, retrieved_h1)
        h1_marker = 'no'      
    if len(retrieved_h1) == 1:
      
      
      if keyword in retrieved_h1[0].lower().replace('-', ' '):
        counter += 20
        print "Keyword found in h1 (exact match)", retrieved_h1
        h1_marker = 'yes'
      else:
        print "Keyword '{0}'' not found in h1: {1}".format(keyword, retrieved_h1[0].strip()) 
        h1_marker = 'no'
  else:
    h1_marker = 'no'

  # Check if keyword is in image alt tags
  if retrieved_alts:

    if any(keyword in i.lower().replace('-', ' ').replace('_', ' ') for i in retrieved_alts):
      counter += 20
      print "Keyword found in image alt tags (exact match)"#, retrieved_alts
      img_alt_marker = 'yes'
    else:
      print "Keyword not in image alts."
      img_alt_marker = 'no'
   
  # Check if keyword is in image names  
  if retrieved_image_names:
    
    if any(keyword in z.lower().replace('-', ' ') for z in retrieved_image_names):
      counter += 20
      print "Keyword found in image name (exact match)"#, retrieved_image_names
      img_name_marker = 'yes'
    else:
      print "Keyword not in image names."
      img_name_marker = 'no'


  

  outt = "Onsite optimization for '{0}': {1}".format(keyword, counter) + '%\n' 
  print outt
  return [outt, counter, title_marker, meta_desc_marker, h1_marker, img_name_marker, img_alt_marker]




