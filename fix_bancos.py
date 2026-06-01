f = open('/Users/' + __import__('os').getenv('USER') + '/Desktop/diablitobet/index.html', 'r')
h = f.read()
f.close()

bancos = [
  ('BANCO PICHINCHA', 'pichincha'),
  ('BANCO DEL PACÍFICO', 'pacifico'),
  ('BANCO DE GUAYAQUIL', 'guayaquil'),
  ('BANCO INTERNACIONAL', 'internacional'),
  ('BANCO BOLIVARIANO', 'bolivariano'),
  ('PRODUBANCO', 'produbanco'),
  ('BANCO DEL AUSTRO', 'austro'),
  ('MUTUALISTA PICHINCHA', 'mutualista')
]

for nombre, archivo in bancos:
  h = h.replace(
    '<span class="banco-icon">🏦</span>\n      <div class="banco-name">' + nombre,
    '<img src="img/' + archivo + '.png" alt="' + nombre + '" style="width:48px;height:48px;object-fit:contain;display:block;margin:0 auto 8px;">\n      <div class="banco-name">' + nombre,
    1
  )

open('/Users/' + __import__('os').getenv('USER') + '/Desktop/diablitobet/index.html', 'w').write(h)
print('Bancos OK')
