from ttdraw import _DRAW
from ttfunc import _FCM,_FCE,_PASS,_MIN,_MAX,_CEN
from pyfirmata import ArduinoMega, util

MESA = "SIMULACAO"
INICIAR = True

mega = ArduinoMega('COM3')
iterator = util.Iterator(mega)
iterator.start()

DM_pin_YGOL_ENE = mega.get_pin('d:18:o')
DM_pin_YGOL_DIR = mega.get_pin('d:19:o')  
DM_pin_YGOL_PAS = mega.get_pin('d:20:o') 
DM_pin_RGOL_ENE = mega.get_pin('d:21:o')  
DM_pin_RGOL_DIR = mega.get_pin('d:22:o')
DM_pin_RGOL_PAS = mega.get_pin('d:23:o') 
FC_pin_MGOL_MIN = mega.get_pin('d:24:i') 
FC_pin_MGOL_MAX = mega.get_pin('d:25:i')
FC_pin_EGOL     = mega.get_pin('d:26:i')

DM_pin_YDEF_ENE = mega.get_pin('d:27:o')
DM_pin_YDEF_DIR = mega.get_pin('d:28:o')  
DM_pin_YDEF_PAS = mega.get_pin('d:29:o') 
DM_pin_RDEF_ENE = mega.get_pin('d:30:o')  
DM_pin_RDEF_DIR = mega.get_pin('d:31:o')
DM_pin_RDEF_PAS = mega.get_pin('d:32:o') 
FC_pin_MDEF_MIN = mega.get_pin('d:33:i') 
FC_pin_MDEF_MAX = mega.get_pin('d:34:i')
FC_pin_EDEF     = mega.get_pin('d:35:i')

DM_pin_YMEI_ENE = mega.get_pin('d:36:o')
DM_pin_YMEI_DIR = mega.get_pin('d:37:o')  
DM_pin_YMEI_PAS = mega.get_pin('d:38:o') 
DM_pin_RMEI_ENE = mega.get_pin('d:39:o')  
DM_pin_RMEI_DIR = mega.get_pin('d:40:o')
DM_pin_RMEI_PAS = mega.get_pin('d:41:o') 
FC_pin_MMEI_MIN = mega.get_pin('d:42:i') 
FC_pin_MMEI_MAX = mega.get_pin('d:43:i')
FC_pin_EMEI     = mega.get_pin('d:44:i')

DM_pin_YATA_ENE = mega.get_pin('d:45:o')
DM_pin_YATA_DIR = mega.get_pin('d:46:o')  
DM_pin_YATA_PAS = mega.get_pin('d:47:o') 
DM_pin_RATA_ENE = mega.get_pin('d:48:o')  
DM_pin_RATA_DIR = mega.get_pin('d:49:o')
DM_pin_RATA_PAS = mega.get_pin('d:50:o') 
FC_pin_MATA_MIN = mega.get_pin('d:51:i') 
FC_pin_MATA_MAX = mega.get_pin('d:52:i')
FC_pin_EATA     = mega.get_pin('d:53:i')

def MESA():
    global aPASS,yPASS,yJOG,mGOL,mDEF,mMEI,mATA
    
    aPASS = 0.18
    yPASS = 0.53

    yJOG   = 40
        
    mGOL = 125
    mDEF = 135
    mMEI = 60
    mATA = 120

def CONFIG():
    global yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA
    yGOL = -100
    aGOL = 0
    yDEF = 50
    aDEF = 90
    yMEI = -20
    aMEI = 180
    yATA = 70
    aATA = 270
    
def INIC():
    global  DM_YGOL,DM_RGOL,DM_YDEF,DM_RDEF,DM_YMEI,DM_RMEI,DM_YATA,DM_RATA
    global  iGOL,iDEF,iMEI,iATA
    global  MAPEAMENTO,MINIMO,MAXIMO,INICIAR
    
    DM_YGOL = "100"
    DM_RGOL = "100"
    DM_YDEF = "100"
    DM_RDEF = "100"
    DM_YMEI = "100"
    DM_RMEI = "100"
    DM_YATA = "100"
    DM_RATA = "100"

    iGOL = 0
    iDEF = 0
    iMEI = 0
    iATA = 0

    INICIAR    = False
    MAPEAMENTO = True
    MINIMO     = False
    MAXIMO     = False

