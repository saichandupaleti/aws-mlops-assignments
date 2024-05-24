def generate_files_list_html(files):
    """
    Generates an HTML unordered list from a list of file names.

    This function takes a list of file names and constructs a string
    that represents an HTML unordered list, with each file name
    wrapped in `<li>` tags.

    Parameters:
    files (list of str): A list of file names to be included in the HTML list.

    Returns:
    str: An HTML string containing the list of file names.
    """
    files_list_html = "<ul>"
    for file in files:
        files_list_html += f"<li>{file}</li>"
    files_list_html += "</ul>"
    return files_list_html
