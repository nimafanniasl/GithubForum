import markdown2
import json
import requests

def convert_md_to_html(md_text):
    return markdown2.markdown(md_text)

def get_pfp(user):
    return json.loads(requests.get(f"https://api.github.com/users/{user}").text)["avatar_url"]