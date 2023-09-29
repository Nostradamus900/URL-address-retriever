import re

file_path = input('Please enter html file path here: ')
with open(file_path) as html:
    content = html.read()
    url_matches = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)
    cleaned_list = list(dict.fromkeys(url_matches))
    url_matches = ','.join(url_matches)
    
print('\n'.join(cleaned_list))
