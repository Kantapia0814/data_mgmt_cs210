import re
# problem 1
# 1-1
str1 = "I am fine? Really?"
fil1 = re.sub(r'\?', r'?!', str1)
print(fil1)
# 1-2
str2 = "Hello world"
fil2 = re.sub(r'^(.).+(.)$', r'\1###\2', str2)
print(fil2)
# 1-3
str3 = "apple|banana"
fil3 = re.sub(r'(.+)\|(.+)', r'\2;\1', str3)
print(fil3)

# problem 2
# 2-1
str4 = "19100 COM Networks 19101 MAT Calculus 19102 MAT Algebra 19103 BIO Microbiology"
id_filter = r'\d{5}'
code_filter = r'[A-Z]{3}'
coures_filter = r'[A-Z][a-z]{3,}'

print(re.findall(id_filter, str4))
print(re.findall(code_filter, str4))
print(re.findall(coures_filter, str4))

# 2-2
tuple_filter = r'(\d{5})\s([A-Z]{3})\s([A-Z][a-z]{3,})'
result = re.findall(tuple_filter, str4)
print(result)

# problem 3
str5 ='<a href="https://www.foxnews.com/politics/">Fox News</a>'
pattern = r'href="https?://(?:www\.)?([^/]+)[^"]*">(.+)</a>'
match = re.search(pattern, str5)
if match:
    domain = match.group(1)
    linkname = match.group(2)
    print("domain:", domain)
    print("linkname:", linkname)

tup1 = re.findall(pattern, str5)
if tup1:
    print("domain:", tup1[0][0])
    print("linkname:", tup1[0][1])

# problem 4
str6 = "<html><body><h1><div><h2>Responsive Sidebar Example</h2><title><p>First paragraph.</p></ol><p>Second paragraph.</p></li><h3>Resize the browser window to see the effect.</h3></div></body></html>"
opening_tag = r'<([^/>]+)>'
closing_tag = r'</([^>]+)>'
open_lst = re.findall(opening_tag, str6)
close_lst = re.findall(closing_tag, str6)

open_set = set(open_lst)
close_set = set(close_lst)

unclosed_open_tags = open_set - close_set
unopened_close_tags = close_set - open_set

print("Opening tags:", sorted(set(f"<{tag}>" for tag in open_lst)))
print("Closing tags:", sorted(set(f"</{tag}>" for tag in close_lst)))
print("Unclosed opening tags:", sorted(f"<{tag}>" for tag in unclosed_open_tags))
print("Unopened closing tags:", sorted(f"</{tag}>" for tag in unopened_close_tags))
