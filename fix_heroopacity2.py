import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  'rgba(8,0,8,0.75) 0%, rgba(30,0,10,0.70) 40%, rgba(8,0,8,0.97)',
  'rgba(8,0,8,0.45) 0%, rgba(30,0,10,0.40) 40%, rgba(8,0,8,0.55)'
)
h = h.replace(
  'rgba(204,0,32,0.28) 0%, transparent 65%',
  'rgba(204,0,32,0.12) 0%, transparent 65%'
)
open(path, 'w').write(h)
print('OK')
