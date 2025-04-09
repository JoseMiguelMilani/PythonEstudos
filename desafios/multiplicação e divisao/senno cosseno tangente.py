import math

num = float(input(''))

sen = math.sin(math.radians(num) )
cos = math.cos(math.radians(num) )
tang = math.tan(math.radians(num) )

print ('o senno de {} é {:.2f}, o coseno {:.2f} e a tangente é {:.2f}' .format(num, sen, cos, tang))