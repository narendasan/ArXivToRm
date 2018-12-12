#!/usr/local/bin/python3

import arxiv
import argparse
from subprocess import call
def is_arxiv_code(code):
    if ".pdf" in code:
        return False
    return True

def to_slug(title):
    # Remove special characters
    filename = ''.join(c if c.isalnum() else '_' for c in title)
    # delete duplicate underscores
    filename = '_'.join(list(filter(None, filename.split('_'))))
    return filename

def main():
    parser = argparse.ArgumentParser(description='Paper to transfer to Remarkable')
    parser.add_argument('paper', type=str, help='ArVix code or path to file')

    ARGS = parser.parse_args()

    path = ARGS.paper 
    if is_arxiv_code(ARGS.paper):
        paper = arxiv.query(id_list=[ARGS.paper])[0]
        arxiv.download(paper, "/tmp/", False, True)
        print("Adding " + paper.title + " to Remarkable")
        path = "/tmp/" +  to_slug(paper.title) + ".pdf"

    call(["rmapi", "put", path])    

if __name__ == "__main__":
    main()