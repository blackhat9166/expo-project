import math

wv = float(input("sidways compopnent "))
wh = float(input("upsidedown component "))
v0 = float(input("muzzle velocity of the gun "))
angle = float(input("input the given inclination ang "))
u_angle = float(input("given input by user "))
g = 9.80665
R = float(input("given range of the target "))
v = float(v0*math.cos(math.radians(u_angle)))
vv = float(v0*math.sin(math.radians(u_angle)))
a = float(0.5*g*(math.sin(math.radians(angle))))
av = float(0.5*g*(math.cos(math.radians(angle))))
t =0
if angle >= 0:
 d = (v*v)-(4*a*R)
 if d <= 0:
  print("bullet cant reach")
 else: 
  d = math.sqrt(d)
  t = (v-d)/(2*a)
  dspl_v = (vv*t)-(a*t*t)
else:
  d =  (v*v)+4*a*R
  d = math.sqrt(d)
  t = (-v+d)/(2*a)
  dspl_v = (vv*t)+(av*t*t)



