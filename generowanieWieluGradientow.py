import numpy as np
from Gradient import GradientWithLetter,CreateGrayGradient,CreateCircleOn
import matplotlib.pyplot as plt
    
num_im = 25
edgeLenght = 28

#~ gradientWithLetter = GradientWithLetter(28,0,50,70,20,"C",15)
def NotUsed():
    angles = np.random.randint(low = -80, high = 80,size=(num_im))
    letters = np.random.randint(low = ord('A'),high = ord('z'),size=(num_im))
    letters = [str(chr(l)) for l in letters]
    colors = np.random.randint(255,size=(num_im*3)).reshape(num_im,3)
    colorLabels = [','.join([str(s) for s in c]) for c in colors]
    heights = np.random.randint(low = int(edgeLenght/3), high = int(1.2*edgeLenght),size=(num_im))
    gradients = [CreateGradient(edgeLenght,colors[i]) for i in range(num_im)]
    images = [GradientWithLetter(gradients[i],heights[i],letters[i],angles[i]) for i in range(num_im)]
    #~ labels = [letters[i]+' '+colorLabels[i]+' a='+str(angles[i])+' h='+str(heights[i]) for i in range(num_im)]
    labels = [letters[i] for i in range(num_im)]

    plt.figure(figsize=(20,10))
    for i in range(50):
        plt.subplot(5,10,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        lab = ''#~ plt.imshow(images[i])
        if i%2 == 0:
            im = gradients[int(i/2)]
        else:
            im = images[int((i-1)/2)]
            lab = labels[int((i-1)/2)]
        plt.imshow(im)
        plt.xlabel(lab)
    plt.show()

def CreateGrayGradientsAsNdArray(shape):
    num_images,x,y = shape
    angles = np.random.randint(360,size = num_images)
    return np.array([CreateGrayGradient(x,angle) for angle in angles])
def CreateLettersOnGradients(gradients):
    num_im = gradients.shape[0]
    edgeLenght = gradients.shape[1]
    letters = [str(chr(l)) for l in np.random.randint(low = ord('A'),high = ord('z'),size=(num_im))]
    heights = np.random.randint(low = int(edgeLenght/3), high = int(1.2*edgeLenght),size=(num_im))
    angles = np.random.randint(low = -80, high = 80,size=(num_im))
    return np.array([GradientWithLetter(gradients[i],heights[i],letters[i],angles[i]) for i in range(num_im)])
    
def CreateRandomCirclesOn(gradients):
    num_im = gradients.shape[0]
    edgeLenght = gradients.shape[1]
    r = np.random.randint(low = 20, high = 100, size = (num_im))/100
    
    return np.array([CreateCircleOn(gradients[i],r[i]) for i in range(num_im)])
    
def SaveGradients(gradients,fileName):
    gradientsFile = open(fileName,'wb')
    gradientsFile.write(gradients.tobytes())
    gradientsFile.close()
    return None
def OpenGradients(fileName):
    gradientsFile = open(fileName,'rb')
    rawData = gradientsFile.read()
    gradientsFile.close()
    return rawData.frombuffer
    
def showGeneratedImages(x,y):
    num_imx,num_imy = x,y
    num_im = num_imx * num_imy
    grayGradients = CreateGrayGradientsAsNdArray((num_im,40,40))
    gradientsWithLetters = CreateLettersOnGradients(grayGradients)
    plt.figure(figsize=(20,10))
    for i in range(num_imx*num_imy):
        plt.subplot(num_imy,num_imx,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(gradientsWithLetters[i],cmap=plt.cm.binary)
    plt.show()
def SaveExampleImages():
    grayGradients = CreateGrayGradientsAsNdArray((90,40,40))
    gradientsWithLetters = CreateLettersOnGradients(grayGradients)
    np.save('gradLett10x9',gradientsWithLetters)
def SaveGradientsWithLetters(num,size):
    print('generowanie danych...')
    grayGradients = CreateGrayGradientsAsNdArray((num,size,size))
    gradientsWithLetters = CreateLettersOnGradients(grayGradients)
    print('dane wygenerowane')
    nameGray = 'gray_'+str(num)+'_'+str(size)+'x'+str(size)
    nameLetter = 'letters_'+str(num)+'_'+str(size)+'x'+str(size)
    np.save(nameGray,grayGradients)
    np.save(nameLetter,gradientsWithLetters)
    print('dane zapisane')
def SaveGradientsCircles(num,size)
    #~ print('generowanie danych...')
    #~ grayGradients = CreateGrayGradientsAsNdArray((num,size,size))
    #~ gradientsWithLetters = CreateLettersOnGradients(grayGradients)
    #~ print('dane wygenerowane')
    #~ nameGray = 'gray_'+str(num)+'_'+str(size)+'x'+str(size)
    #~ nameLetter = 'letters_'+str(num)+'_'+str(size)+'x'+str(size)
    #~ np.save(nameGray,grayGradients)
    #~ np.save(nameLetter,gradientsWithLetters)
    #~ print('dane zapisane')
def showSavedImages(fileName):
    images = np.load(fileName)
    num_imx,num_imy = 10,9
    num_im = num_imx * num_imy
    plt.figure(figsize=(20,10))
    for i in range(num_imx*num_imy):
        plt.subplot(num_imy,num_imx,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i],cmap=plt.cm.binary)
    plt.show()
    
if __name__ == "__main__":
    #~ showGeneratedImages(10,9)
    #~ showSavedImages('gradLett10x9.npy')
    #~ SaveExampleImages()
    SaveGradients(10000,28)
