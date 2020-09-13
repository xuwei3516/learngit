from time import sleep
def hanoi(n,a,b,c):
	global t
	if n==1:
		print(a,'->',c)
		t+=1
		#sleep(1)
	else:
		hanoi(n-1,a,c,b)
		hanoi(1,a,b,c)
		hanoi(n-1,b,a,c)
#
t=0
hanoi(20,'左','中','右')
print("%d次移动后可以得到"%t)
