import unittest
import Gradient as gd
import generowanieWieluGradientow as gwg
import numpy as np
import os


class SimpleFunctions(unittest.TestCase):#
    def test(self):
        self.assertFalse(False)
    def testRotatePointXY(self):
        point = 1.0,1.0
        expected = ['%.5f'%(e) for e in (0.0, (2**(0.5)))]
        self.assertEqual(expected,['%.5f'%(r) for r in gd.RotatePointXY(point,gd.CosAndSinFromDegrees(45.0))])
    def testExtendSqareEdgeByRotate(self):
        squareEdge = 1
        angle = 45
        expectedSquareEdge = '%.5f'%(2**(0.5))
        self.assertEqual(expectedSquareEdge,'%.5f'%(gd.ExtendSqareEdgeByRotate(squareEdge,gd.CosAndSinFromDegrees(angle))))
        angle = -45
        expectedSquareEdge = '%.5f'%(2**(0.5))
        self.assertEqual(expectedSquareEdge,'%.5f'%(gd.ExtendSqareEdgeByRotate(squareEdge,gd.CosAndSinFromDegrees(angle))))
        angle = 80
        self.assertEqual(str(1.15846),'%.5f'%(gd.ExtendSqareEdgeByRotate(squareEdge,gd.CosAndSinFromDegrees(angle))))
        angle = 175
        self.assertEqual(str(1.08335),'%.5f'%(gd.ExtendSqareEdgeByRotate(squareEdge,gd.CosAndSinFromDegrees(angle))))
    def testFillNdArraysBy(self):
        var = 135
        arr = np.ones((3,4,5))
        arr = gd.FillNdArraysBy(arr,var)
        self.assertEqual(135,arr[2,2,4])
    def testFillNdArraysBy135(self):
        arr = np.ones((3,4,5))
        arr = gd.FillNdArraysBy135(arr)
        self.assertEqual(135,arr[2,2,4])
    def testFillNdArrayElementInStep(self):
        var = 124
        arr = np.ones((3,4,5))
        step = 6
        arr = gd.FillNdArrayElementInStep(arr,var,step)
        self.assertEqual(124,arr[1,2,0])
    def testFillNdArrayElementBy124InStep6(self):
        arr = np.ones((3,4,5))
        arr = gd.FillNdArraysElementBy124InStep6(arr)
        self.assertEqual(124,arr[2,2,4])
    def testCalcRatio_integers(self):
        numTotal = 24
        self.assertEqual((6,4),gd.CalcRatio((3,2),numTotal))
    def testCalcRatio_fractions(self):
        numTotal = 26
        self.assertEqual((6,5),gd.CalcRatio((3,2),numTotal))
    def testMergeTwoImagesSetsIntoPairs(self):
        left = np.full((5,4,4),8)
        right = np.full((5,4,4),9)
        result = [8]*4+[9]*4
        self.assertEqual(result,list(gd.MergeTwoImagesSetsIntoPairs(left,right)[2,3,:]))
        
        
class GradientCreate():#unittest.TestCase
    def testShapeGradientWithLetter(self):
        gradient = gd.CreateGrayGradient(48,0,False)
        gradientWithLetter = gd.GradientWithLetter(gradient,36,'G',15)
        self.assertEqual(gradient.shape,gradientWithLetter.shape)
    def testPixelColorGradientWithLetter(self):
        gradient = gd.CreateGrayGradient(200,99)
        gradientWithLetter = gd.GradientWithLetter(gradient,120,'G',15)
        self.assertEqual(1,gradientWithLetter[72,100])
    def testCreateCircleOnGradient(self):
        gradient = gd.CreateGrayGradient(200,163)
        gradientC = gd.CreateCircleOn(gradient)
        self.assertEqual(0,gradientC[25,34])
    def testCreateCircleWithRadius(self):
        gradient = gd.CreateGrayGradient(200,23)
        gradientC = gd.CreateCircleOn(gradient,0.7)
        self.assertEqual(0,gradientC[80,33])
class ManyGradientsCreate():#unittest.TestCase
    def testCreateGrayGradient(self):
        angles = [3,78,94,175,192,266,291,349,90]
        gradients = [gd.CreateGrayGradient(200,angle,False) for angle in angles]
    def testCreateGrayGradientsAsNdArray(self):
        shape = (10,50,50)
        gradients = gwg.CreateGrayGradientsAsNdArray(shape)
        self.assertEqual((10,50,50),gradients.shape)
    def testShapeCreateLettersOnGradients(self):
        gradients = gwg.CreateGrayGradientsAsNdArray((10,50,50))
        gradientsWithLetters = gwg.CreateLettersOnGradients(gradients)
        self.assertEqual((10,50,50),gradientsWithLetters.shape)
    def testShapeCreateRandomCirclesOnGradients(self):
        gradients = gwg.CreateGrayGradientsAsNdArray((10,40,40))
        gradientsWithCircle = gwg.CreateRandomCirclesOn(gradients)
        self.assertEqual((10,40,40),gradientsWithCircle.shape)

#~ poniższe okazało się niepotrzebne, bo jest funkcja np.save
class GenerateAndSaveTrainingData(unittest.TestCase):
    
    
    def testGenerateBackground(self):
        createBackgroundFunc = np.ones((3,4,5))
        backGrd = gwg.GenerateDataUsingFunctions([createBackgroundFunc])
        self.assertEqual(1,backGrd[2,2,4])
    def testGenerateDataUsingCommonFunctions(self):
        commonFunctions = [np.ones((3,4,5)),gd.FillNdArraysBy135]
        diffFunctions = [gd.FillNdArraysElementBy124InStep6]
        basics = gwg.GenerateDataUsingFunctions(commonFunctions)
        diffs = gwg.ModifyDataUsingFunctions(basics,diffFunctions)
        self.assertEqual(135,basics[2,2,4])
        self.assertEqual(124,diffs[1,2,0])
        
    def testGenerateFileNames(self):
        pass
    def testSave4FilesByGenerateData(self):
        pass
        
    """
    def testIsFileGrayGradientsNdArray(self):
        gradients = gwg.CreateGrayGradientsAsNdArray((10,28,28))
        fileName = 'testData.dat'
        gwg.SaveGradients(gradients,fileName)
        try:
            f = open(fileName)
        except:
            self.assertTrue(False)
        else:
            f.close()
            os.remove(fileName)
            self.assertTrue(True)
    def testShapeAfterSaveAndOpenGradientsNdArray(self):
        gradients = gwg.CreateGrayGradientsAsNdArray((10,28,28))
        fileName = 'testData2.dat'
        gwg.SaveGradients(gradients,fileName)
        gradientsRead = gwg.OpenGradients(fileName)
        self.assertEqual(gradientsRead.shape,gradients.shape)
        os.remove(fileName)
    def testIsFileGradientsWithLettersNdArray(self):
        #~ savedFile = SaveGradients
        pass
    def testDivdeData(self):
        pass
    """
if __name__ == "__main__":
    unittest.main()
