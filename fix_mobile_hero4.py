import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
lines = open(path, 'r').readlines()
new_lines = []
skip = 0
for i, line in enumerate(lines):
    if 'background-image: url("img/hero-bg.png")' in line:
        skip = 3  # saltar esta línea y las 2 siguientes (background-size y background-position)
    if skip > 0:
        skip -= 1
        continue
    new_lines.append(line)
open(path, 'w').write(''.join(new_lines))
print('OK')
