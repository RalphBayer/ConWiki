import json
import os

def create_article(json_data):
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

    # Generate the html
    lexer     = Lexer()
    text_html = lexer.generate_html(lexer.get_tokens(json_data["text"]))
    side_html = lexer.generate_html(lexer.get_tokens(json_data["text_sidebar"]))

    # Open a file or create one if it doens't already exist
    cwd      = os.getcwd().replace('\\','/')

    if not os.path.exists(f"{cwd}/articles"):
        os.mkdir(f"{cwd}/articles")

    location = f"{cwd}/articles/{json_data['title'].replace(' ', '_')}.json"

    # JSON dump the data
    file = open(location, "w+")
    json.dump(json_data, file)
    json.dump({"text":text_html, "text_sidebar":side_html}, file)
    file.close()

class Lexer:
    """
        The Lexer class takes a string as data and can find all markup language
        tokens such as '#' and '*'.

        The Lexer class can also take those tokens and generate valid HTML.
    """

    def get_tokens(self, data):
        """
            Finds all the markup tokens.
        """

        counter = 0
        current = ""
        tokens  = []

        while counter < len(data):
            current += data[counter]

            # We have encountered a header.
            if current[-1] == "#":
                tokens.append(["HEADER", "#"])
                current = ""

            # We have encountered plain text and line break.
            elif current[-1] == "\n":
                tokens.append(["TEXT", current[0:len(current)-1]])
                tokens.append(["BREAK", "br"])
                current = ""

            elif counter == len(data) - 1:
                tokens.append(["TEXT", current])
                current = ""

            counter += 1

        return self.add_liketerms(tokens)

    def add_liketerms(self, tokens):
        """
            Joins certain tokens together like '#' and '*'.
            for example # would be <h1> but ## would be <h2>
        """

        joined_tokens = []
        prev_token    = ""

        for token in tokens:
            if token[0] == "HEADER":
                if prev_token == "HEADER":
                    joined_tokens[-1][1] += 1
                else:
                    joined_tokens.append(["HEADER", 1])
                    prev_token = "HEADER"

            else:
                joined_tokens.append(token)
                prev_token = token[0]

        return joined_tokens

    def generate_html(self, tokens):
        """
            generates and returns valid HTML
        """

        counter  = 0
        gen_html = "<p>"

        while counter < len(tokens):
            token = tokens[counter]

            if token[0] == "TEXT":
                gen_html += token[1]

            elif token[0] == "BREAK":
                gen_html += "<br>"

            elif token[0] == "HEADER":
                text = f"<h{token[1]}> {tokens[counter+1][1]} </h{token[1]}>"
                gen_html += text
                counter += 1 # SKIP THE TEXT WE ARE ENCOUNTERING NEXT

            counter += 1

        gen_html += "</p>"

        return gen_html
