from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import math

def CosAndSinFromDegrees(angle):
    Fi = math.radians(angle)
    return math.cos(Fi),math.sin(Fi)
def RotatePointXY(point,CosSinFi):
    x,y = point
    cosFi,sinFi = CosSinFi
    x_rot,y_rot = x * cosFi - y * sinFi ,  x * sinFi + y * cosFi 
    return (x_rot,y_rot)
    
def ExtendSqareEdgeByRotate(edge,cosSinFi):
    #krawędź należy do kwadratu, którego środek leży w punkcie 0,0. Krawędzie kwadratu są poziome i pionowe
    #kwadrat ten jest obracany wokół punktu 0,0
    #Na obróconym kwadracie należy opisać nowy kwadrat, który znów będzie miał poziome i pionowe krawędzie
    pointToRotate = (edge/2,edge/2)
    rotatedPoint = max([abs(xy) for xy in RotatePointXY(pointToRotate,cosSinFi)])
    #szukaną wielkość uzyskamy z większej z nowych wartości
    extendedEdge = 2*rotatedPoint
    return extendedEdge 
    
def CreateColorGradient(edgeLenght,rgb):
    a = edgeLenght
    im1 = Image.new('RGBA', (a,a), (0,0,0,0))
    pixArray2 = np.array(im1)
    r,g,b = rgb
    for x in range(a):
        for y in range(a):
            G = int(x*g/a)
            B = int(y*b/a)
            pixArray2[y,x] = (r,G,B,255) # alfa musi być 255 bo dla zera pyplot nie widzi, w przeciwieństwie do Pil. Image.show()
    #~ return 
    return pixArray2
    
def CreateGrayGradient(edgeLenght,angle,usingImageNew = True):
    a = edgeLenght
    cosSinFi_L = CosAndSinFromDegrees(angle)
    e = math.ceil(ExtendSqareEdgeByRotate(a,cosSinFi_L))
    cosSinFi_R = CosAndSinFromDegrees(-angle)
    try:
        pixArray = np.zeros((e,e))
    except:
        print('error in np.zeros with angle,e',angle,e)
    for x in range(e):
        for y in range(e):
            pixArray[x,y] = int(255 * y/e)
    #~ print(pixArray)
    if usingImageNew:
        im = Image.new('L',(a,a),(255,))
        pixRotatedGradient = np.array(im)
    else:
        pixRotatedGradient = np.zeros((a,a))
    try:
        for x in range(a):
            for y in range(a):
                x0,y0 = x - a/2, y - a/2 # przesuwamy środek kwadratu do punktu 0,0
                Xrotated,Yrotated = RotatePointXY((x0,y0),cosSinFi_R)
                Xrotated,Yrotated = math.floor(Xrotated + e/2),math.floor(Yrotated + e/2)
                if Xrotated >= e:
                    Xrotated = e - 1
                if Xrotated < 0:
                    Xrotated = 0
                if Yrotated >= e:
                    Yrotated = e - 1
                if Yrotated < 0:
                    Yrotated = 0
                color = pixArray[Xrotated,Yrotated]
                pixRotatedGradient[x,y] = color
    except:
        print('error in for loop with angle ',angle,Xrotated,Yrotated)
    return pixRotatedGradient
    
def CreateCircleOn(background,r = 1.0):
    mode = 'L'
    if len(background) == 3:
        if background[2] == 4:
            mode = 'RGBA'
        if background[2] == 3:
            mode = 'RGB'
    
    im = Image.fromarray(background,mode)
    if (r <= 0):
        return np.array(im)
    if (r > 1.0):
        r = 1.0
    a,b = im.size
    dx,dy = [d*(1-r)/2 for d in [a,b]]
    x1,y1,x2,y2 = dx,dy,a-dx,b-dy
    ImageDraw.Draw(im).ellipse((x1,y1,x2,y2))
    return np.array(im)
        
def GradientWithLetter(pixArray,h,Letter,angle):
    mode = 'L'
    if len(pixArray) == 3:
        if pixArray[2] == 4:
            mode = 'RGBA'
        if pixArray[2] == 3:
            mode = 'RGB'
    
    im = Image.fromarray(pixArray,mode)
    a,b = im.size
    imDraw = ImageDraw.Draw(im)
    #~ h = 20
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', h)

    txt = Image.new('L',(a,b),(0))
    d = ImageDraw.Draw(txt)
    c1 = int(a/2-h/3)
    c2 = int(a/2-h/2)
    d.text((c1,c2), Letter, font=fnt, fill=(255))

    txt = txt.rotate(angle,expand = 1)
    txt_width,txt_height = txt.size
    im_width,im_height = im.size
    l_margin,top_margin = int((txt_width - im_width)/2),int((txt_height - im_height)/2)
    txt = txt.crop((l_margin,top_margin,l_margin+im_width,top_margin + im_height))
    imDraw.bitmap((0,0),bitmap=txt)
    #~ return im
    return np.array(im)

def FillNdArraysBy(arr,var):
    shp = arr.shape
    return np.array([var]*arr.size).reshape(shp)
def FillNdArraysBy135(arr):
    shp = arr.shape
    return np.array([135]*arr.size).reshape(shp)

def FillNdArrayElementInStep(arr,var,step):
    shp = arr.shape
    arrRes = arr.reshape(arr.size,)
    arrRes[::step] = var
    arrRes = arrRes.reshape(shp)
    return arr
def FillNdArraysElementBy124InStep6(arr):
    shp = arr.shape
    arrRes = arr.reshape(arr.size,)
    arrRes[::6] = 124
    arrRes = arrRes.reshape(shp)
    return arr
def CalcRatio(ratio,numTotal):
    rat_x,rat_y = ratio
    rat_xy = rat_x*rat_y
    c = (numTotal/rat_xy)**(0.5)
    y = math.ceil(rat_y*c)
    x = math.floor(rat_x*c)
    #~ x,y = rat_x*c,rat_y*c
    return (x,y)
    
def MergeTwoImagesSetsIntoPairs(arrL,arrR):
    if arrL.shape != arrR.shape: return
    return np.concatenate((arrL,arrR),axis = -1)
    

if __name__ == "__main__":
    grayGradient = CreateGrayGradient(200,23)
    #~ gradientWithLetter = GradientWithLetter(grayGradient,120,'G',-35)
    #~ colors = gradientWithLetter[:,100]
    #~ print(colors)
    #~ gradientWithLetter = Image.fromarray(gradientWithLetter,'L')
    #~ gradientWithLetter.show()
    #~ point = (10,0)
    #~ pointRotated = '\n'.join([' '.join(['%.3f'%(c) for c in RotatePointXY(point,CosAndSinFromDegrees(a))]) for a in range(0,270,5)])
    #~ print(pointRotated)
    gradientC = CreateCircleOn(grayGradient,0.7)
    print(gradientC[80,33])
    gradientC = Image.fromarray(gradientC,'L')
    gradientC.show()
    
