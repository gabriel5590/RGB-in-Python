import math
import time


def rgb(velocidade):
	t = time.perf_counter() * velocidade
	r = int((math.sin(t +0 ) * 127 + 128))
	g = int((math.sin(t + 2) * 127 + 128))
	b =  int((math.sin(t +4 ) * 127 + 128))
	return f"0x{r:02X}{g:02X}{b:02X}"
	
while True:
		print(rgb(2.0))