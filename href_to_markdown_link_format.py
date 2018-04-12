import re

f = open('README.md')
data = f.readlines()

link_regex = re.compile('".+"')
content_regex = re.compile('>.+<')

for idx, line in enumerate(data):
    if 'a href' in line:
        link = link_regex.findall(line)[0][1:-1]
        content = content_regex.findall(line)[0][1:-1]
        new_line = '- [{}]({})\n'.format(content, link)
        data[idx] = new_line

f.close()

f = open('README.md', 'w')
for line in data:
    f.write(line)

f.close()