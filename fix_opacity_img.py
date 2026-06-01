import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace('opacity: 0.18;', 'opacity: 0.12;')
open(path, 'w').write(h)
print('OK')
