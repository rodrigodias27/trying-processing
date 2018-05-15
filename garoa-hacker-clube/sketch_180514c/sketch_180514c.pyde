


def setup():
    #size(400, 400)
    fullScreen()
    
def draw():
    background(0)
    strokeWeight(16)
    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r = 256*tan(((((frameCount**2)-(x*y)))/100.0+y)*TWO_PI)
            g = 256*cos(((frameCount+y)/50.0)*TWO_PI)
            b = 256*sin(((frameCount+x)/50.0)*TWO_PI)
            stroke(r, g, b)
            point(x,y)
            
def keyPressed():
    if key == 's':
        saveFrame("frame###.png")
