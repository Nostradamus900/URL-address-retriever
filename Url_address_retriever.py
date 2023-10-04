import re

file_path = input('Please enter html file path here: ')
with open(file_path) as html:
    content = html.read()
    url_matches = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)
    cleaned_url = list(dict.fromkeys(url_matches))
    
print('\nFound URL........................\n\n','\n '.join(cleaned_url))
print('\nEOF..............................')