def MIN():
    global DM_YGOL,FCMGOL_MIN,DM_RGOL,FCEGOL
    global DM_YDEF,FCMDEF_MIN,DM_RDEF,FCEDEF
    global DM_YMEI,FCMMEI_MIN,DM_RMEI,FCEMEI
    global DM_YATA,FCMATA_MIN,DM_RATA,FCEATA
    global MINIMO
    
    DM_YGOL = _MIN(FCMGOL_MIN)
    DM_RGOL = _MIN(FCEGOL)
    DM_YDEF = _MIN(FCMDEF_MIN)
    DM_RDEF = _MIN(FCEDEF)
    DM_YMEI = _MIN(FCMMEI_MIN)
    DM_RMEI = _MIN(FCEMEI)
    DM_YATA = _MIN(FCMATA_MIN)
    DM_RATA = _MIN(FCEATA)
    
    if(FCMGOL_MIN+FCEGOL+FCMDEF_MIN+FCEDEF+FCMMEI_MIN+FCEMEI+FCMATA_MIN+FCEATA == 8):
        MINIMO = True 
        if MESA == "FISICA": #Sincronizar a simulação com a mesa
            iGOL = -mGOL
            iDEF = -mDEF
            iMEI = -mMEI
            iATA = -mATA
            
def MAX():
    global DM_YGOL,iGOL_TEMP,iGOL,FCMGOL_MAX
    global DM_YDEF,iDEF_TEMP,iDEF,FCMDEF_MAX
    global DM_YMEI,iMEI_TEMP,iMEI,FCMMEI_MAX
    global DM_YATA,iATA_TEMP,iATA,FCMATA_MAX
    global MAXIMO
    
    [iGOL,DM_YGOL] = _MAX(iGOL,FCMGOL_MAX)
    [iDEF,DM_YDEF] = _MAX(iDEF,FCMDEF_MAX)
    [iMEI,DM_YMEI] = _MAX(iMEI,FCMMEI_MAX)
    [iATA,DM_YATA] = _MAX(iATA,FCMATA_MAX)
    
    if(FCMGOL_MAX+FCMDEF_MAX+FCMMEI_MAX+FCMATA_MAX == 4):
        MAXIMO = True
        iGOL_TEMP = iGOL/2
        iDEF_TEMP = iDEF/2
        iMEI_TEMP = iMEI/2
        iATA_TEMP = iATA/2
    
def CEN():
    global iGOL_TEMP,DM_YGOL
    global iDEF_TEMP,DM_YDEF
    global iMEI_TEMP,DM_YMEI
    global iATA_TEMP,DM_YATA
    global MAPEAMENTO
    
    [iGOL_TEMP,DM_YGOL] = _CEN(iGOL_TEMP,DM_YGOL)
    [iDEF_TEMP,DM_YDEF] = _CEN(iDEF_TEMP,DM_YDEF)
    [iMEI_TEMP,DM_YMEI] = _CEN(iMEI_TEMP,DM_YMEI)
    [iATA_TEMP,DM_YATA] = _CEN(iATA_TEMP,DM_YATA)
    
    if(iGOL_TEMP+iDEF_TEMP+iMEI_TEMP+iATA_TEMP < 0):
        MAPEAMENTO = False

