import math

def _FCM (Y,X):
    if Y <= X:
        sensor = 1
    else:
        sensor = 0
    return sensor
    
def _FCE(A,PASS):
    A = math.asin(math.sin(A*math.pi/180))*180/math.pi #Considerar apenas a fração do angulo.
    if (A > -PASS and A < PASS ):                      #Considerar uma faixa minima.
        sensor = 1
    else:
        sensor = 0
    return sensor
    
def _PASS(Yold,DM,PASS):
    if DM[1] == '0':
        PASS = -PASS
    if DM[2] == '1':
        Y = Yold + PASS
    else:
        Y = Yold 
    return Y
    
def _MIN(FC):
    if FC != 1:
        DM = "001"
    else:
        DM = "000"
    return DM
        
def _MAX(i,FC):
    if FC != 1:
        DM = "011"
        i = i+1
    else:
        DM = "000"
    return i,DM
    
def _CEN(i,DM):
    if i > 0:
        DM = "001"
        i = i-1
    else:
        DM = "000"
        i = i
    return i,DM
    