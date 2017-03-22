from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.config import Config


from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
pla_no =0
amntx = 100
amnty = 100
x1=0
y1=0
x2 =0
y2 =0
xz=0
yz=0
q =0
multx = 0
multy =Window.width*0.025
animsound = SoundLoader.load('anim.wav')
laddersound = SoundLoader.load('ladder.wav')
snakesound = SoundLoader.load('snake.wav')
winner = 0
Builder.load_string('''
<Simple>:
    the_label: _the_label
    label1:_label1
    orientation:'vertical'
    size:900,1000
    RelativeLayout:
        size_hint:1,0.9
        center_x:0
        center_y:0
        canvas.before:
                         
            Rectangle:
                
                source:'background.jpg'                
                size:root.width,root.height*0.9
                
        Label:
            id: _the_label
            size_hint: 0.1, 0.1
            center_x: 0
            center_y: 0
            
            bcolor: 0.8, 0.5, 0.5, 0.9
            canvas.before:
                Color:
                    rgba: self.bcolor
                    
                Rectangle:
                    pos: self.pos
                    size: self.size
                
        Label:
            id: _label1
            bcolor:0.1,0.55,0.55,0.9
            size_hint: 0.1, 0.1
            center_x: 0
            center_y: 0
               
            canvas.before:
                Color:
                    rgba: self.bcolor
                Rectangle:
                    pos: self.pos
                    size: self.size
     
    Button:
        text: '+++'
        size_hint:1,0.1          
        on_press:root.mainfunction()
''')
import random as rand



snin = [33,41,49,56,62,87,93,95,98]
snout = [6,20,9,53,5,16,73,75,64]
ladderin = [2,10,27,41,51,61,65,71,81]
ladderout =[37,32,46,68,79,84,91,100]
def snl(Score):
    global q
    diff =0
    for i in range(len(snin)-1):
        if(Score == snin[i]):
            diff = Score 
            Score = snout[i]
            q =1
            break
    for i in range(len(ladderin)-1):
        if(Score == ladderin[i]):
            diff = Score
            Score = ladderout[i]
            q =1
            break
    return Score,diff
        

class player:
    
   score = 0
    
   diff =0
   name = 0
   before =0
   def __init__(self,name):
       self.score = 0
       self.win = 0
       self.name = name
   def rolldice(self):
       global pla_no,winner
       self.before = self.score
       randominteger = rand.randint(1,6)
       self.score = self.score+randominteger
       
       if(self.score>100):
           self.score = self.score- randominteger
       elif(self.score == 100):
           winner = pla_no+1
           win = 1
           print(self.name+'won')
       print(self.name+':'+str(self.score))                     
       self.score,self.diff = snl(self.score)
       return 
   def updateanimparam(self):
       global x1,y1,x2,y2,xz,yz
       a = self.score
       
       dig0 = (a%10)
       a = a/10
       dig1 = (a%10)
       if(dig0 !=0):
           y2 = (dig1)*Window.height*0.9*0.1
           if(dig1%2):
               x2 = (10-dig0)*Window.width*0.1
           else:
               x2 = (dig0-1)*Window.width*0.1
       else:
           y2 = (dig1-1)*Window.height*0.9*0.1
           
           if(dig1%2):
               x2 = (9)*Window.width*0.1
           else:
               x2 = 0
    
    
       a = self.before
       dig0 = (a%10)
       a = a/10
       dig1 = (a%10)
       if(dig0 !=0):
           y1 = (dig1)*Window.height*0.9*0.1
           if(dig1%2):
               x1 = (10-dig0)*Window.width*0.1
           else:
               x1 = (dig0-1)*Window.width*0.1
       else:
           y1 = (dig1-1)*Window.height*0.9*0.1
           
           if(dig1%2):
               x1 = (9)*Window.width*0.1
           else:
               x1 = 0
               
       a = self.diff        
       dig0 = (a%10)
       a = a/10
       dig1 = (a%10)
       if(dig0 !=0):
           yz = (dig1)*Window.height*0.9*0.1
           if(dig1%2):
               xz = (10-dig0)*Window.width*0.1
           else:
               xz = (dig0-1)*Window.width*0.1
       else:
           yz = (dig1-1)*Window.height*0.9*0.1
           
           if(dig1%2):
               xz = (9)*Window.width*0.1
           else:
               xz = 0
               
       return
                







