# __ASG_TypesMetaModel.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
class ASG_TypesMetaModel(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'TypesMetaModel', ASGroot, ['ASG_TypesMetaModel' ,'TypeName' ,'LeafType' ,'ModelType' ,'Operator'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.Author=ATOM3String('')
      self.Comments=ATOM3String('')
      self.generatedAttributes = {'Author': ('ATOM3String', ),
                                  'Comments': ('ATOM3String', )      }
      self.realOrder = ['Author','Comments']
      self.directEditing = [1,0]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'TypesMetaModel', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


