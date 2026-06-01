import os, re
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()

# Actualizar el estilo de hero-bg-img para incluir blur
h = h.replace(
  '.sport-bg .hero-bg-img {\n  position: absolute; inset: 0; z-index: 0;\n  width: 100%; height: 100%; object-fit: cover;\n  opacity: 0.18;\n  pointer-events: none;\n}',
  '.sport-bg .hero-bg-img {\n  position: absolute; inset: 0; z-index: 0;\n  width: 100%; height: 100%; object-fit: cover;\n  opacity: 0.18;\n  filter: blur(2px) brightness(0.6);\n  pointer-events: none;\n}'
)

open(path, 'w').write(h)
print('OK')
