global height, width, N, bdict, i
bdict = {}

height = 400
width = 400
N = 800 # number of circles
i = 0


def setup():
    global a0,x0,y0,r0
    size(height,width)
    background(255)
    a0 = 100 # Radius of the disc
    x0 = 200
    y0 = 200 # centre of the disc



class Bubbles:
    """
    Class Bubbles generates N filled circles 
    """
    h = height
    w = width

    def __init__(self,x0,y0,r0):
    
        self.x = x0
        self.y = y0
        self.r = r0
        
    def __str__(self):
        return( str(self.x) +" " + str(self.y) + " " + str(self.r))
    
    
    def render(self):
        fill(255,0,0,random(255))
        circle(self.x,self.y,self.r)
            
    def overlap(self,b2):
        x1 = self.x
        y1 = self.y
        r1 = self.r
        x2 = b2.x
        y2 = b2.y
        r2 = b2.r
        return(sqrt (sq(x1-x2) + sq(y1 -y2)) < abs(r1 + r2)/2.0)
    
def collision(b,b1):
    for num, bub in b.items():
        if (b1.overlap(bub)):
            return False
    return True
  
def draw():
    global N, bdict, i
    r0 = random(5,10)
    x = random(x0 -a0, x0+a0)
    y = random(y0-a0, y0+a0)
    
    d = sqrt(sq(x0-x) + sq(y0-y))
# Find if the points lie within a circle   
    if d < a0:
        next = Bubbles(x,y,r0)
        if (collision (bdict,next)):
            next.render() 
            bdict[i] = next
            i = i+1

        print(i)
    if i == N:
        noLoop()
