import os
path = '/Users/' + os.getenv('USER') + '/Desktop/diablitobet/index.html'
h = open(path, 'r').read()
h = h.replace(
  '<span class="op-icon">🏛️</span><span>Logo CNT</span>',
  '<img src="img/cnt.png" alt="CNT" style="width:50px;height:50px;object-fit:contain;">'
)
open(path, 'w').write(h)
print('CNT OK')
