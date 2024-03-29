import sys
import os
from bs4 import BeautifulSoup
from datetime import datetime
from includes import *

mode = sys.argv[1]
issue_number = sys.argv[2]
post_author = sys.argv[3]
post_content = convert_md_to_html(sys.argv[4])


if mode.lower() == "add":
    posts_dir = "posts"
    issue_html = os.path.join(posts_dir, f"{issue_number}.html")

    with open("templates/comment.html", "r") as isuue_comment:
        isuue_comment_template = isuue_comment.read()

    isuue_comment_template = isuue_comment_template.replace("{POST-CONTENT}", post_content)
    isuue_comment_template = isuue_comment_template.replace("{POST-AUTHOR}", post_author)
    isuue_comment_template = isuue_comment_template.replace("{POST-DATE}",
                                                            datetime.now().strftime("%Y-%m-%d"))

    # Read existing issue_html content and parse it with BeautifulSoup
    with open(issue_html, "r", encoding="utf-8") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")

    # Find the <main> section
    main_section = soup.find("main")

    # Append the modified isuue_comment_template to <main>
    main_section.append(BeautifulSoup(isuue_comment_template, "html.parser"))

    # Save the updated HTML back to issue_html
    with open(issue_html, "w", encoding="utf-8") as html_file:
        html_file.write(str(soup))