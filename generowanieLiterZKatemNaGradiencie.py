import numpy as np
from Gradient import CreateGradient,GradientWithLetter
import matplotlib.pyplot as plt
    
num_im = 25
edgeLenght = 28

#~ gradientWithLetter = GradientWithLetter(28,0,50,70,20,"C",15)
angles = np.random.randint(low = -80, high = 80,size=(num_im))
letters = np.random.randint(low = ord('A'),high = ord('z'),size=(num_im))
letters = [str(chr(l)) for l in letters]
colors = np.random.randint(255,size=(num_im*3)).reshape(num_im,3)
colorLabels = [','.join([str(s) for s in c]) for c in colors]
heights = np.random.randint(low = int(edgeLenght/3), high = int(1.2*edgeLenght),size=(num_im))
gradients = [CreateGradient(edgeLenght,colors[i]) for i in range(num_im)]
images = [GradientWithLetter(gradients[i],heights[i],letters[i],angles[i]) for i in range(num_im)]
#~ labels = [letters[i]+' '+colorLabels[i]+' a='+str(angles[i])+' h='+str(heights[i]) for i in range(num_im)]


