import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  '.hero {\n  background-image: url("img/hero-bg.png");\n  background-size: cover;\n  background-position: center top;',
  '.hero {\n  background-image: url("img/hero-bg.png");\n  background-size: cover;\n  background-position: center top;'
)
# Bajar opacidad del overlay
h = h.replace(
  'rgba(8,0,8,0.97) 0%, rgba(30,0,10,0.92)',
  'rgba(8,0,8,0.75) 0%, rgba(30,0,10,0.70)'
)
open(path, 'w').write(h)
print('OK')
