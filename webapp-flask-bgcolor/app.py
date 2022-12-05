from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

# Get color from Environment variable
HEX_COLOR_FROM_ENV = os.environ.get("APP_HEX_COLOR")
# Generate a random color
HEX_COLOR = '#' + hex(random.randint(0, 2 ** 24))  # 2 ** 24 due to 3 byte hex string
# Get dynamic title from Environment variable
TITLE_FROM_ENV = os.environ.get('APP_TITLE')
# Set default title
TITLE = "Cloud Computing - University of West Attica"

@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), color=HEX_COLOR, title=TITLE)


if __name__ == "__main__":
    print("This is a simple flask webapp that displays a colored background and a greeting message. \n"
          "The color can be specified in two different ways: \n"
          "    1. As a command line argument with --hex-color as the argument.\n"
          "    2. As an Environment variable APP_HEX_COLOR.\n"
          "In any other case, a random color is picked.\n"
          "\n"
          "Note 1: Color can be specified as a 3-byte hexadecimal number prefixed with the character '#'. \n"
          "Note 2: Command line argument precedes over environment variable.\n"
          "\n"
          "")


    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--hex-color', required=False, type=str)
    # Check for Command Line Parameters for title
    parser.add_argument('--title', required=False)
    args = parser.parse_args()

    if args.hex_color:
        print("Color from command line argument =" + args.hex_color)
        HEX_COLOR = args.hex_color
        if HEX_COLOR_FROM_ENV:
            print("A color was set through environment variable -" + HEX_COLOR_FROM_ENV + ". However, color from command line argument takes precendence.")
    elif HEX_COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + HEX_COLOR_FROM_ENV)
        HEX_COLOR = HEX_COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + HEX_COLOR)

    if args.title:
        print("Title from command line argument =" + args.title)
        TITLE = args.title
        if TITLE_FROM_ENV:
            print("A title was set through environment variable -" + TITLE_FROM_ENV + ". However, title from command line argument takes precendence.")
    elif TITLE_FROM_ENV:
        print("No Command line argument. Title from environment variable =" + TITLE_FROM_ENV)
        TITLE = TITLE_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a default title =" + TITLE)


    # Run Flask Application
    app.run(host="0.0.0.0", port=8000)
