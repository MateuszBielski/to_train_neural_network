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
    
        
class GradientCreate(unittest.TestCase):#
    def testShapeGradientWithLetter(self):
        gradient = gd.CreateGrayGradient(48,0,False)
        gradientWithLetter = gd.GradientWithLetter(gradient,36,'G',15)
        self.assertEqual(gradient.shape,gradientWithLetter.shape)
    def testPixelColorGradientWithLetter(self):
        gradient = gd.CreateGrayGradient(200,99)
        gradientWithLetter = gd.GradientWithLetter(gradient,120,'G',15)
        self.assertEqual(1,gradientWithLetter[72,100])
    
class ManyGradientsCreate(unittest.TestCase):#
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

#~ poniższe okazało się niepotrzebne, bo jest funkcja np.save
class SaveAndOpenGeneratedGradients(unittest.TestCase):
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
