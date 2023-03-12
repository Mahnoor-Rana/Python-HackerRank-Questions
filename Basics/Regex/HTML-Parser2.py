# You are given an HTML code snippet of N lines.
# Your task is to print the single-line comments, multi-line comments and the data.


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):    
    def handle_comment(self, data):
        prefix = 'Multi' if '\n' in data else 'Single' 
        print(f">>> {prefix}-line Comment", data, sep="\n")
    
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data", data, sep="\n")

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()