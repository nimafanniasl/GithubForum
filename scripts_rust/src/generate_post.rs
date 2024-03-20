use std::env;
use std::fs;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let args: Vec<String> = env::args().collect();

    let issue_number = &args[1];
    let post_title = &args[2];
    let post_author = &args[3];
    let post_content = &args[4];
    let post_created_date = &args[5];

    let template_file_path = "templates/posttemplate.html";

    let template_file = fs::read_to_string(template_file_path)
        .expect("Should have been able to read the file");

    let output_directory = "posts";


    let mut html_content = String::from(template_file);

    html_content = html_content.replace("{POST-TITLE}", &post_title);
    html_content = html_content.replace("{POST-AUTHOR}", &post_author);
    html_content = html_content.replace("{POST-DATE}", &post_created_date);
    html_content = html_content.replace("{POST-NUMBER}", &issue_number);
    html_content = html_content.replace("{POST-CONTENT}", &post_content);

    match fs::create_dir(&output_directory) {
        Ok(()) => println!("Dir created"),
        _ => println!("Dir already exists")
    }

    // Change the file creation and write operations as follows
    let mut file = File::create(format!("{}/{}.html", output_directory, issue_number))
    .expect("Failed to create file");

    file.write_all(html_content.as_bytes())
    .expect("Failed to write to file");


}