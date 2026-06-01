import os, re
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
# Reemplazar cualquier src que empiece con data:
h = re.sub(r'src="data:image/[a-zA-Z]+;base64,[^"]*"', 'src="img/logo.png"', h)
open(path, 'w').write(h)
print('Logo fixed:', h.count('img/logo.png'), 'reemplazos')
