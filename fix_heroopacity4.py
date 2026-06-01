import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  'linear-gradient(160deg, rgba(8,0,8,0.25) 0%, rgba(30,0,10,0.20) 40%, rgba(8,0,8,0.30) 100%);',
  'linear-gradient(160deg, rgba(8,0,8,0.05) 0%, rgba(30,0,10,0.05) 40%, rgba(8,0,8,0.10) 100%);'
)
open(path, 'w').write(h)
print('OK')
