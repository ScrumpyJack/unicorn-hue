#!/usr/bin/python
import unicornhat as unicornhat
import colorsys
import time
import signal

def cleanup():
 unicornhat.clear()

while True:
 count=0
 h=0 # hue
 l=0.5 # saturation 50%
 s=1.0 # value 100%
 unicornhat.brightness(1.0)
 while h <= 1:
  count = count + 1
  h = h + 0.001
  rf, gf, bf = colorsys.hls_to_rgb(h, l, s)
  r, g, b = (int(rf*255.0), int(gf*255.0), int(bf*255.0))
  print(r, g, b, h, count)
  for x in range(8):
   for y in range(8):
    unicornhat.set_pixel(x,y,int(r),int(g),int(b))
  unicornhat.show()
  time.sleep(6)
  signal.signal(signal.SIGTERM, cleanup)
