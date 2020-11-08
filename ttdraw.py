import pygame
import math

from pygame.locals import *
from OpenGL.GL import *

########################################################
################## CONFIGURAÇÕES MESA ##################

larCamp = 1160
altCamp = 770
passo   = 0.53
apasso  = 0.18 #deg
xJog    = 30
yJog    = 40
has     = 10

hasGOL =   70
disGOL =   250

hasDEF =   215
disDEF =   250

hasMEI =   505
disMEI =   128

hasATA =   795
disATA =   163

########################################################
pygame.init()
pygame.display.set_mode((larCamp, altCamp), DOUBLEBUF | OPENGL)
####################### DESENHO ########################

def rect(x, y, w, l):
    glBegin(GL_QUADS)
    glVertex2f(x  , y  )
    glVertex2f(x  , y+l)
    glVertex2f(x+w, y+l)
    glVertex2f(x+w, y  )
    glEnd()

def F_CAM():
    glColor4d(0, 255, 0, 255)
    rect(0, 0, larCamp, altCamp)
    glColor4d(255, 255, 255, 255)
    rect(0              , (altCamp-disGOL)/2,  has, disGOL)
    rect((larCamp-has/4)/2, 0, has/4, altCamp)
    rect(larCamp        , (altCamp-disGOL)/2, -has, disGOL)
    
def F_HAS(xhas): 
    glColor4d(63, 63, 63, 255)
    rect(xhas-has/2, 0, has, altCamp)
    rect(larCamp-xhas-has/2, 0, has, altCamp)

def F_GOL(Y,A):
    glColor4d(0, 0, 255, 126)
    rect(hasGOL               , altCamp/2-Y-yJog/3, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasGOL-xJog/2        , altCamp/2-Y-yJog/2, xJog                         , yJog    )
    glColor4d(255, 0, 0, 126)
    rect(larCamp-hasGOL-xJog/2, altCamp/2  -yJog/2, xJog                         , yJog    )
    
def F_DEF(Y,A):
    glColor4d(0, 0, 255, 126)
    rect(hasDEF               , altCamp/2-Y-yJog/3-disDEF/2, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasDEF               , altCamp/2-Y-yJog/3+disDEF/2, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasDEF-xJog/2        , altCamp/2-Y-yJog/2-disDEF/2, xJog               , yJog    )
    rect(hasDEF-xJog/2        , altCamp/2-Y-yJog/2+disDEF/2, xJog               , yJog    )
    glColor4d(255, 0, 0, 126)
    rect(larCamp-hasDEF-xJog/2, altCamp/2  -yJog/2-disDEF/2, xJog               , yJog    )
    rect(larCamp-hasDEF-xJog/2, altCamp/2  -yJog/2+disDEF/2, xJog               , yJog    )
    
def F_MEI(Y,A):
    glColor4d(0, 0, 255, 126)
    rect(hasMEI               , altCamp/2-Y-yJog/3-disMEI*2, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasMEI               , altCamp/2-Y-yJog/3-disMEI  , math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasMEI               , altCamp/2-Y-yJog/3         , math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasMEI               , altCamp/2-Y-yJog/3+disMEI  , math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasMEI               , altCamp/2-Y-yJog/3+disMEI*2, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasMEI-xJog/2        , altCamp/2-Y-yJog/2-disMEI*2, xJog               , yJog    )
    rect(hasMEI-xJog/2        , altCamp/2-Y-yJog/2-disMEI  , xJog               , yJog    )
    rect(hasMEI-xJog/2        , altCamp/2-Y-yJog/2         , xJog               , yJog    )
    rect(hasMEI-xJog/2        , altCamp/2-Y-yJog/2+disMEI  , xJog               , yJog    )
    rect(hasMEI-xJog/2        , altCamp/2-Y-yJog/2+disMEI*2, xJog               , yJog    )
    glColor4d(255, 0, 0, 126)
    rect(larCamp-hasMEI-xJog/2, altCamp/2     -yJog/2-disMEI*2, xJog               , yJog    )
    rect(larCamp-hasMEI-xJog/2, altCamp/2     -yJog/2-disMEI  , xJog               , yJog    )
    rect(larCamp-hasMEI-xJog/2, altCamp/2     -yJog/2         , xJog               , yJog    )
    rect(larCamp-hasMEI-xJog/2, altCamp/2     -yJog/2+disMEI  , xJog               , yJog    )
    rect(larCamp-hasMEI-xJog/2, altCamp/2     -yJog/2+disMEI*2, xJog               , yJog    )
    
def F_ATA(Y,A):
    glColor4d(0, 0, 255, 126)
    rect(hasATA               , altCamp/2-Y-yJog/3-disATA, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasATA               , altCamp/2-Y-yJog/3       , math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasATA               , altCamp/2-Y-yJog/3+disATA, math.sin(A*math.pi/180)*45, yJog*2/3)
    rect(hasATA-xJog/2        , altCamp/2-Y-yJog/2-disATA, xJog               , yJog    )
    rect(hasATA-xJog/2        , altCamp/2-Y-yJog/2       , xJog               , yJog    )
    rect(hasATA-xJog/2        , altCamp/2-Y-yJog/2+disATA, xJog               , yJog    )
    glColor4d(255, 0, 0, 126)
    rect(larCamp-hasATA-xJog/2, altCamp/2  -yJog/2-disATA, xJog               , yJog    )
    rect(larCamp-hasATA-xJog/2, altCamp/2  -yJog/2       , xJog               , yJog    )
    rect(larCamp-hasATA-xJog/2, altCamp/2  -yJog/2+disATA, xJog               , yJog    )
    
def _DRAW(yGOL,aGOL,yDEF,aDEF,yMEI,aMEI,yATA,aATA):
    glViewport(0,0,larCamp,altCamp)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,larCamp,0,altCamp,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    F_CAM()
    F_HAS(hasGOL)
    F_HAS(hasDEF)
    F_HAS(hasMEI)
    F_HAS(hasATA)
    F_GOL(yGOL,aGOL)
    F_DEF(yDEF,aDEF)
    F_MEI(yMEI,aMEI)
    F_ATA(yATA,aATA)
    
    pygame.display.flip()
    pygame.event.pump()
