import time as tm
import numpy as np
import Gradient as gd
import generowanieWieluGradientow as gwg

if __name__ == "__main__":
    #~ DataParameters
    num_train = 20
    size = 256
    num_test = None
    numToShow = 6
    #~ Generate
    start = tm.time()
    print('generowanie danych...')
    commonFunctions = [gwg.CreateGrayGradientsAsNdArray((num_train,size,size)),gwg.CreateLettersOnGradients]
    diffFunctions = [gwg.CreateRandomCirclesOn]
    
    train_labels = gwg.GenerateDataUsingFunctions(commonFunctions)
    train_images = gwg.ModifyDataUsingFunctions(train_labels,diffFunctions)
    merged_images = gd.MergeTwoImagesSetsIntoPairs(train_labels,train_images)
    stop = tm.time()
    print('wygenerowano dane w '+'%.5f'%(stop - start)+'s')
    #~ Save
    start = stop
    nameCommon = 'GradientLetters'
    nameDiff = 'DiffCircles'
    gwg.SaveNdArrayAsSeparatedJpgFiles(merged_images,'train_drawLetters/',nameCommon,nameDiff)
    stop = tm.time()
    print('zapisano dane w '+'%.5f'%(stop - start)+'s')
    #~ Show
    gwg.ShowGeneratedImages(merged_images,numToShow)
