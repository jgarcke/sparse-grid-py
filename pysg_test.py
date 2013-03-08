import pysg
import unittest
import math
class testFunctest(unittest.TestCase):
  """ simple test if sparse grid for sparse grid in 3d of level 3 """
  def testSGNoBound3D(self):
    sg = pysg.sparseGrid(3,3)
    sg.generatePoints()
    # right number of grid points
    self.assertEqual(len(sg.indices),31)
    for i in range(len(sg.indices)):
      sum = 1.0
      pos = sg.gP[tuple(sg.indices[i])].pos
      for j in range(len(pos)):
        sum *= 4.*pos[j]*(1.0-pos[j])
      sg.gP[tuple(sg.indices[i])].fv = sum
    # convert to hierarchical values
    sg.nodal2Hier()
    # does the evaluation of sparse grid function in
    # hierarchical values give the correct value gv
    for i in range(len(sg.indices)):
      self.assertEqual(sg.gP[tuple(sg.indices[i])].fv,\
        sg.evalFunct(sg.gP[tuple(sg.indices[i])].pos))
  
  def testSGNoBound2D(self):    
    sg = pysg.sparseGrid(2,3)
    sg.generatePoints()
    # right number of grid points
    self.assertEqual(len(sg.indices),17)
    for i in range(len(sg.indices)):
      sum = 1.0
      pos = sg.gP[tuple(sg.indices[i])].pos
      for j in range(len(pos)):
        sum *= 4.*pos[j]*(1.0-pos[j])
      sg.gP[tuple(sg.indices[i])].fv = sum
    # convert to hierarchical values
    sg.nodal2Hier()
    # does the evaluation of sparse grid function in
    # hierarchical values give the correct value gv
    for i in range(len(sg.indices)):
      self.assertEqual(sg.gP[tuple(sg.indices[i])].fv,\
        sg.evalFunct(sg.gP[tuple(sg.indices[i])].pos))

if __name__=="__main__":
  unittest.main()
    


