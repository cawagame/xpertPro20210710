import pygame
from pygame.locals import *
import sys,os,random
import itertools
def LoadImage(im):
    _dImg ={}

    for i in im:
        n = i.split('.')[0]
        _dImg[n] = pygame.image.load('image/' + i)
    return _dImg
def GeneNamTupe(na):
    while 1:
        nn = na+str(random.randrange(99))+str(random.randrange(99))+random.choice(['a','b','c','d','f'])
        if _dImgSur.get(nn)==None:return nn
_dImgSur =LoadImage(os.listdir('image/'))
def _Key(k):
    out =()
    d =0
    _k =k.count(1)
    if _k==0:return None
    return k.index(1)

class People:
    def __init__(self):
        self._aniImg =[ 'yellowbird-downflap', 'yellowbird-midflap', 'yellowbird-upflap']
        self.nuI    =0
    def ImYiel(self):

        itAn    =itertools.cycle([1,0,0,0,0,0])
        it =itertools.cycle([0,1,2,1])
        for i in itAn:

            if i==1:ib=next(it)

            img =self._aniImg[ib]
            self.nuI =img
            yield (img,ib)

class RectConfor:
    def __init__(self):
        ""
        self._posRect =[]
        self.sz =[50,50]
        self.szMax =[100,50]
        #self.vi =1
        self._posRect.append({'rect': [280, 130, 300, 200 ],'hb': 0, 'cl':1, 'xy': [0, 0]})
        self._posTube =[]
        self.MakeTupeB()

    def MakeTupeH(self):
        ""


    def MakeTupeB(self):
        c,ro=self._MkTuB(None,None,1)
        nn =random.randrange(5)
        if nn==0:
            if ro==0:ro=1
            else:ro=0

            self._MkTuB(c,ro,None)
    def _MkTuB(self,c=None,ro=None,sc=1):
        x, y, xs, ys = self._posRect[-1]['rect']

        if c==None:c =random.randrange(2)                      #couleur c0 =rouge  c1 =vert
        if ro ==None:ro = random.randrange(2)        #haut bas r0 =haut  r1=bas

        n ='pipe-green'
        if c==0:n='pipe-red'
        nn =GeneNamTupe(n)
        ns =_dImgSur[n]
        xn, yn = ns.get_size()
        if sc == 1: ns = pygame.transform.scale(ns, [xs, yn + 100])
        if ro==0:ns =pygame.transform.rotate(ns,180)


        xna,yna =ns.get_size()
        xnb,ynb =x,y+ys
        if ro==0:xnb,ynb =x,-yna+y

        self._posTube.append([nn,[xnb,ynb]])
        _dImgSur[nn] =ns
        return c,ro
    def MakeEnd(self):
        ""
        x, y, xs, ys = self._posRect[-1]['rect']
        if x + xs > 280:return

        hb,ec =y,ys
        ec =ec+random.randrange(0,30,10)
        r = random.randrange(3)
        d =random.randrange(2,5)
        if r == 0:
            a = int(hb - ec / d)
        elif r == 1:
            a = hb
        else:
            a = int(hb + ec / d)
        d = 50 + random.randrange(0, 80, 10)
        e = 80 + random.randrange(0, 30, 5)


        if a < 50: a = 50
        if a > 450: a = 450
        if a+e<60:
            e-=20
            a-=10
        self._posRect.append({'rect':[280,a,d,e],'hb':random.randrange(2),'cl':random.randrange(2),'xy':[0,0]})
        self.MakeTupeB()
    def MoveRec(self,data,vi=1):
        for i in range(len(data)):
            if type(data[i]) ==type({}):data[i]['rect'][0] -= vi
            else:data[i][1][0]-=vi
        if type(data[0])==type({}):x,y,xs,ys=  data[0]['rect']
        else:
            x,y=data[0][1]
            xs,ys=_dImgSur[data[0][0]].get_size()

        if x+xs<3:data.pop(0)





    def DispRect(self):
        out =[]
        for i in self._posRect:
            out.append({'typ':'rect','rect':i['rect'],'cl':(0,0,0)})
        return  out


