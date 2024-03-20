use std::env;
use std::fs;

fn remove_duplicate_posts(html_file_addr: &str, issue_number: &str) {
    // Python code here
}

fn add_section_to_html(html_file_addr: &str, new_section_html: &str) {
    // Python code here
}

fn remove_oldest_section(html_file_addr: &str) {
    // Python code here
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let issue_number = &args[1];
    let post_title = &args[2];
    let post_author = &args[3];
    let post_content = &args[4];
    let post_created_date = &args[5];

    let url = "https://nimafanniasl.github.io/GithubForum/posts/";

    let minified_post_content = format!("{}{}", &post_content[..70], "...");

    let recent_html = "recent.html";
    let template_file_path = "templates/section.html";

    let template_file_str = fs::read_to_string(template_file_path)
    .expect("Should have been able to read the file :(");

    let new_section_html = template_file_str.replace("{POST-TITLE}", &post_title);
    let new_section_html = new_section_html.replace("{POST-AUTHOR}", &post_author);
    let new_section_html = new_section_html.replace("{POST-DATE}", &post_created_date);
    let new_section_html = new_section_html.replace("{POST-NUMBER}", &issue_number);
    let new_section_html = new_section_html.replace("{MINIFIED-POST-CONTENT}", &minified_post_content);
    let new_section_html = new_section_html.replace("{POST-PAGE-LINK}", format!("{}{}.html", &url, &issue_number).as_str());

}