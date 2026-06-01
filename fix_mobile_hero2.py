import os, re
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
# Eliminar cualquier background-image del hero en media queries
h = re.sub(r'background-image:\s*url\(img/hero-bg\.png\);?\s*\n?\s*background-size:\s*cover;\s*\n?\s*background-position:[^;]+;', '', h)
open(path, 'w').write(h)
print('OK')
