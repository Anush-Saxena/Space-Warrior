try:
     import pygame as pg
     from tkinter import *
     from tkinter import messagebox
     import mysql.connector as msc
     import random
     import pickle
     import os
     run=True
except:
     print("These Libraries must be installed!")
     print("pygame")
     print("tkinter")
     print("mysql.connector")
     print("random")
     print("pickle")
     print("os")
     run=False

cmnd1=lambda : name("320x180+300+300"," Enter Name "," OK ",3,4,70,61,checkplr,1,240)
cmnd2=lambda : name("380x230+300+300"," Enter Name of \nThe Person "," FIND ",5,15,113,104,checkscr,2,250)    
# FOR TKINTER
def name(dimens,t_lab,t_but,w_but,lab_x,entr_y,but_y,cmnd,ht,but_x):
     global tplr,cont
     try:
          cont.destroy()
     except:
          pass
     cont=Tk()
     cont.geometry(dimens)
     cont.overrideredirect(True)
     cont.config(bg="#bdffdb")
     calls()
     lplr=Label(cont,width=13,height=ht,text=t_lab,bg="#bdffdb",fg="black",font="courier 23 bold")
     bplr=Button(cont,width=w_but,text=t_but,pady=-1,command=cmnd,bg='white',fg="black",font="courier 22 bold",bd=4)
     tplr=Entry(cont,width=12,bg='white',fg="black",font="courier 22 bold",bd=4)
     lplr.place(x=lab_x,y=14+40)
     tplr.place(x=20,y=entr_y+40)
     bplr.place(x=but_x,y=but_y+40)
     close=PhotoImage(master=cont,file="close.png")
     lc=Label(cont,width=1000,height=2,bg="black")
     bc=Button(cont,image=close,bg="black",command=lambda :cont.destroy(),activebackground="black",border=0)
     bc.place(x=3,y=3)
     lc.place(x=0,y=0)
     cont.mainloop()

def checklvl():
     global start_lev,level
     x=0
     start_lev=1
     for plr in players:
          if plr[0]==pname:
               x=1
               if plr[1]>759:
                    start_lev=2
               break
     if start_lev==1:
          start_game(ship1,enmy1,e_b1,e_b2,bullet_1,2,23,2)
     elif start_lev==2:
          try:
               _cont.destroy()
          except:
               pass
          def l_1():
               global level
               level=1
               _cont.destroy()
               start_game(ship1,enmy1,e_b1,e_b2,bullet_1,2,23,2)
          def l_2():
               global level
               _cont.destroy()
               level=2
               start_game(ship2,enmy2,e_b3,e_b4,bullet_2,3,25,3)
          bgcol="#f0f0f0"
          fgcol="green"
          _cont=Tk()
          _cont.geometry("600x420+300+300")
          _cont.overrideredirect(True)
          bg=PhotoImage(master=_cont,file="bg.png")
          lbg=Label(_cont,image=bg)
          btn1=Button(_cont,width=8,bg="black",bd=10,fg="white",command=l_1,text=" LEVEL-1 ",font="courier 27 bold")
          btn2=Button(_cont,width=8,bg="black",bd=10,fg="white",command=l_2,text=" LEVEL-2 ",font="courier 27 bold")
          btn3=Button(_cont,bg="black",bd=10,fg="white",command=lambda : _cont.destroy(),text="QUIT",font="courier 23 bold")
          close=PhotoImage(master=_cont,file="close.png")
          lc=Label(_cont,width=1000,height=2,bg="black")
          bc=Button(_cont,image=close,bg="black",command=lambda :_cont.destroy(),activebackground="black",border=0)
          bc.place(x=3,y=3)
          lc.place(x=0,y=0)
          lbg.place(x=0,y=0)
          btn1.place(x=38,y=220)
          btn2.place(x=362,y=220)
          btn3.place(x=241,y=308)
          _cont.mainloop()

