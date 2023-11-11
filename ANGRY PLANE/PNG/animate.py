import pygame
import random
import math
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)
def msg(fsize,bold,text,x,y,r,g,b):
    win=pygame.font.SysFont("arial",fsize,bold)
    t=win.render(text,1,(r,g,b))
    trect=t.get_rect()
    trect.center=x,y
    screen.blit(t,trect)
def gameover():
    global background, bgx
    gameover=True
    while gameover:
        screen.blit(background,(bgx,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=False
        pygame.display.update()
        key=pygame.key.get_pressed()
        if key[pygame.K_r]:
            main()
    pygame.quit()
def main():
    pygame.init()
    global background, bgx
    image=[
        pygame.transform.flip(pygame.transform.scale(pygame.image.load("Frame-1.png"),(70,70)),True,False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load("frame-2.png"),(70,70)),True,False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load("frame-3.png"),(70,70)),True,False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load("frame-4.png"),(70,70)),True,False)
           ]
    fly=[
        pygame.transform.scale(pygame.image.load("Plane/Fly (1).png"),(110,100)),
        pygame.transform.scale(pygame.image.load("Plane/Fly (2).png"),(110,100))
        ]
    shoot=[pygame.transform.scale(pygame.image.load("Plane/Shoot (1).png"),(110,100)),
           pygame.transform.scale(pygame.image.load("Plane/Shoot (2).png"),(110,100)),
           pygame.transform.scale(pygame.image.load("Plane/Shoot (3).png"),(110,100)),
           pygame.transform.scale(pygame.image.load("Plane/Shoot (4).png"),(110,100)),
           pygame.transform.scale(pygame.image.load("Plane/Shoot (5).png"),(110,100))
           ]
    fire=[
         pygame.transform.scale(pygame.image.load("1/Explosion_1.png"),(100,90)),
         pygame.transform.scale(pygame.image.load("1/Explosion_2.png"),(100,90)),
         pygame.transform.scale(pygame.image.load("1/Explosion_3.png"),(100,90)),
         pygame.transform.scale(pygame.image.load("1/Explosion_4.png"),(100,90)),
         pygame.transform.scale(pygame.image.load("1/Explosion_5.png"),(100,90)),
         pygame.transform.scale(pygame.image.load("1/Explosion_6.png"),(100,90))
         ]
    bullets=[
         pygame.transform.scale(pygame.image.load("Bullet/Bullet (1).png"),(50,50)),
         pygame.transform.scale(pygame.image.load("Bullet/Bullet (2).png"),(50,50)),
         pygame.transform.scale(pygame.image.load("Bullet/Bullet (3).png"),(50,50)),
         pygame.transform.scale(pygame.image.load("Bullet/Bullet (4).png"),(50,50)),
         pygame.transform.scale(pygame.image.load("Bullet/Bullet (5).png"),(50,50))
         ]
    blood=[
        pygame.transform.scale(pygame.image.load("2/blood2.png"),(50,50)),
        pygame.transform.scale(pygame.image.load("2/blood3.png"),(50,50)),
        pygame.transform.scale(pygame.image.load("2/blood4.png"),(50,50)),
        pygame.transform.scale(pygame.image.load("2/blood5.png"),(50,50)),
        pygame.transform.scale(pygame.image.load("2/blood6.png"),(50,50))
        ]
    explo=pygame.mixer.Sound("Plane/explosion07.wav")
    touch=pygame.mixer.Sound("Plane/explosion09.wav")
    blc=0
    bl=False
    bullet=False
    bulletc=0
    firec=0
    dead=pygame.transform.scale(pygame.image.load("Plane/Dead (1).png"),(110,100))
    background=pygame.transform.scale(pygame.image.load("BG.png"),(width+100,height))
    bgx=-50
    num=0
    x1=width/2-300
    y1=height/2
    bx=[]
    by=[]
    bird=[]
    many=50
    wait=0
    bspeed=20
    die=False
    for i in range(many):
        bx.append(random.randint(1100,2000))
        by.append(random.randint(0,770))
        bird.append(0)
    run=True
    start=False
    clock=pygame.time.Clock()
    bullx=x1+50
    bully=y1+40
    score=0
    vibrate=False
    vc=0
    vib=10
    ########### WHILE LOOP ############ 
    while run:
        clock.tick(60)
        screen.blit(background,(bgx,0))
        num+=1
        if num >=2:
            num=0
        player=fly[int(num)]
        if y1>=height+90:
            touch.play()
            player=dead
            y1=height+90
            wait+=1
        if y1<=0:
            player=dead
            y1=0
            wait+=1
        if wait==20:
            touch.play()
            gameover()
            wait=0
        if bullet==False:
            bullx=x1+50
            bully=y1+40
            bulletc+=1
            if bulletc>=5:
                bulletc=0
            bull=bullets[bulletc]
            screen.blit(bull,(bullx,bully))
        click=pygame.mouse.get_pressed()
        if click[0]:
            start=True
        if start:
            y1+=5
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if start:
                y1-=10
        ######BULLET COLLIDE#################
        if key[pygame.K_LCTRL]:
            bullet=True
        if bullet:
            if bullx<x1+100:
                num+=2
                if num >=5:
                    num=0
                player=shoot[int(num)]
                brect=pygame.Rect(bullx,bully,50,50)
            bullx=bullx
            bully=bully
            bullx+=bspeed
            bulletc+=1
            if bulletc>=5:
                bulletc=0
            bull=bullets[bulletc]
            screen.blit(bull,(bullx,bully))
            if bullx<x1+90:
                explo.play()
        
        if bullx>=width:
            bullet=False
        for i in range(many):
            brect=pygame.Rect(bullx,bully,50,50)
            b=pygame.Rect(bx[i],by[i],50,50)
            p=pygame.Rect(x1,y1,110,90)
            bird[i]+=0.2
            if bird[i]>=4:
                bird[i]=0
            bir=image[int(bird[i])]
            if start:
                bx[i]-=5
            if bx[i]<=-80:
                bx[i]=random.randint(1000,2000)
                by[i]=random.randint(0,810)
            if b.colliderect(p):
                die=True
            screen.blit(bir,(bx[i],by[i]))
            if brect.colliderect(b):
                touch.play()
                score+=1
                posx=brect.x
                posy=brect.y
                bl=True
                bullet=False
                bx[i]=random.randint(1200,2000)
                vibrate=True
            if bl:
                blc+=0.01
                if blc>=5:
                    blc=0
                    bl=False    
                showbl=blood[int(blc)]
                screen.blit(showbl,(posx,posy))
                posy+=0.5
        msg(35,True,f"SCORE: {score}",width/2,20,255,255,255)
        screen.blit(player,(x1,y1))
        if die:
            firec+=0.2
            if firec>=6:
                firec=0
            img=fire[int(firec)]
            screen.blit(img,(x1,y1))
            y1+=10
        if vibrate:
            vc+=1
            if vc==2:
                bgx-=vib
            if vc==4:
                bgx+=vib
            if vc==6:
                bgx-=vib
            if vc==8:
                vc=0
                bgx+=vib
                vibrate=False
        pygame.display.update()
    pygame.quit()
main()