class Simple(BoxLayout):
    p1 = player('player1')
    p2= player('player2')
    
    the_label = ObjectProperty(None)
    label1 = ObjectProperty(None)
    sometext = NumericProperty(5)
    
        
    popup1 = Popup(title='******************************', content=Button(text = 'player 1 won \n start new game'), auto_dismiss=False,size = (Window.width,Window.height))
    popup2 = Popup(title='******************************', content=Button(text = 'player 2 won \n start new game'), auto_dismiss=False,size = (Window.width,Window.height))
    popup1.content.bind(on_press= popup1.dismiss)
    popup2.content.bind(on_press= popup2.dismiss)    
    
    def mainfunction(self):
        global pla_no,winner,q
        animation = Animation(pos=(0,0),duration = 0.00001)
        if(pla_no ==0):
            self.p1.rolldice()
            self.p1.updateanimparam()
        else:
            self.p2.rolldice()
            self.p2.updateanimparam()
        if(q==1):
            print("player 1",self.p1.before,self.p1.diff,self.p1.score)
            print("player 2",self.p2.before,self.p2.diff,self.p2.score)
        if(winner==0):
            self.animate()
            return
        elif(winner ==1):            
            pla_no = 0
            q=0
            winner =0
            x1 = x2=xz=y1=y2=yz =0
            self.p1.score = self.p2.score = self.p1.diff = self.p2.diff = self.p1.before = self.p2.before = 0
            animation.start(self.the_label)
            animation.start(self.label1)
            self.popup1.open()            
            return
        elif(winner ==2):           
            pla_no = 0
            q=0
            winner =0
            x1 = x2=xz=y1=y2=yz =0
            self.p1.score = self.p2.score = self.p1.diff = self.p2.diff = self.p1.before = self.p2.before = 0
            animation.start(self.the_label)
            animation.start(self.label1)
            self.popup2.open()   
            return
            
    def playsound(self):
        global animsound
        animsound.play()
        return

    def animate(self):
        global x1,y1,x2,y2,xz,yz,q,animsound,snakesound,laddersound,multx
        global pla_no
        x1 = x1+multx
        y1 = y1+multx
        xz = xz+multx
        yz = yz+multx
        x2 = x2+multx
        y2 = y2+multx
        
        if(pla_no ==0):
            if(q==0):
                
                anim = Animation(pos=(x1,y1))
                
                anim = anim+Animation(pos=(x2,y2),duration = 0.5)
                
                
                
                
              
                anim.start(self.the_label)
                
                
                print('from',(x1,y1),'to',(x2,y2))
                pla_no =1
                
            else:
                print('sanke/ladder')
                anim = Animation(pos=(x1,y1))
                anim += Animation(pos=(xz,yz),duration = 0.5)
                anim += Animation(pos=(x2,y2),duration = 0.5)
                anim.start(self.the_label)
               
                q=0
                pla_no =1
        else:
            if(q==0):
                pla_no =0
                anim = Animation(pos=(x1,y1))
                anim += Animation(pos=(x2,y2),duration = 0.5)
                print('from',(x1,y1),'to',(x2,y2))
                anim.start(self.label1)
            else:
                q=0
                anim = Animation(pos=(x1,y1))
                anim += Animation(pos=(xz,yz),duration = 0.5)
                anim += Animation(pos=(x2,y2),duration = 0.5)
                anim.start(self.label1)
                pla_no =0
                print('sanke/ladder')
        return        
    def restart(self,popup):
        global winner,q,pla_no
        pla_no = 0
        q=0
        winner =0
        x1 = x2=xz=y1=y2=yz =0
        self.p1.score = self.p2.score = self.p1.diff = self.p2.diff = self.p1.before = self.p2.diff = 0
        popup.dismiss()
class TApp(App):
    def build(self):
        Window.size = (450,500)
        return Simple()

TApp().run()
