"""
Py CURL by Alexander Abraham.
Licensed under the MIT license.
"""

import sys
import requests
from sys import argv
from requests import get

def download(url):
    """
    Downloads a file from an URL.
    """
    request = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as result:
        result.write(request.content)

def cli():
    """
    Command-line interface for Py CURL.
    """
    args = argv
    try:
        download(args[1])
    except Exception as error:
        print(str(error))
        sys.exit()

def main():
    """
    Main entry-point for the interpreter.
    """
    cli()

if __name__ == '__main__':
    """
    Run the tool when it is invoked as a stand-alone tool.
    """
    main()
