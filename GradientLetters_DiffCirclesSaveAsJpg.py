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
    nameCommon = 'GradientLetters_'
    nameDiff = nameCommon+'_DiffCircles_'+str(num_train)+'_'+str(size)+'x'+str(size)
    nameCommon = nameCommon+str(num_train)+'_'+str(size)+'x'+str(size)
    print(nameCommon)
    print(nameDiff)
    
    #~ np.save(nameCommon,train_labels)
    #~ np.save(nameDiff,train_images)
    stop = tm.time()
    print('zapisano dane w '+'%.5f'%(stop - start)+'s')
    #~ Show
    gwg.ShowGeneratedImages(merged_images,numToShow)
