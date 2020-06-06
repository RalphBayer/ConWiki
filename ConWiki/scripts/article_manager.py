import json
import os
import markup_lexer

def create_n_save_article(json_data):
    """
        Creates a JSON file filled with the original text form the user
        and generated html for that text.

        I.E:
            # HEADING 1
            ## Sub heading 1
            ## Sub heading 2

            becomes

            <p>
                <h1> HEADING 1 </h1>
                <h2> Sub heading 1 </h2>
                <h2> Sub heading 2 </h2>
            </p>
    """

    # Generate the html.
    lexer     = markup_lexer.Lexer()
    main_html = lexer.generate_html(lexer.get_tokens(json_data['main']))
    side_html = lexer.generate_html(lexer.get_tokens(json_data['side_text']))

    # Open a file or create one if it doens't already exist.
    cwd = os.getcwd().replace('\\','/')

    # Create the folder articles if it doesn't exit.
    if not os.path.exists(f'{cwd}/articles'):
        os.mkdir(f'{cwd}/articles')

    location = f'{cwd}/articles/{json_data["title"].replace(" ", "_")}.json'

    # JSON dump the data.
    file = open(location, 'w+')
    data = {'data': {'markup':json_data, 'html':{'main_html':main_html, 'side_html':side_html}}}

    json.dump(data, file)
    file.close()


def find_article(file_name):
    # Get the current working directory.
    cwd = os.getcwd().replace('\\', '/')

    # Return error if we can't find the articles folder.
    if os.path.exists(f'{cwd}/articles'):
        location = f'{cwd}/articles/{file_name.replace(" ", "_")}.json'

        # Try to find the file
        if os.path.exists(location):
            file = open(location, 'r')
            return json.load(file)

        else:
            return f'<h1> ConWiki can\'t find the article {file_name}. Try creating it!'
    else:
        return '<h1> ConWiki can\'t find any articles. Try creating some! </h1>'