def FC ():
    global  yGOL,aGOL,mGOL,FC_pin_MGOL_MIN,FC_pin_MGOL_MAX,FC_pin_EGOL,FCMGOL_MIN,FCMGOL_MAX,FCEGOL
    global  yDEF,aDEF,mDEF,FC_pin_MDEF_MIN,FC_pin_MDEF_MAX,FC_pin_EDEF,FCMDEF_MIN,FCMDEF_MAX,FCEDEF
    global  yMEI,aMEI,mMEI,FC_pin_MMEI_MIN,FC_pin_MMEI_MAX,FC_pin_EMEI,FCMMEI_MIN,FCMMEI_MAX,FCEMEI
    global  yATA,aATA,mATA,FC_pin_MATA_MIN,FC_pin_MATA_MAX,FC_pin_EATA,FCMATA_MIN,FCMATA_MAX,FCEATA
    global  aPASS,MESA
            
    if MESA == "FISICA":        
        FCMGOL_MIN = int(FC_pin_MGOL_MIN.read()) 
        FCMGOL_MAX = int(FC_pin_MGOL_MAX.read()) 
        FCEGOL     = int(FC_pin_EGOL.read()) 
        
        FCMDEF_MIN = int(FC_pin_MDEF_MIN.read()) 
        FCMDEF_MAX = int(FC_pin_MDEF_MAX.read()) 
        FCEDEF     = int(FC_pin_EDEF.read()) 
        
        FCMMEI_MIN = int(FC_pin_MMEI_MIN.read()) 
        FCMMEI_MAX = int(FC_pin_MMEI_MAX.read()) 
        FCEMEI     = int(FC_pin_EMEI.read()) 
        
        FCMATA_MIN = int(FC_pin_MATA_MIN.read()) 
        FCMATA_MAX = int(FC_pin_MATA_MAX.read()) 
        FCEATA     = int(FC_pin_EATA.read()) 
    else:       
        FCMGOL_MIN = _FCM(yGOL,-mGOL)
        FCMGOL_MAX = _FCM(mGOL, yGOL)
        FCEGOL     = _FCE(aGOL,aPASS)
       
        FCMDEF_MIN = _FCM(yDEF,-mDEF)
        FCMDEF_MAX = _FCM(mDEF, yDEF)
        FCEDEF     = _FCE(aDEF,aPASS)
        
        FCMMEI_MIN = _FCM(yMEI,-mMEI)
        FCMMEI_MAX = _FCM(mMEI, yMEI)
        FCEMEI     = _FCE(aMEI,aPASS)
        
        FCMATA_MIN = _FCM(yATA,-mATA)
        FCMATA_MAX = _FCM(mATA, yATA)
        FCEATA     = _FCE(aATA,aPASS)
    
def MAPE():
    global MINIMO,MAXIMO
    if MINIMO == False:
        FC()
        MIN()
    elif MAXIMO == False:
        FC()
        MAX()
    else:
        CEN()
        
