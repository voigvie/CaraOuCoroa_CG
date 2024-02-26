# Rodrigo Siqueira Ribeiro Januário - 21110618
# Giovanna Almeida Vieira - 21112927


import random as rd
import numpy
from math import cos
from math import sin
from PIL import Image as Image
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global giro
global animado
global ligaventilador
global rota
global cair
global cont
global light_pos
global tex1
global tex2
global tex3

tex1 = 0
tex2 = 0
tex3 = 0

light_pos = 0
cont = 0
cair = 0
rota = 0
esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 30
giro = 0
animado = 0

def read_texture(filename):
      img = Image.open(filename)
      img_data = numpy.array(list(img.getdata()), numpy.int8)
      textID = glGenTextures(1)
      glBindTexture(GL_TEXTURE_2D, textID)
      glPixelStorei(GL_UNPACK_ALIGNMENT, 1)     
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
      glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
      return textID


def texture():
    global tex1
    global tex2
    global tex3

    tex1 = read_texture('parede.jpg')
    tex2 = read_texture('xadrez.jpg')
    tex3 = read_texture('bola.jpg')


def parede(x,y,z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex1)
    
    glBegin(GL_POLYGON)
    glTexCoord2f (0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)

    glTexCoord2f (3.0, 0.0)
    glVertex3f(3.0, 0.0, 0.0)

    glTexCoord2f (3.0, 3.0)
    glVertex3f(3.0, 3.0, 0.0)

    glTexCoord2f (0.0, 3.0)
    glVertex3f(0.0, 3.0, 0.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)   
    glPopMatrix()
    

def mesa(x,y,z):
    
    glPushMatrix()
    glTranslate( x, y, z)  
     
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex2)
    
    glBegin(GL_POLYGON)
    
    glTexCoord2f (0.0, 0.0)
    glVertex3f(4.0, 0.0, -4.0)

    glTexCoord2f (3.0, 0.0)
    glVertex3f(4.0, 0.0, 4.0)

    glTexCoord2f (3.0, 3.0)
    glVertex3f(-4.0, 0.0, 4.0)

    glTexCoord2f (0.0, 3.0)
    glVertex3f(-4.0, 0.0, -4.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)   
    glPopMatrix()

def bola(x,y,z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(80, 0, 1, 0)
    glRotatef(180, 1, 0, 0)
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex3)

    gluSphere(qobj, 1, 20, 20)
    
    gluDeleteQuadric(qobj)
    glDisable(GL_TEXTURE_2D)    
    glPopMatrix()

def desenho():
    bola(2,1.7,-2.3)
    parede(2,0,-3)
    parede(1,0,-3)
    parede(-2,0,-3)
    parede(-5,0,-3)
    mesa(0,-.1,0)
    glColor3f(1, 0.8, 0.0)
    glPushMatrix()
    glTranslatef(0,cair,0)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(rota, 1.0, 0.0, 0.0)
    glutSolidCylinder(1.1, .15, 1000, 10)
    
    glPushMatrix()
    for i in range(-10,0):
        glColor3f(1, 1, 1)
        glTranslatef(0,0.1,0)
        glPushMatrix()
        glTranslatef(0,(i/10),0.03)
        glutSolidCube(0.1)
        glPopMatrix()    
        
    for i in range(-10,0):
        glColor3f(0, 0, 1)
        glTranslatef(0.1,0,0)
        glPushMatrix()
        glTranslatef((i/10),-1,0.03)
        glutSolidCube(0.1)
        glPopMatrix()
    glPopMatrix()  
    
    glPushMatrix()  
    for i in range(-10,0):
        glColor3f(1, 0, 0)
        glTranslatef(0,0.1,0)
        glPushMatrix()
        glTranslatef(0,(i/10),0.12)
        glutSolidCube(0.1)
        glPopMatrix()    
        
    for i in range(-10,0):
        glColor3f(0, 0, 0)
        glTranslatef(0.1,0,0)
        glPushMatrix()
        glTranslatef((i/10),-1,0.12)
        glutSolidCube(0.1)
        glPopMatrix()
    glPopMatrix()    
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(-1.5,0,-2.1)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(-1.5,.2,-2.1)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(-1.2,.4,-2.1)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(-1.7,.6,-2.1)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(2,0,-2.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(2,.2,-2.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(2,.4,-2.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(2,.6,-2.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 0.8, 0.0)
    glTranslatef(2,.8,-2.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.8, .15, 1000, 10)
    glPopMatrix()



def iluminacao_da_cena():
    global aux1
    global light_pos
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]
    luzEspecular = [1.0, 1.0, 1.0, 1.0] 
    posicaoLuz=[0.0, 50.0, 0.0, 1]
    posicaoLuz2=[50.0, 0.0, 50.0, 1]
    luzes = [posicaoLuz,posicaoLuz2]
    
    
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60
    
    glClearColor(0.0, 0.0, 0.0, 0.0)
    
    glShadeModel(GL_SMOOTH)
    
    glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, especularidade)
   
    glMateriali(GL_FRONT_AND_BACK,GL_SHININESS,especMaterial)
    
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, luzes[light_pos])
    
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o uso de transparencias
    glEnable(GL_BLEND)
    #glEnable(GL_ALFA_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def tela():
    global angulo
    global animado
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    
    gluPerspective(angulo,1,0.1,500) 

    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 

    gluLookAt(sin(esqdir) * 15, 5 + cimabaixo ,cos(esqdir) * 15, aux1,aux2,0, 0,1,0) 

    iluminacao_da_cena()

    glEnable(GL_DEPTH_TEST)
     
    desenho() 
    glutSwapBuffers()


def Teclado (tecla, x, y):
    global aux1
    global aux2
    global cimabaixo
    global esqdir
    global angulo
    global light_pos
    
    if tecla == b'q':  # Q
        light_pos = 1
	
    if tecla == b'w': # W
        light_pos = 0
        
    if tecla == b'e': # E
        cimabaixo = 0
        esqdir = 0
        
    if tecla == b'r': # R
        cimabaixo = 8
        esqdir = 5

    tela()
    glutPostRedisplay()

   
def ControleMouse(button, state, x, y):
    global animado
    global cont
    if (button == GLUT_LEFT_BUTTON):
        animado = 1
        cont = 0
    tela()
    glutPostRedisplay()

def animacao():
    global rota
    global cont
    global cair
    global animado
    lista = [0, 180]
    if animado == 1:
        rota = rota + 80
        if(cont<=2):
            cair += 0.1
            cont += 0.08
        elif(cont>2):
            if(cair > 0):
                cair -= 0.08
            elif(cair<=0.2):
                cair = 0
                rota = lista[rd.randint(1,100)%2]
                animado = 0
                print(rota)
    
    tela()
    glutPostRedisplay()
    
    
glutInit(argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH |GLUT_DOUBLE) 
glutInitWindowSize(600,600)
glutCreateWindow(b"Animacao")
distancia = 20
texture()
glutDisplayFunc(tela)
glutIdleFunc(animacao)
glutMouseFunc(ControleMouse)
glutKeyboardFunc(Teclado)
glutMainLoop() 