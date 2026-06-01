import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  '  .hero {\n  background-image: url("img/hero-bg.png");\n  background-size: cover;\n  background-position: center top; padding:84px 16px 50px; }',
  '  .hero { padding:84px 16px 50px; }'
)
open(path, 'w').write(h)
print('OK')
