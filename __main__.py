import sys
import json

from invcard.formats import get_format

def main():

    jsonfile = sys.argv[1]

    with open(jsonfile) as f:
        data = json.load(f)

    for box in data:
        get_format(box["format"])(box["name"], box["number"], box["content"]).generate()

if __name__ == "__main__":
    main()