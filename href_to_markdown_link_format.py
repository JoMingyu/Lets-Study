f = open('README.md')
data = f.readlines()

for idx, line in enumerate(data):
    if 'a href' in line:
        import re
        link = re.findall('".+"', line)[0][1:-1]
        content = re.findall('>.+<', line)[0][1:-1]
        new_line = '- [{}]({})\n'.format(content, link)
        data[idx] = new_line

f.close()

f = open('README.md', 'w')
for line in data:
    f.write(line)

f.close()