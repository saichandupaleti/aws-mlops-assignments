def generate_files_list_html(files):
    """
    Generates an HTML list from a list of file names.
    """
    files_list_html = "<ul>"
    for file in files:
        files_list_html += f"<li>{file}</li>"
    files_list_html += "</ul>"
    return files_list_html
