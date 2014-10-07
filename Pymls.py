import numpy

def xor(a,b):
    if bool(a) != bool(b):
	    ans = 1
    else:
	    ans = 0
    return ans

def GenerateMLS(n):
    """
	GenerateMLS Generates an MLS sequence 
	
	y = mls(n)
    
    n:		order of MLS
    flag:	true for registers initialised to 1, flase for random
    y:		P-length MLS sequence, where P = 2n-1
	"""
	
	# assign taps which will yeild a maximum length 
	# sequence for a given bit length
	# Vanderkooy, JAES, 42(4), 1994

    if n == 2:
        taps = 2
        tap1 = 1
        tap2 = 2
    elif n == 3:
        taps=2
        tap1=1
        tap2=3
    elif n == 4:
        taps=2
        tap1=1
        tap2=4
    elif n == 5:
        taps=2
        tap1=2
        tap2=5
    elif n == 6:
        taps=2
        tap1=1
        tap2=6
    elif n == 7:
        taps=2
        tap1=1
        tap2=7
    elif n == 8:
        taps=4
        tap1=2
        tap2=3
        tap3=4
        tap4=8
    elif n == 9:
        taps=2
        tap1=4
        tap2=9
    elif n == 10:
        taps=2
        tap1=3
        tap2=10
    elif n == 11:
        taps=2
        tap1=2
        tap2=11
    elif n == 12:
        taps=4
        tap1=1
        tap2=4
        tap3=6
        tap4=12
    elif n == 13:
        taps=4
        tap1=1
        tap2=3
        tap3=4
        tap4=13
    elif n == 14:
        taps=4
        tap1=1
        tap2=3
        tap3=5
        tap4=14
    elif n == 15:
        taps=2
        tap1=1
        tap2=15
    elif n == 16:
        taps=4
        tap1=2
        tap2=3
        tap3=5
        tap4=16
    elif n == 17:
        taps=2
        tap1=3
        tap2=17
    elif n == 18:
        taps=2
        tap1=7
        tap2=18
    elif n == 19:
        taps=4
        tap1=1
        tap2=2
        tap3=5
        tap4=19
    elif n == 20:
        taps=2
        tap1=3
        tap2=20
    elif n == 21:
        taps=2
        tap1=2
        tap2=21
    elif n == 22:
        taps=2
        tap1=1
        tap2=22
    elif n == 23:
        taps=2
        tap1=5
        tap2=23
    elif n == 24:
        taps=4
        tap1=1
        tap2=3
        tap3=4
        tap4=24
    else:
	    print 'input bits must be between 2 and 24'
		
    # initialize the mls buffer and output
    abuff = numpy.ones(n)   
    y = numpy.ndarray(2**n-1)
		
    for i in range(2**n-1,0,-1):
 

        xorbit = xor(abuff[tap1-1],abuff[tap2-1])
        
        if taps == 4:
            xorbit2 = xor(abuff[tap3-1],abuff[tap4-1])
            xorbit = xor(xorbit,xorbit2)

		
		# shift register
        for ii in range(1,n):
            abuff.itemset(n-ii,abuff[n-ii-1])
            #print abuff
        abuff.itemset(0,xorbit)
        
	   
	    # print output
        y[i-1] = (-2 * xorbit) + 1
    return y
        
		
        
        
	
out = GenerateMLS(15)  
print out
    




