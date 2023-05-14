import math
n = 10
a = { 'x': 0, 'y': 0 }
b = { 'x': 100, 'y': 0 }
th = math.pi * 60 / 180
def koch_curve(n, a, b):
  if n == 0:
    return

  s = {}
  t = {}
  u = {}
  s['x'] = (2.0 * a['x'] + 1.0 * b['x']) / 3.0
  s['y'] = (2.0 * a['y'] + 1.0 * b['y']) / 3.0
  t['x'] = (1.0 * a['x'] + 2.0 * b['x']) / 3.0
  t['y'] = (1.0 * a['y'] + 2.0 * b['y']) / 3.0
  u['x'] = (t['x'] - s['x']) * math.cos(th) - (t['y'] - s['y']) * math.sin(th) + s['x']
  u['y'] = (t['x'] - s['x']) * math.sin(th) + (t['y'] - s['y']) * math.cos(th) + s['y']

  koch_curve(n - 1, a, s)
  print('%.8f %.8f' % (s['x'], s['y']))
  koch_curve(n - 1, s, u)
  print('%.8f %.8f' % (u['x'], u['y']))
  koch_curve(n - 1, u, t)
  print('%.8f %.8f' % (t['x'], t['y']))
  koch_curve(n - 1, t, b)

print('%.8f %.8f' % (a['x'], a['y']))
koch_curve(n, a, b)
print('%.8f %.8f' % (b['x'], b['y']))