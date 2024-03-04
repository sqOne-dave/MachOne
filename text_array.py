WIDTH = 3840
HEIGHT = 1080

x_kor = [(WIDTH/4),(WIDTH/4)*2,(WIDTH/4)*3]
y_kor = [HEIGHT/2,HEIGHT/2,HEIGHT/2]
c_kor = [(x_kor[0],y_kor[0]),(x_kor[1],y_kor[1]),(x_kor[2],y_kor[2])]

print(c_kor[1][0])


red = [255,2,3]
green = [4,255,5]
blue = [6,7,255]

c_farbe = [[red[0],green[0],blue[0]],[red[1],green[1],blue[1]],[red[2],green[2],blue[2]]]
print(c_farbe[0])
print(type(c_farbe[0]))
c_farbe[0][0] = 1 
print(c_farbe[0][0])
