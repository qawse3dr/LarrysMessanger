#This will be msging chat room software. This will be the hosts program.
import pygame,sys,socket,thread#imports Pygame,sys, and sockets for sending msgs
from pygame.locals import *
host = raw_input("What is the ip of the host") #asks for the users ip
pygame.init()#Gets everything ready for pygame
screen = pygame.display.set_mode((300,300))#Create Screen
pygame.display.set_caption("Larry's Messenger") #Change Title
#Create font
font = pygame.font.Font(None, 16)
#For displaying text
def text(string,x,y,colour):
    textobj = font.render(string, 1, colour)
    screen.blit(textobj, (x-textobj.get_width()//2,y-textobj.get_height()//2))
def getText(key,message):#This is to get the message before it's sent.
    #This checks if the key is a valued input
    #and if it is convert it to a charater and append it to
    #msg using event.unicode.
    if 31< key<255 and len(message) < 200:message.append(event.unicode)
    else:
        if key == K_BACKSPACE and len(message) != 0:
            message = message.pop()#Deletes a char
        if key == K_KP_ENTER or key == K_RETURN:
            send("".join(message))#sends message.
            sendBlank = False
   
        
            
def send(string): #This will send the message to the client program
    ProgramSocket.sendall(string)
    oldMessages.append("me: "+string)
    del message[:]

    
message = [] #used to hold the messages
oldMessages = []#This will hold all the hold messages
ProgramSocket = socket.socket()#This will be the socket to send all the info back and forth
port = 12345 #This will be the socket They Connect to.
ProgramSocket.connect((host,port))#Connects to host.
global sendBlank
while 1:#run Loop
    sendBlank = True
    screen.fill((200,200,200))#Fills screen gray
    pygame.draw.rect(screen,(255,255,255),(0,260,300,35),0)
    text("".join(message),150,280,(255,150,0))#Where the user text is writen
    for msg in range(len(oldMessages)-1,-1,-1):#Puts old messages
        text(oldMessages[msg],150,(len(oldMessages)-msg)*-30+250,(30,25,255))
    pygame.draw.rect(screen,(200,200,200),(0,0,300,120),0)
    text("Larry's Chat Room Client",150,50,(10,10,10))#Makes chat title

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            getText(event.key,message)#adds Character to message.
        
        if event.type == QUIT:#Quits game and exits pygame and sys.
            ProgramSocket.close#Closes the socket
            pygame.quit()
            sys.exit()
    
    pygame.display.update()  #Updates the screen image
    #gets msg
    textfile =ProgramSocket.recv(1024)
    if not(textfile.isspace()):
        oldMessages.append("Guessed: "+textfile)
    if sendBlank:
        #sends blank msg so it continues loop
        ProgramSocket.send(" ")
    
    
    
