import os
import sys
from datetime import datetime
from includes import *

# Template for the HTML file
template_file_path = "templates/posttemplate.html"

with open(template_file_path, "r") as template_file:
    template = template_file.read()

# Replace placeholders with actual data
issue_number = sys.argv[1]
post_title = sys.argv[2]
post_author = sys.argv[3]
post_content = convert_md_to_html(sys.argv[4])

pfp_url = get_pfp(post_author)

html_content = template.replace("{POST-TITLE}", post_title)
html_content = html_content.replace("{POST-AUTHOR}", post_author)
html_content = html_content.replace("{POST-DATE}", datetime.now().strftime("%Y-%m-%d"))
html_content = html_content.replace("{POST-NUMBER}", issue_number)
html_content = html_content.replace("{POST-CONTENT}", post_content)
html_content = html_content.replace("{PFP-URL}", pfp_url)


# Define the output directory
output_directory = "posts"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Save the HTML content to a file
output_file_path = os.path.join(output_directory, f"{issue_number}.html")
with open(output_file_path, "w") as f:
    f.write(html_content)