import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
f = open(path, 'r')
h = f.read()
f.close()
h = h.replace('<div class="section-title" style="color:#f5c518; text-shadow:0 0 30px rgba(245,197,24,0.5);">BINGO593</div>', '')
open(path, 'w').write(h)
print('Bingo title OK')
