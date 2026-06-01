import os, re
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
f = open(path, 'r')
h = f.read()
f.close()
# Reemplazar el src base64 del hero por img/logo.png
h = re.sub(r'src="data:image/[^"]*"', 'src="img/logo.png"', h)
open(path, 'w').write(h)
print('Logo OK')
