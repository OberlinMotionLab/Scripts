import os
import re
import sys

class Issue:
    def __init__(self,fname, title, tags):
        self.title = title
        self.tags = tags

    def __str__(self):
        retstr = "Title: " + self.title + "\nTags: "
        for tag in self.tags:
            retstr += tag + " "
        return retstr

def parse_todo_block(lines, delim, fname):
    issues = []
    for line in lines:
        stripped = line[:-1].replace(delim, '')
        title = " ".join([x for x in stripped.split() if x[0]!="@"])
        tags = [x for x in stripped.split() if x[0]=="@"]
        issues.append(Issue(fname, title, tags))
    for i in issues:
        print(i)

        
def parse_files(l):
    todo_re = re.compile(r'TODO|todo')
    for fname in l:
        try:
            with open(fname, 'r') as f:
                found = False
                todo_block = []
                for line in f:
                    if (not found) and todo_re.search(line):
                        # print("not found and re_search yes: "+line)
                        delim = line[0]
                        found = True
                    elif found and line[0] == delim:
                        # print("found and line[0] is delim"+" ".join(todo_block))
                        todo_block.append(line)
                    else:
                        parse_todo_block(todo_block, delim, fname)
                        break
        except IOError:
            print("No file: " + fname + " found.")
            
def main():
    args = sys.argv
    if len(args)<2:
        print("Error: no input file specified.\n")
        print("Usage: python3 issues.py <filename>")
    else:
        parse_files(args[1:])

main()
