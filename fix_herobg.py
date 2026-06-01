import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  '.hero {',
  '.hero {\n  background-image: url("img/hero-bg.png");\n  background-size: cover;\n  background-position: center top;'
)
open(path, 'w').write(h)
print('Hero BG OK')
