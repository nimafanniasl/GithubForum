import sys
from bs4 import BeautifulSoup


html_file = "recent.html"
issue_number = sys.argv[1]

with open("recent.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

main_tag = soup.find('main')
if main_tag:
    sections = main_tag.find_all('section')

    for section in sections:
        if section.get('id') == str(issue_number):
            section.decompose()

with open(html_file, 'w') as file:
    file.write(str(soup))