class Menu:
    def __init__(self):
        self.ima ='message'
        self.rotastion =self.Rosta()
        #self.nn = GeneNamTupe('An' + self.ima)
        self._menuAni =[]
        for i in [-5,0,5]:
            nn = GeneNamTupe('An' + self.ima)
            self._menuAni.append(nn)
            _dImgSur[nn]=pygame.transform.rotate(_dImgSur[self.ima],i)
        a =self._menuAni[1]

        self._menuAni =self._menuAni[:1]+[a]+self._menuAni[1:]
        self._menuAni.append(self._menuAni[1])
        self._menuAni.append(self._menuAni[1])
        #print (self._menuAni)


        next((self.rotastion))

    def Centre(self,ima,d=2):
        sur =_dImgSur[ima]
        xs,ys =sur.get_size()
        return int(xs/d),int(ys/d)
    def Rosta(self):
        itAn = itertools.cycle([1, 0, 0, 0, 0, 0,0,0,0,0,0])
        it =itertools.cycle(self._menuAni)

        for i in itAn:
            if i==1:ib=next(it)
            yield ib

    def Display(self,ima=None):
        if ima==None:ima=self.ima

        return next(self.rotastion)
    def PrsKeyMode(self,prK):
        #print (_Key(prK))
        out =-1
        if _Key(prK)==98:

            out =0
        return out


class GameOver:
    def __init__(self):
        ""
        self.ima ='gameover'
        self.y0 =[1,0,0,0,0,0]
        self.y1=[1,1,1,1,0,0,0,0]
        self._YGmover =self._GmOver()
        next(self._YGmover)
    def _GmOver(self):
        ""
        it1 =itertools.cycle(self.y1)
        for i in it1:
            yield i
    def yDisplay(self):
        ""
        it0 =itertools.cycle(self.y0)
        ib =0
        for i in it0:
            if i ==1:ib =next(self._YGmover)
            yield ib



