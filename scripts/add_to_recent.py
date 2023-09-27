import sys
from datetime import datetime
from bs4 import BeautifulSoup

def add_section_to_html(html_file, new_section_html):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    main_tag = soup.find('main')

    if main_tag:
        # Create a new section and add it to the top of the main element
        new_section = BeautifulSoup(new_section_html, 'html.parser')
        main_tag.insert(0, new_section)

    with open(html_file, 'w') as file:
        file.write(str(soup))

def remove_oldest_section(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    main_tag = soup.find('main')
    if main_tag:
        sections = main_tag.find_all('section')

        if len(sections) > 10:
            # Remove the oldest section (last one in the list)
            sections[-1].decompose()

    with open(html_file, 'w') as file:
        file.write(str(soup))

def remove_duplicate_posts(html_file, issue_number):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    main_tag = soup.find('main')
    if main_tag:
        sections = main_tag.find_all('section')

        for section in sections:
            if section.get('id') == str(issue_number):
                section.decompose()

    with open(html_file, 'w') as file:
        file.write(str(soup))

if __name__ == "__main__":
    issue_number = sys.argv[1]
    post_title = sys.argv[2]
    post_author = sys.argv[3]
    post_content = sys.argv[4]

    post_content = "".join(post_content[:70]) + "..."
    print(post_content)

    recent_html = "recent.html"

    with open("templates/section.html", "r") as section_template:
        new_section_html = section_template.read()

    new_section_html = new_section_html.replace("{POST-TITLE}", post_title)
    new_section_html = new_section_html.replace("{POST-AUTHOR}", post_author)
    new_section_html = new_section_html.replace("{POST-DATE}", datetime.now().strftime("%Y-%m-%d"))
    new_section_html = new_section_html.replace("{POST-NUMBER}", issue_number)
    new_section_html = new_section_html.replace("{MINIFIED-POST-CONTENT}", post_content)
    new_section_html = new_section_html.replace("{POST-PAGE-LINK}", f"https://nimafanniasl.github.io/GithubForum/posts/{issue_number}.html")

    # Remove suplicate post
    remove_duplicate_posts(recent_html, issue_number)

    # Add the new section to the HTML file
    add_section_to_html(recent_html, new_section_html)

    # Remove the oldest section if there are more than 10 sections
    remove_oldest_section(recent_html)
