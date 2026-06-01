import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
# Quitar background-image del hero
h = h.replace(
  '  background-image: url("img/hero-bg.png");\n  background-size: cover;\n  background-position: center top;\n',
  ''
)
# Poner la imagen con opacidad via pseudo elemento en sport-bg
h = h.replace(
  '/* ── SPORT BG ── */\n.sport-bg {\n  position: relative;\n  background:\n    linear-gradient(160deg, rgba(8,0,8,0.05) 0%, rgba(30,0,10,0.05) 40%, rgba(8,0,8,0.10) 100%);\n}',
  '/* ── SPORT BG ── */\n.sport-bg {\n  position: relative;\n  background: #080008;\n}\n.sport-bg .hero-bg-img {\n  position: absolute; inset: 0; z-index: 0;\n  width: 100%; height: 100%; object-fit: cover;\n  opacity: 0.18;\n  pointer-events: none;\n}'
)
# Agregar la imagen en el HTML dentro del hero
h = h.replace(
  '<section class="hero sport-bg">',
  '<section class="hero sport-bg"><img class="hero-bg-img" src="img/hero-bg.png" alt="">'
)
open(path, 'w').write(h)
print('OK')