class VABird:
    def __init__(self):
        xb,yb =_dImgSur['background-night'].get_size()
        xc,yc =_dImgSur['base'].get_size()
        self._scrx =xb
        self._sol   =yb

        self.root  =pygame.display.set_mode([xb,yb+yc])

        self._bkDisp    =[300,580,860]
        self._bsDisp    =[300,580,860]

        self._modeJeux  =-1
        self._posROld   =[]

        self._dispRoot =[]
        self._birdPos=[70,200]             #pos de l oiseuax
        self.espace =0
        self._espace =-1
        self.bird =People()
        self.birdAni =self.bird.ImYiel()
        next(self.birdAni)
        self.confore =RectConfor()
        self.menu =Menu()
        self.GameOver =GameOver()
        self._ydisp =self.GameOver.yDisplay()
        next(self._ydisp)
        self.p          =   0
        self._p         =[]



    def _CalBack(self,data,vi=1):
        for i in range(len(data)):
            data[i] -=vi

    def _EffBack(self,data,p=1):
        if data[p]<-3:return True
        return False

    def _DisBack(self,img,data,y=0):
        for i in data:
            self._dispRoot.append([img,[i,y]])


    def Back(self,img,data,vi,y=0):
        self._CalBack(data, vi)
        if self._EffBack(data, 1):
            data.pop(0)
            data.append(data[0] + 280)

        self._DisBack(img,data,y)






    def DispSurface(self):
        for i in self._dispRoot:
            #print (i,type(i))
            if type(i)==type([]):self.root.blit(_dImgSur[i[0]],i[1])

            else:
                ""

                #if i['typ']=='rect':pygame.draw.rect(self.root,i['cl'],i['rect'],1)

    def DispBird(self):
        nn,p ='yellowbird-midflap',None
        if self.espace <0:nn,p =next(self.birdAni)
        if self.espace ==0:nn ='yellowbird-midflap'
        if self.espace>0:nn='yellowbird-downflap'
        self._birdPos[1] += self.espace
        if self._birdPos[1]<5:self._birdPos[1]=5
        if self._birdPos[1] > 480: self._birdPos[1] = 480
        #print (self.bird.nuI,nn,p)

        self._dispRoot.append([nn,self._birdPos])

    def Menu(self,data,pos,di=1):
        if di !=1:return
        self._dispRoot.append([data,pos])
        #self._dispRoot.append([self.menu.Display(),[10,10]])
    def GameOvr(self,di=1):
        ima = 'gameover'
        if di !=1:return
        iy =next(self._ydisp)
        if iy==1:self._dispRoot.append(['gameover',[50,400]])


    def Point(self):
        sP =str(self.p)
        if len(sP)==1:sP="0"+sP
        if len(sP)==2:sP="0"+sP
        if len(sP) == 3: sP = "0" + sP
        self.Menu(sP[0],[0,0])
        self.Menu(sP[1], [25, 0])
        self.Menu(sP[2], [50, 0])
        self.Menu(sP[3], [75, 0])

    def Collision(self,pos=None,data=None):
        xp,yp   =pos
        xp =xp+2
        yp =yp+2

        #print(self.confore._posRect)
        _p =0
        for i in range(len(self.confore._posTube)):

            out =[None,None,None,None]
            x,y     =self.confore._posTube[i][1]
            xs,ys =_dImgSur[self.confore._posTube[i][0]].get_size()
            if x>xp:out[0]=1
            if y+ys<yp:out[1]=1
            if x+xs<xp:out[2]=1
            if y>yp:out[3]=1
            nt      =self.confore._posTube[i]
            if out==[None,None,None,None]:
                self._modeJeux =-2
                #self.p -= 10
                #self._dispRoot.append({'typ':'rect','rect': [x, y, xs, ys], 'hb': 0, 'cl': [255,0,0], 'xy': [0, 0]})#out_.append(out)*
            if out == [None, 1, None, None]:
                _p =1
                self._dispRoot.append(
                {'typ': 'rect', 'rect': [x, y, xs, ys], 'hb': 0, 'cl': [0, 255, 250], 'xy': [0, 0]})
            if out == [None, None, None, 1]:
                _p=1
                self._dispRoot.append(
                {'typ': 'rect', 'rect': [x, y, xs, ys], 'hb': 0, 'cl': [0, 255, 250], 'xy': [0, 0]})
        #print (_p    )
        self.p +=_p






    def Mainloop(self):
        while 1:


            self.event =pygame.event.get()

            self._dispRoot =[]
            self.Back('background-night',self._bkDisp,1,0)

            self.DispBird()

            self.confore.MakeEnd()
            self.confore.MoveRec(self.confore._posRect,1)
            self.confore.MoveRec(self.confore._posTube,1)
            self._dispRoot=self._dispRoot+self.confore.DispRect()
            self._dispRoot=self._dispRoot+self.confore._posTube
            self.Back('base', self._bsDisp, 1,self._sol)

            if self._modeJeux==-1: self.Menu(self.menu.Display(),[10,10],1)
            if self._modeJeux==-2:
                self.Menu(self.menu.Display(),[10,10],1)
                self.GameOvr()
            #self._dispRoot.append([self.menu.Display(), [10, 10]])

            prK = pygame.key.get_pressed()
            self.ModeJeux(prK)
            if self._modeJeux>-1:self.Collision(self._birdPos, data=self.confore._posTube)
            self.Point()
            self.DispSurface()
            pygame.display.update()
            pygame.time.wait(10)

    def ModeJeux(self,prK):
        a =_Key(prK)

        #if a !=None:print (a)
        if a==41:self._modeJeux=-1
        if self._modeJeux in [-2,-1] :
            #self._modeJeux = self.menu.PrsKeyMode(prK)
            if _Key(prK) ==98 or pygame.mouse.get_pressed()[0]==True:

                self.__init__()
                self._modeJeux = 0

        if self._modeJeux==0:
            bkV     =1
            if a==44 or pygame.mouse.get_pressed()[0]==True:
                bkV =-1
                self._espace =0

            if bkV ==1 and -1<self._espace<50:
                bkV =0
                self._espace +=1

            self.espace =bkV






print (_dImgSur.keys())
root =VABird()
root.Mainloop()