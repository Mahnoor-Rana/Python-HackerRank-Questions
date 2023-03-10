#You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if (len(attrs) > 0):
            for attr in attrs:
                print('->', attr[0], '>', attr[1])

parser = MyHTMLParser()
n=int(input())
for _ in range(n):
    parser.feed(input())