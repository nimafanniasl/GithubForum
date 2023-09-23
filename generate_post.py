import os
import sys
from datetime import datetime

# Template for the HTML file
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/styles.css">
    <title>Example Post</title>
</head>
<body>
    <header>
        <h1>GithubForum</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="recent.html">Recent Posts</a></li>
                <li><a href="categories.html">Categories</a></li>
                <li><a href="posting.html">Post a new topic</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="post">
            <h2>{POST-TITLE}</h2>
            <p>{POST-AUTHOR} | Date: {POST-DATE} | Post #{POST-NUMBER}</p> <!--POST-Number is the issue number in github, for example #23-->
            <p dir="auto">{POST-CONTENT}</p>
            <!-- Add post content here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 GithubForum</p>
    </footer>
</body>
</html>
"""

# Replace placeholders with actual data
issue_number = sys.argv[1]
post_title = sys.argv[2]
post_author = sys.argv[3]
post_content = sys.argv[4]

html_content = template.replace("{POST-TITLE}", post_title)
html_content = html_content.replace("{POST-AUTHOR}", post_author)
html_content = html_content.replace("{POST-DATE}", datetime.now().strftime("%Y-%m-%d"))
html_content = html_content.replace("{POST-NUMBER}", issue_number)
html_content = html_content.replace("{POST-CONTENT}", post_content)


# Define the output directory
output_directory = "posts"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Save the HTML content to a file
output_file_path = os.path.join(output_directory, f"{issue_number}.html")
with open(output_file_path, "w") as f:
    f.write(html_content)
