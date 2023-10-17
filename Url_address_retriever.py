import re
while True:

    try:
        file_path = str(input('Please enter file path here: '))
        with open(file_path) as html:
            content = html.read()
            url_matches = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)
            cleaned_url = list(dict.fromkeys(url_matches))

    except FileNotFoundError as err:
        print('File does not exist')

    else:
        print('\nFound URL...................\n\n','\n '.join(cleaned_url))
        print('\nEOF.........................')
        break
