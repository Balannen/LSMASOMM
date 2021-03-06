"""
__OrgUnit.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Sat Apr 14 23:09:41 2018
_________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from ATOM3List import *
from graph_OrgUnit import *
class OrgUnit(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_OrgUnit
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(True)
      self.parent = parent
      self.ID=ATOM3String('OU|', 20)
      self.keyword_= self.ID
      self.Individual=ATOM3Boolean()
      self.Individual.setValue(('1', 0))
      self.Individual.config = 0
      self.UnitSize=ATOM3String('Individual', 20)
      self.hasActions=ATOM3List([ 1, 1, 1, 0],ATOM3String)
      lcobj0=[]
      cobj0=ATOM3String('ChangeRole', 20)
      lcobj0.append(cobj0)
      self.hasActions.setValue(lcobj0)
      self.name=ATOM3String('OUname', 20)
      self.generatedAttributes = {'ID': ('ATOM3String', ),
                                  'Individual': ('ATOM3Boolean', ),
                                  'UnitSize': ('ATOM3String', ),
                                  'hasActions': ('ATOM3List', 'ATOM3String'),
                                  'name': ('ATOM3String', )      }
      self.realOrder = ['ID','Individual','UnitSize','hasActions','name']
      self.directEditing = [1,1,0,1,1]
   def clone(self):
      cloneObject = OrgUnit( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.ID
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.ID
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CONNECT:
         res = self.ConstraintOutputOrgUnit(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def ConstraintOutputOrgUnit(self, params):
      from CustomCode import *
      res = OrgUnitCheckOutputs(self)
      if res is "manyKnArts":
          return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)
      else:
          return
      
      

   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.CONNECT or actionID == self.SELECT:
         self.determineSize(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <---- Remove this to use QOCA
      
      """ Get the high level constraint helper and solver """
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)
      oc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)
      
      

   def determineSize(self, params):
      from CustomCode import *
      res = OrgUnitDetermineSize(self)
      self.UnitSize.setValue(res)
      self.graphObject_.ModifyAttribute('UnitSize', res)
      
      



