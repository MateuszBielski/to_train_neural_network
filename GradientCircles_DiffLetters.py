import time as tm
import numpy as np
import Gradient as gd
import generowanieWieluGradientow as gwg

if __name__ == "__main__":
    #~ DataParameters
    num_train = 200
    num_test = None
    numToShow = 20
    #~ Generate
    start = tm.time()
    print('generowanie danych...')
    commonFunctions = [gwg.CreateGrayGradientsAsNdArray((num_train,28,28)),gwg.CreateRandomCirclesOn]
    diffFunctions = [gwg.CreateLettersOnGradients]
    
    train_labels = gwg.GenerateDataUsingFunctions(commonFunctions)
    train_images = gwg.ModifyDataUsingFunctions(train_labels,diffFunctions)
    stop = tm.time()
    print('wygenerowano dane w '+'%.5f'%(stop - start)+'s')
    #~ Show
    gwg.ShowGeneratedImages(train_images,numToShow)
    gwg.ShowGeneratedImages(train_labels,numToShow)
    #~ Save
    #~ time
