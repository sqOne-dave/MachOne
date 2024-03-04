import pgzrun

WIDTH = 1280
HEIGHT = 960



def draw():
    screen.clear()
    screen.fill((255,255,255))
    color_rects()

def color_rects():
    r_anteil=0
    g_anteil=0
    b_anteil=0
    x_kor=0
    y_kor=0
    breite=1
    hohe=1
    #BOX=Rect((x_kor,y_kor),(breite,hohe))
    #farbe=r_anteil,g_anteil,b_anteil 
    #screen.draw.filled_rect(BOX,farbe)
    while b_anteil < 255:
        g_anteil= 0
        while g_anteil < 255:
            r_anteil = 0
            x_kor = 0
            while r_anteil < 255:
                r_anteil += 1
                farbe=r_anteil,g_anteil,b_anteil 
                x_kor += 1
                BOX=Rect((x_kor,y_kor),(breite,hohe))
                #print('r_anteil',r_anteil)
                screen.draw.filled_rect(BOX,farbe)
            g_anteil += 1
            y_kor += 1
        b_anteil += 1
        print('b_anteil: ',b_anteil)
        
                
pgzrun.go()