def PASS ():
    global  yGOL,DM_YGOL,DM_pin_YGOL_ENE,DM_pin_YGOL_DIR,DM_pin_YGOL_PAS,aGOL,DM_RGOL,DM_pin_RGOL_ENE,DM_pin_RGOL_DIR,DM_pin_RGOL_PAS
    global  yDEF,DM_YDEF,DM_pin_YDEF_ENE,DM_pin_YDEF_DIR,DM_pin_YDEF_PAS,aDEF,DM_RDEF,DM_pin_RDEF_ENE,DM_pin_RDEF_DIR,DM_pin_RDEF_PAS
    global  yMEI,DM_YMEI,DM_pin_YMEI_ENE,DM_pin_YMEI_DIR,DM_pin_YMEI_PAS,aMEI,DM_RMEI,DM_pin_RMEI_ENE,DM_pin_RMEI_DIR,DM_pin_RMEI_PAS
    global  yATA,DM_YATA,DM_pin_YATA_ENE,DM_pin_YATA_DIR,DM_pin_YATA_PAS,aATA,DM_RATA,DM_pin_RATA_ENE,DM_pin_RATA_DIR,DM_pin_RATA_PAS
    global  yPASS,aPASS
            
    DM_pin_YGOL_ENE.write(int(DM_YGOL[0])) 
    DM_pin_YGOL_DIR.write(int(DM_YGOL[1]))   
    DM_pin_YGOL_PAS.write(int(DM_YGOL[2])) 
    yGOL = _PASS(yGOL,DM_YGOL, yPASS) 
    
    DM_pin_RGOL_ENE.write(int(DM_RGOL[0])) 
    DM_pin_RGOL_DIR.write(int(DM_RGOL[1])) 
    DM_pin_RGOL_PAS.write(int(DM_RGOL[2])) 
    aGOL = _PASS(aGOL,DM_RGOL,aPASS) 
    
    DM_pin_YDEF_ENE.write(int(DM_YDEF[0])) 
    DM_pin_YDEF_DIR.write(int(DM_YDEF[1]))   
    DM_pin_YDEF_PAS.write(int(DM_YDEF[2]))
    yDEF = _PASS(yDEF,DM_YDEF, yPASS)
    
    DM_pin_RDEF_ENE.write(int(DM_RDEF[0])) 
    DM_pin_RDEF_DIR.write(int(DM_RDEF[1])) 
    DM_pin_RDEF_PAS.write(int(DM_RDEF[2]))
    aDEF = _PASS(aDEF,DM_RDEF,aPASS) 
    
    DM_pin_YMEI_ENE.write(int(DM_YMEI[0])) 
    DM_pin_YMEI_DIR.write(int(DM_YMEI[1]))   
    DM_pin_YMEI_PAS.write(int(DM_YMEI[2])) 
    yMEI = _PASS(yMEI,DM_YMEI, yPASS)
    
    DM_pin_RMEI_ENE.write(int(DM_RMEI[0])) 
    DM_pin_RMEI_DIR.write(int(DM_RMEI[1])) 
    DM_pin_RMEI_PAS.write(int(DM_RMEI[2]))  
    aMEI = _PASS(aMEI,DM_RMEI,aPASS) 
    
    DM_pin_YATA_ENE.write(int(DM_YATA[0])) 
    DM_pin_YATA_DIR.write(int(DM_YATA[1]))   
    DM_pin_YATA_PAS.write(int(DM_YATA[2]))
    yATA = _PASS(yATA,DM_YATA, yPASS) 
    
    DM_pin_RATA_ENE.write(int(DM_RATA[0])) 
    DM_pin_RATA_DIR.write(int(DM_RATA[1])) 
    DM_pin_RATA_PAS.write(int(DM_RATA[2])) 
    aATA = _PASS(aATA,DM_RATA,aPASS) 
    
    _DRAW(yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA)
    
def _MOV(i,PASS):
    if i > PASS/2:
        DM = "011"
        i = i-1
    elif i < PASS/2:
        DM = "001"
        i = i+1
    else:
        DM = "000"
        i = i
    return i,DM
    
def MOVER(ID,yPOS,CHUT):
    global yPASS,yGOL,DM_YGOL,yDEF,DM_YDEF,yMEI,DM_YMEI,yATA,DM_YATA
    if ID == 0: 
        i = int((yPOS-yGOL)/yPASS)
        while i != 0:
            [i,DM_YGOL] = _MOV(i,yPASS)
            PASS()
        DM_YGOL = "000"
    elif ID == 1: 
        i = int((yPOS-yDEF)/yPASS)
        while i != 0:
            [i,DM_YDEF] = _MOV(i,yPASS)
            PASS()
        DM_YDEF = "000"
    elif ID == 2: 
        i = int((yPOS-yMEI)/yPASS)
        while i != 0:
            [i,DM_YMEI] = _MOV(i,yPASS)
            PASS()
        DM_YMEI = "000"
    elif ID == 3: 
        i = int((yPOS-yATA)/yPASS)
        while i != 0:
            [i,DM_YATA] = _MOV(i,yPASS)
            PASS()
        DM_YATA = "000"

def _CONTROL(ID,yPOS,CHUT):
    global INICIAR,MAPEAMENTO,yPASS,aPASS,yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA,DM_YGOL,DM_YDEF,DM_YMEI,DM_YATA
    while INICIAR == True:
        MESA()
        CONFIG()
        INIC()
    while MAPEAMENTO == True:
        MAPE()
        PASS()
        DM_YGOL = "000"
        DM_YDEF = "000"
        DM_YMEI = "000"
        DM_YATA = "000"
        
    MOVER(ID,yPOS,CHUT)
    return yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA
