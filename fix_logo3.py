import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
# Buscar desde src=" hasta el onerror
import re
h = re.sub(r'src="[^"]{500,}"', 'src="img/logo.png"', h)
open(path, 'w').write(h)
print('reemplazos:', h.count('img/logo.png'))