def checkplr():
     global tplr,j,con,cur,players,cont,pname
     pname=tplr.get().strip()
     if len(pname)>0 and len(pname)<16:
          con=msc.connect(host="localhost",user="root",passwd=password,database="inv")
          cur=con.cursor()
          q="select * from invaders"
          cur.execute(q)
          players=cur.fetchall()
          cont.destroy()
          checklvl()
     else:
          cont.destroy()
          messagebox.showinfo(""," Name Must Be of Length 1 to 15")
          cmnd1()

def checkscr():
     global tplr,cont,pname
     pname=tplr.get().strip()
     if len(pname)>0 and len(pname)<16:
          cont.destroy()
          fetch("one")
     else:
          cont.destroy()
          messagebox.showinfo(""," Name Must Be of Length 1 to 15")
          cmnd2()

def fetch(x):
     global lscr,pname,l_scr
     con=msc.connect(host="localhost",user="root",passwd=password,database="inv")
     cur=con.cursor()
     if x=="one":
          q="select * from invaders"
     else:
          q="select * from invaders ORDER BY lv_1 DESC LIMIT 1"
          q_="select * from invaders ORDER BY lv_2 DESC LIMIT 1"
          cur.execute(q_)
          l_scr=cur.fetchall()
     cur.execute(q)
     lscr=cur.fetchall()
     if len(lscr)>0:
          if x=="one":
               for i in lscr:
                    if i[0]==pname:
                         dispscr(pname,i[1],i[2])
                         break
               else:
                    messagebox.showinfo(""," Name Not Found")
          elif x=="top":
               dispscr(lscr[0][0],lscr[0][1],lscr[0][2],"top")
     else:
          messagebox.showinfo("","No Entries Till Now!")

