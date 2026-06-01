import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
# Agrandar el círculo del hero
h = h.replace('width: 150px; height: 150px;', 'width: 220px; height: 220px;')
open(path, 'w').write(h)
print('OK')