def dispscr(plrname,plrscr1,plrscr2,x="one"):
     global tplr,lscr,cont,players,pname,scrdisp
     try:
          scrdisp.destroy()
     except:
          pass
     dimens="500x195+300+300"
     scrdisp=Tk()
     scrdisp.overrideredirect(True)
     bgcol="#f0f0f0"
     fgcol="green"
     if x=="top":
          dimens="500x270+300+300"
          if len(l_scr)>0:
               l22=Label(scrdisp,width=10,text=l_scr[0][0],bg=bgcol,fg=fgcol,font="courier 23 bold")
               l23=Label(scrdisp,text=l_scr[0][1],bg=bgcol,fg=fgcol,font="courier 23 bold")
               l24=Label(scrdisp,text=l_scr[0][2],bg=bgcol,fg=fgcol,font="courier 23 bold")
          else:
               l22=Label(scrdisp,width=10,text=plrname,bg=bgcol,fg=fgcol,font="courier 23 bold")
               l23=Label(scrdisp,text=plrscr1,bg=bgcol,fg=fgcol,font="courier 23 bold")
               l24=Label(scrdisp,text=plrscr2,bg=bgcol,fg=fgcol,font="courier 23 bold")
          hsep2=Label(scrdisp,pady=-2,text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",bg=bgcol,fg='black',font="'' 20")
          hsep2.place(x=0,y=170)
          l22.place(x=0,y=210)
          l23.place(x=245,y=210)
          l24.place(x=390,y=210)
     scrdisp.geometry(dimens)
     scrdisp.config(bg=bgcol)
     l10=Label(scrdisp,width=6,text="Name",bg=bgcol,fg=fgcol,font="courier 23 bold")
     hsep1=Label(scrdisp,pady=-2,text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",bg=bgcol,fg='black',font="'' 20")
     l110=Label(scrdisp,pady=-1,text="Level\nI",bg=bgcol,fg=fgcol,font="courier 23 bold")
     l111=Label(scrdisp,pady=-1,text="Level\nII",bg=bgcol,fg=fgcol,font="courier 23 bold")
     l12=Label(scrdisp,width=10,text=plrname,bg=bgcol,fg=fgcol,font="courier 23 bold")
     l13=Label(scrdisp,text=plrscr1,bg=bgcol,fg=fgcol,font="courier 23 bold")
     l14=Label(scrdisp,text=plrscr2,bg=bgcol,fg=fgcol,font="courier 23 bold")
     close=PhotoImage(master=scrdisp,file="close.png")
     lc=Label(scrdisp,width=1000,height=2,bg="black")
     bc=Button(scrdisp,image=close,bg="black",command=lambda :scrdisp.destroy(),activebackground="black",border=0)
     bc.place(x=3,y=3)
     lc.place(x=0,y=0)
     vsep=Label(scrdisp,width=0,text="",bg="black",font="'' 160 ")
     vsep_=Label(scrdisp,width=0,text="",bg="black",font="'' 160 ")
     hsep1.place(x=0,y=90)
     vsep.place(x=202,y=30)
     vsep_.place(x=350,y=30)
     l10.place(x=40,y=50)
     l110.place(x=229,y=35)
     l111.place(x=377,y=35)
     l12.place(x=0,y=130)
     l13.place(x=245,y=130)
     l14.place(x=390,y=130)
     scrdisp.mainloop()

def close_it(master,col="black"):
     global close
     close=PhotoImage(master=master,file="close.png")
     lc=Label(master,width=1000,height=2,bg=col)
     bc=Button(master,image=close,bg=col,command=lambda :master.destroy(),activebackground=col,border=0)
     bc.place(x=3,y=3)
     lc.place(x=0,y=0)

# FOR GAME

def _images():
     global ship1,ship2,bg,enmy1,enmy2,exp,bullet_1,bullet_2,e_b1,e_b2,e_b3,e_b4,khatam,info
     ship1=pg.image.load("1.png")
     ship2=pg.image.load("11.png")
     bg=pg.image.load("8.jpg")
     enmy1=pg.image.load("enmy1.png")
     enmy2=pg.image.load("enmy2.png")
     exp=pg.image.load("explosion.png")
     bullet_1=pg.image.load("bullet-1.png")
     bullet_2=pg.image.load("bullet-2.png")
     e_b1=pg.image.load("b-1.png")
     e_b2=pg.image.load("b-2.png")
     e_b3=pg.image.load("b-3.png")
     e_b4=pg.image.load("b-4.png")
     khatam=pg.image.load("khatam.jpg")

def _music():
     global bgmusic,eappear,eshoot,sshoot,sdamage,bclash,edie,sdie
     bgmusic=pg.mixer.Sound("bg.wav")
     eappear=pg.mixer.Sound("eappear.wav")
     eshoot=pg.mixer.Sound("eshoot.wav")
     sshoot=pg.mixer.Sound("sshoot.wav")
     sdamage=pg.mixer.Sound("sdamage.wav")
     bclash=pg.mixer.Sound("bclash.wav")
     edie=sdie=pg.mixer.Sound("killed.wav")

def _main_(_ship,_enmy,_eb1,_eb2,_bullet,_scrinc,_health_dec,_shealth_dec):
     global dispship,dispe,hship,wship,henmy,wenmy,xinc,ship,enmy,eb1,eb2,bullet,scrinc,w_eb,health_dec,shealth_dec
     ship,enmy,eb1,eb2,bullet,scrinc,health_dec,shealth_dec=_ship,_enmy,_eb1,_eb2,_bullet,_scrinc,_health_dec,_shealth_dec
     dispship=gwin.blit(ship,(xship,yship))
     hship=dispship[3]
     wship=dispship[2]
     dispe=gwin.blit(enmy,(xenmy,yenmy))
     henmy=dispe[3]
     wenmy=dispe[2]
     dispeb=gwin.blit(eb1,(0,0))
     w_eb=dispeb[2]
     xinc=30+wenmy

def disp_ship():
     global xship,yship
     if (keys[pg.K_UP] or keys[pg.K_w]) and yship>=300:  #(htgw-100)/2
          yship-=vship
     elif (keys[pg.K_DOWN]or keys[pg.K_s]) and yship<htgw-dispship[3]-8:
          yship+=vship
     elif (keys[pg.K_LEFT] or keys[pg.K_a]) and xship>0:
          xship-=vship
     elif (keys[pg.K_RIGHT] or keys[pg.K_d]) and xship<wtgw-wship+10:
          xship+=vship

def disp_enmy():
     global r,ecnt,lifeline
     while r<len(ecoord):
          e=ecoord[r]
          if e[0]<-1  or e[0]>635:
               e[2]*=-1
               e[1]+=80
          e[0]-=(e[2]*venmy)        
          gwin.blit(enmy,(e[0],e[1]))
          if e[1]>750:
               ecoord.pop(r)
               lifeline-=1
               r-=1
               ecnt-=1
          r+=1

def dl():
     global xenmy
     dl=random.randint(0,4)
     xenmy=enmy_dl[dl]
     
def my_shoot():
     global bcnt,b_set,b_rounds
     k=0
     if i==b_set:
          bcnt=100
     if (keys[pg.K_f] or keys[pg.K_RCTRL]) and i%30==0 and bcnt>0:
          bcnt-=1
          if bcnt==0:
               b_rounds-=1
               b_set=i+800
          l.append(dispship)
          xbullet=l[0][0]
          ybullet=l[0][1]
          l.pop()
          bcoord.append([xbullet+(wship/2)-10,ybullet-10])
          sshoot.play(fade_ms=360)
     while k <len(bcoord):
          if bcoord[k][1]<=-6:
               bcoord.pop(k)
               k-=1
          k+=1
     for m in bcoord:
          m[1]-=1
          gwin.blit(bullet,(m[0],m[1]))

def e_shoot():
     ebcnt,x=0,0
     ply=0
     while i%(200 or 250)==0 and ebcnt<len(ecoord):                                                                  
          m=ecoord[ebcnt]
          z=random.randint(0,2)
          u=[[m[0]+wenmy/2 -12,m[1]+henmy-6],[m[0]+1,m[1]+38],[m[0]+51,m[1]+38]]
          eb.append(u[z])
          ebcnt+=1
          if ply==0:
               eshoot.play()
               ply=1
     while x<len(eb):
          eb[x][1]+=1
          if eb[x][1]+54<htgw:
               if i%2==0:
                    gwin.blit(eb1,(eb[x][0],eb[x][1]))
                    
               else:
                    gwin.blit(eb2,(eb[x][0],eb[x][1]))
               x+=1
          else:
               eb.pop(x)

def b_clash():
     global scr
     s=0
     while s<len(bcoord):
          m=bcoord[s]
          e=0
          while e<len(eb):
               o=eb[e]
               if (o[1]+5>m[1]+1 and o[1]+5<m[1]+28) or (o[1]+55>m[1]+1 and o[1]+55<m[1]+28):
                    if (o[0]+5>m[0] and o[0]+5<m[0]+14) or (o[0]+w_eb-5>m[0] and o[0]+w_eb-5<m[0]+14):
                         bcoord.pop(s)
                         eb.pop(e)
                         s-=1
                         e-=1
                         bclash.play()
                         scr+=1
                         break
               e+=1
          s+=1

def my_hit():                                                    # enemy has been damaged/hitted.
     global eship,bhit,h_mar,henmy,wenmy,scr,ecnt
     while eship<len(ecoord):
          e=ecoord[eship]
          bhit=0
          while bhit <len(bcoord):
               b=bcoord[bhit]
               if (b[0] >e[0]+h_mar and b[0]<e[0]+wenmy-h_mar) or (b[0]+10>e[0]+h_mar and b[0]+10<e[0]+wenmy-h_mar):
                    if (b[1]>e[1] and b[1]<e[1]+henmy-5) or (b[1]+23>e[1] and b[1]+23<e[1]+henmy-5):  # 10,23=width,height bullet
                         bcoord.pop(bhit)                              
                         bhit-=1
                         e[3]+=1
                         if e[3]==2:
                              e_exp.append([e[0],e[1],i+25])
                              ecoord.pop(eship)
                              eship-=1
                              edie.play()
                              ecnt-=1
                              scr+=scrinc
                         else:
                              scr+=1
                         break
               bhit+=1
          eship+=1
     m=0
     x=e_exp
     while m<len(x):
          gwin.blit(exp,(x[m][0],x[m][1]))
          if x[m][2]<i:
               e_exp.pop(m)
               m-=1
          m+=1          

def e_hit():                                                     #my ship has been damaged.
     global health
     e=0
     while e<len(eb):
          x=eb[e]
          if x[0]+5>xship+s_mar and x[0]+5<xship+wship-s_mar or x[0]+w_eb-5>xship+s_mar and x[0]+w_eb-5<xship+wship-s_mar:
               if x[1]+5>yship+2 and x[1]+5<yship+hship-2 or x[1]+55>yship+2 and x[1]+55<yship+hship-2:
                    eb.pop(e)
                    health-=shealth_dec
                    sdamage.play()
                    e-=1
          e+=1

def collision():
     global ecnt,health
     x=0
     while x<len(ecoord):
          e=ecoord[x]
          if (e[0]>xship and e[0]<xship+wship-c_mar) or (e[0]+wenmy>xship and e[0]+wenmy<xship+wship-c_mar):
               if (e[1]>yship+c_mar and e[1]<yship+hship) or (e[1]+henmy>yship+c_mar and e[1]<yship+hship):
                    ecoord.pop(x)
                    sdamage.play()
                    health-=health_dec
                    ecnt-=1
                    x-=1
          x+=1

def all_text():
     s=font.render("SCORE",True,(255,255,255))
     s1=font.render(str(scr),True,(255,255,255))
     h=font.render("HEALTH",True,(255,255,255))
     hperc=font.render(str(health)+"%",True,(255,255,255))
     lfln=font.render("LIFELINE",True,(255,255,255))
     r1=font.render("ROUNDS",True,"white")
     r2=font.render(str(b_rounds),True,"white")
     r3=font.render("LOADED",True,"white")
     r4=font.render("BULLETS",True,"white")
     r5=font.render(str(bcnt),True,"white")
     gwin.blit(lfln,(713,20))
     gwin.blit(h,(717,150))
     gwin.blit(hperc,(746,293))
     gwin.blit(s,(725,400))
     gwin.blit(s1,(760,435))
     gwin.blit(r1,(714,530))
     gwin.blit(r2,(770,570))
     gwin.blit(r3,(715,620))
     gwin.blit(r4,(711,650))
     gwin.blit(r5,(750,690))
     
     pg.draw.rect(gwin,(255,165,0),(715,70,130,60))
     for x in range(lifeline):
          pg.draw.rect(gwin,(0,255,255),(725+40*x,80,30,40))
     
     pg.draw.rect(gwin,(50,0,50),(719,200,120,70))
     pg.draw.rect(gwin,(0,255,255),(729,210,health,50))
     pg.draw.line(gwin,(255,255,255),(wtgw+7,0),(wtgw+7,htgw),3)

def calls():
     global eship,r,i,run,ecnt,gwin,eship,r,keys,scr,dispship,health,lifeline,bcoord,ecoord,eb,l
     global pg,wtgw,htgw,run,font,xship,yship,xenmy,yenmy,bcnt,b_rounds,b_set,venmy,vship,enmy_dl
     global h_mar,e_exp,c_mar,s_mar
     pg.init()
     wtgw,htgw=700,800
     run=True
     font=pg.font.Font("freesansbold.ttf",30)

     _images()
     _music()

     health=0
     lifeline=3

     xship,yship=300,600
     xenmy,yenmy=random.randint(50,330),75
     scr=0
     i,ecnt,bcnt,b_set,b_rounds=0,0,100,IntVar(),7
     venmy=1.4
     vship=1.7
     bcoord,ecoord,eb,l=[],[],[],[]

     enmy_dl=[20,120,220,500,600]
     e_exp=[]                                   #show image of explosion

     h_mar=15          #hitting margin
     c_mar=15          #collision margin
     s_mar=8           #ship1 
     #   to take width of ship1 , enemy
     #bcnt=bullet count        bcoord=coordinates of bullets

def start_game(_ship,_enmy,_eb1,_eb2,_bullet,_scrinc,_health_dec,_shealth_dec):
     global eship,r,i,run,ecnt,gwin,eship,r,keys,scr,dispship,health,lifeline,bcoord,ecoord,eb,l
     gwin=pg.display.set_mode((wtgw+150,htgw))
     bgmusic.play(loops=-1)
     _main_(_ship,_enmy,_eb1,_eb2,_bullet,_scrinc,_health_dec,_shealth_dec)
     j=0
     while run:
          pg.time.delay(-1)
          eship,r=0,0
          i+=1
          gwin.blit(bg,(0,0))
          if health<0 and lifeline>0:
               health+=100
               lifeline-=1
          if lifeline<0 or health<0 or (b_rounds<0 and len(bcoord)==0):
               gwin.blit(exp,(xship,yship))
               gwin.blit(khatam,(0,0))
               run=False
               bgmusic.stop()
          else:
               dispship=gwin.blit(ship,(xship,yship))
          keys=pg.key.get_pressed()
          
          my_shoot()                                        # for   My   Bullets
          if i%50==0:
               e_cnt=random.randint(4,5)
               if ecnt<e_cnt:                 # for enemy ship
                    eappear.play()
                    dl()                                               #dl=drop location
                    z=random.randint(0,2)
                    ecoord.append([xenmy,yenmy*z,(-1)**z,0])       # xenmy= x-coord, yenmy= y-coord , 1 is for speed multiplier
                    ecnt+=1                                                             # 0 is for the no. of bullets hitted on
          disp_enmy()
          e_shoot()          #enemy bullets
          
          if len(eb)>0 and len(bcoord)>0:
               b_clash()
          my_hit()                                  # bullets hitting
          collision()
          disp_ship()
          e_hit()
          all_text()
          
          for ev in pg.event.get():
               if ev.type==pg.QUIT:
                    run=False
                    bgmusic.stop()
          pg.display.update()
          if not run and (lifeline<0 or health<0 or (b_rounds<0 and len(bcoord)==0)):
          	   pg.time.wait(3000)

     pg.display.quit()

     for name in players:
          if name[0]==str(pname):
               j=1
               if start_lev==1:
                    if name[1]<scr:
                         q1="update invaders set lv_1={} where name='{}'".format(scr,name[0])
                         cur.execute(q1)
                    break
               elif start_lev==2:
                    if level==1 and name[1]<scr:
                         q1="update invaders set lv_1={} where name='{}'".format(scr,name[0])
                         cur.execute(q1)
                    elif level==2 and name[2]<scr:
                         q1="update invaders set lv_2={} where name='{}'".format(scr,name[0])
                         cur.execute(q1)
                    break
          else:
               j=0
     if j==0:
          q1="insert into invaders values('{}',{},0)".format(pname,scr)
          cur.execute(q1)
     con.commit()
     con.close()     

def __main__():
     root=Tk()
     #   wtmw x htmw     color=  #cdfcfc   or   #bdffdb
     def quit_all():
          try:
               cont.destroy()
          except:
               pass
          try:
               _cont.destroy()
          except:
               pass
          try:
               scrdisp.destroy()
          except:
               pass
          root.destroy()
     root.geometry("1080x805+50+10")
     root.configure(bg="#cdfcfc")
     root.overrideredirect(True)
     close=PhotoImage(master=root,file="close.png")
     #root.title(" MODERN SPACE WARRIOR ")
     l1=Label(root,bg="#cdfcfc",fg="purple",text="MODERN  SPACE  WARRIOR\nWELCOMES  YOU",font="algerian 60 underline")
     b1=Button(root,command=cmnd1,width=5,pady=0,bd=15,text=" PLAY ",bg="black",fg="white",font="courier 40 bold italic")
     b2=Button(root,command=cmnd2,width=11,pady=0,bd=15,text=" SEE SCORES ",bg="black",fg="white",font="courier 40 bold italic")
     b3=Button(root,command=lambda : fetch("top"),width=11,pady=0,bd=15,text=" BEST SCORE ",bg="black",fg="white",font="courier 40 bold italic")
     b4=Button(root,command=start_info,width=5,bd=15,text="ABOUT",bg="black",fg="white",font="courier 40 bold")
     b5=Button(root,command=quit_all,width=5,pady=0,bd=10,text=" QUIT ",bg="black",fg="white",font="forte 30")
     lc=Label(root,width=1000,height=2,bg="black")
     bc=Button(root,image=close,bg="black",command=quit_all,activebackground="black",border=0)
     bc.place(x=3,y=3)
     lc.place(x=0,y=0)
     l1.place(x=42,y=75)
     b1.place(x=53,y=310)
     b2.place(x=249,y=441)
     b3.place(x=637,y=572)
     b4.place(x=53,y=572)
     b5.place(x=450,y=710)

     root.mainloop()

def start_info():
     _root=Tk()
     _root.overrideredirect(True)
     _root.geometry("1050x819+100+0")
     info=PhotoImage(master=_root,file="info.png")
     canv=Canvas(_root,width=1050,height=789)
     canv.create_image(0,0,anchor=NW,image=info)
     canv.place(x=0,y=30)
     close_it(_root,"purple")
     _root.mainloop()

def chkpwd():
     global password
     try:
          pfile=open("main.txt","rb")
          size=os.stat("main.txt")
          if size.st_size>0:
               try:
                    records=pickle.load(pfile)
                    pfile.close()
               except:
                    pfile.close()
                    records=[]
                    os.remove("main.txt")
               if len(records)>0:
                    password=records[0]
                    try:
                         con=msc.connect(user="root",host="localhost",passwd=password)
                         con.close()
                         __main__()
                    except:
                         os.remove("main.txt")
                         chkpwd()
               else:
                    chkpwd()
          else:
               pfile.close()
               os.remove("main.txt")
               chkpwd()
     except (FileNotFoundError , EOFError):
          pfile=open("main.txt","wb")
          def lenchk():
               global password
               if len(tp.get())>0:
                    z.append(tp.get())
                    password=tp.get()
                    pickle.dump([password],pfile)
                    pfile.close()
                    pcont.destroy()
               else:
                    pcont.destroy()
                    messagebox.showinfo("","Enter your MySQL Password")
                    chkpwd()
          z=[]
          pcont=Tk()
          pcont.geometry("450x240+300+300")
          pcont.config(bg="#bdffdb")
          pcont.overrideredirect(True)
          lp=Label(pcont,text="Enter PASSWORD of your \nMySQL Server",bg="#bdffdb",fg="black",font="courier 23 bold")
          bp=Button(pcont,width=3,text="OK",pady=-1,command=lenchk,bg='white',fg="black",font="courier 22 bold",bd=4)
          tp=Entry(pcont,width=14,bg='white',fg="black",font="courier 22 bold",bd=4,show="*")
          close_it(pcont)
          lp.place(x=15,y=54)
          tp.place(x=40,y=157)
          bp.place(x=330,y=146)
          pcont.mainloop()
          if len(z)>0:
               try:
                    con=msc.connect(user="root",host="localhost",passwd=password)
                    cur=con.cursor()
                    q="create database if not exists inv"
                    cur.execute(q)
                    con.commit()
                    q="use inv"
                    cur.execute(q)
                    con.commit()
                    q="create table if not exists invaders(name varchar(15) primary key,lv_1 int,lv_2 int)"
                    cur.execute(q)
                    con.commit()
                    con.close()
                    __main__()
               except ValueError:
                    messagebox.showerror(""," Wrong Password ")
                    os.remove("main.txt")
                    chkpwd()
          else:
               pfile.close()
               os.remove("main.txt")

if __name__=="__main__" and run:
     chkpwd()
