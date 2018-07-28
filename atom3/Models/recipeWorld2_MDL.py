"""
__recipeWorld2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Fri Feb  2 18:31:45 2018
__________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from Objective import *
from canHaveRole import *
from hasActions import *
from isPartOfObjective import *
from hasObjective import *
from graph_canHaveRole import *
from graph_Action import *
from graph_isPartOfObjective import *
from graph_hasObjective import *
from graph_Role import *
from graph_Objective import *
from graph_OrgUnit import *
from graph_hasActions import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def recipeWorld2_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # agentImplementation
        LSMASOMMRootNode.agentImplementation.setValue( (['SPADE', 'Enmasse', 'EveJS'], 0) )
        LSMASOMMRootNode.agentImplementation.config = 0

        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('recipeWorld33')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj93=OrgUnit(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # Individual
    self.obj93.Individual.setValue(('1', 0))
    self.obj93.Individual.config = 0

    # hasActions
    self.obj93.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj93.hasActions.setValue(lcobj2)

    # ID
    self.obj93.ID.setValue('OU|0')

    # name
    self.obj93.name.setValue('Agent')

    # UnitSize
    self.obj93.UnitSize.setValue('Individual')

    self.obj93.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(0,480,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj85=Role(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # isMetaRole
    self.obj85.isMetaRole.setValue((None, 0))
    self.obj85.isMetaRole.config = 0

    # hasActions
    self.obj85.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('SearchForFactories', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('CheckFactoryAvailability', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('WaitForFactoryAnswer', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('StartProduction', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('FinishProduction', 20)
    lcobj2.append(cobj2)
    self.obj85.hasActions.setValue(lcobj2)

    # ID
    self.obj85.ID.setValue('R|0')

    # name
    self.obj85.name.setValue('Order')

    self.obj85.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(191,640,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=Role(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # isMetaRole
    self.obj86.isMetaRole.setValue((None, 0))
    self.obj86.isMetaRole.config = 0

    # hasActions
    self.obj86.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('AnswerQuery', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Produce', 20)
    lcobj2.append(cobj2)
    self.obj86.hasActions.setValue(lcobj2)

    # ID
    self.obj86.ID.setValue('R|1')

    # name
    self.obj86.name.setValue('Factory')

    self.obj86.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(450,160,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj57=Action(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # ID
    self.obj57.ID.setValue('A|0')

    # name
    self.obj57.name.setValue('SearchForFactories')

    # ActionCode
    self.obj57.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj57.ActionCode.setHeight(15)

    self.obj57.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(450,800,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=Action(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # ID
    self.obj58.ID.setValue('A|1')

    # name
    self.obj58.name.setValue('CheckFactoryAvailability')

    # ActionCode
    self.obj58.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj58.ActionCode.setHeight(15)

    self.obj58.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(450,960,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=Action(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # ID
    self.obj59.ID.setValue('A|2')

    # name
    self.obj59.name.setValue('WaitForFactoryAnswer')

    # ActionCode
    self.obj59.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj59.ActionCode.setHeight(15)

    self.obj59.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(450,640,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=Action(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # ID
    self.obj60.ID.setValue('A|3')

    # name
    self.obj60.name.setValue('StartProduction')

    # ActionCode
    self.obj60.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj60.ActionCode.setHeight(15)

    self.obj60.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(756,320,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=Action(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # ID
    self.obj61.ID.setValue('A|4')

    # name
    self.obj61.name.setValue('FinishProduction')

    # ActionCode
    self.obj61.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj61.ActionCode.setHeight(15)

    self.obj61.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(756,480,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=Action(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # ID
    self.obj62.ID.setValue('A|5')

    # name
    self.obj62.name.setValue('AnswerQuery')

    # ActionCode
    self.obj62.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj62.ActionCode.setHeight(15)

    self.obj62.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(756,0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=Action(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # ID
    self.obj63.ID.setValue('A|6')

    # name
    self.obj63.name.setValue('Produce')

    # ActionCode
    self.obj63.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj63.ActionCode.setHeight(15)

    self.obj63.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(756,160,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj44=Objective(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # description
    self.obj44.description.setValue('\n')
    self.obj44.description.setHeight(4)

    # ofActions
    self.obj44.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj44.ofActions.setValue(lcobj2)

    # Measurement
    self.obj44.Measurement.setValue('\n')
    self.obj44.Measurement.setHeight(4)

    # Reward
    self.obj44.Reward.setValue('\n')
    self.obj44.Reward.setHeight(4)

    # ID
    self.obj44.ID.setValue('O|0')

    # name
    self.obj44.name.setValue('ProduceRecipePart')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1254,480,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Objective(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # description
    self.obj45.description.setValue('\n')
    self.obj45.description.setHeight(4)

    # ofActions
    self.obj45.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj45.ofActions.setValue(lcobj2)

    # Measurement
    self.obj45.Measurement.setValue('\n')
    self.obj45.Measurement.setHeight(4)

    # Reward
    self.obj45.Reward.setValue('\n')
    self.obj45.Reward.setHeight(4)

    # ID
    self.obj45.ID.setValue('O|1')

    # name
    self.obj45.name.setValue('SelectFactory')

    self.obj45.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1021,800,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=Objective(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # description
    self.obj46.description.setValue('\n')
    self.obj46.description.setHeight(4)

    # ofActions
    self.obj46.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj46.ofActions.setValue(lcobj2)

    # Measurement
    self.obj46.Measurement.setValue('\n')
    self.obj46.Measurement.setHeight(4)

    # Reward
    self.obj46.Reward.setValue('\n')
    self.obj46.Reward.setHeight(4)

    # ID
    self.obj46.ID.setValue('O|2')

    # name
    self.obj46.name.setValue('ProductionStarted')

    self.obj46.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1021,320,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Objective(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # description
    self.obj47.description.setValue('\n')
    self.obj47.description.setHeight(4)

    # ofActions
    self.obj47.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj47.ofActions.setValue(lcobj2)

    # Measurement
    self.obj47.Measurement.setValue('\n')
    self.obj47.Measurement.setHeight(4)

    # Reward
    self.obj47.Reward.setValue('\n')
    self.obj47.Reward.setHeight(4)

    # ID
    self.obj47.ID.setValue('O|3')

    # name
    self.obj47.name.setValue('ProductionFinished')

    self.obj47.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1021,480,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Objective(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # description
    self.obj48.description.setValue('\n')
    self.obj48.description.setHeight(4)

    # ofActions
    self.obj48.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj48.ofActions.setValue(lcobj2)

    # Measurement
    self.obj48.Measurement.setValue('\n')
    self.obj48.Measurement.setHeight(4)

    # Reward
    self.obj48.Reward.setValue('\n')
    self.obj48.Reward.setHeight(4)

    # ID
    self.obj48.ID.setValue('O|4')

    # name
    self.obj48.name.setValue('SearchSuitableFactories')

    self.obj48.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(756,800,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Objective(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # description
    self.obj49.description.setValue('\n')
    self.obj49.description.setHeight(4)

    # ofActions
    self.obj49.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('CheckFactoryAvailability', 20)
    lcobj2.append(cobj2)
    self.obj49.ofActions.setValue(lcobj2)

    # Measurement
    self.obj49.Measurement.setValue('\n')
    self.obj49.Measurement.setHeight(4)

    # Reward
    self.obj49.Reward.setValue('\n')
    self.obj49.Reward.setHeight(4)

    # ID
    self.obj49.ID.setValue('O|5')

    # name
    self.obj49.name.setValue('CheckIfFactoryAvailable')

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(756,960,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Objective(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # description
    self.obj50.description.setValue('\n')
    self.obj50.description.setHeight(4)

    # ofActions
    self.obj50.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj50.ofActions.setValue(lcobj2)

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('O|6')

    # name
    self.obj50.name.setValue('ReceiveAnswer')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(756,640,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Objective(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # description
    self.obj51.description.setValue('\n')
    self.obj51.description.setHeight(4)

    # ofActions
    self.obj51.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj51.ofActions.setValue(lcobj2)

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    # Reward
    self.obj51.Reward.setValue('\n')
    self.obj51.Reward.setHeight(4)

    # ID
    self.obj51.ID.setValue('O|7')

    # name
    self.obj51.name.setValue('ProduceSingleRecipePart')

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1254,160,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Objective(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # description
    self.obj52.description.setValue('\n')
    self.obj52.description.setHeight(4)

    # ofActions
    self.obj52.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj52.ofActions.setValue(lcobj2)

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    # Reward
    self.obj52.Reward.setValue('\n')
    self.obj52.Reward.setHeight(4)

    # ID
    self.obj52.ID.setValue('O|8')

    # name
    self.obj52.name.setValue('ReplyToOrder')

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1021,0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Objective(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # description
    self.obj53.description.setValue('\n')
    self.obj53.description.setHeight(4)

    # ofActions
    self.obj53.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    self.obj53.ofActions.setValue(lcobj2)

    # Measurement
    self.obj53.Measurement.setValue('\n')
    self.obj53.Measurement.setHeight(4)

    # Reward
    self.obj53.Reward.setValue('\n')
    self.obj53.Reward.setHeight(4)

    # ID
    self.obj53.ID.setValue('O|9')

    # name
    self.obj53.name.setValue('ProducePart')

    self.obj53.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1021,160,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj96=canHaveRole(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(True)

    # ID
    self.obj96.ID.setValue('OUR|0')

    self.obj96.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(122.0,511.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj91=hasActions(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # ID
    self.obj91.ID.setValue('aR|0')

    self.obj91.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(387.0,654.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=hasActions(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # ID
    self.obj92.ID.setValue('aR|1')

    self.obj92.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(692.0,174.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj54=isPartOfObjective(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(True)

    # ID
    self.obj54.ID.setValue('pO|0')

    self.obj54.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(1194.0,490.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=isPartOfObjective(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(True)

    # ID
    self.obj55.ID.setValue('pO|1')

    self.obj55.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(961.0,810.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=isPartOfObjective(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(True)

    # ID
    self.obj56.ID.setValue('pO|2')

    self.obj56.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(1194.0,170.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj64=hasObjective(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # ID
    self.obj64.ID.setValue('RPO|0')

    self.obj64.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(689.0,810.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj69=hasObjective(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # ID
    self.obj69.ID.setValue('RPO|1')

    self.obj69.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(689.0,970.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=hasObjective(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # ID
    self.obj70.ID.setValue('RPO|2')

    self.obj70.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(689.0,650.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj73=hasObjective(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # ID
    self.obj73.ID.setValue('RPO|3')

    self.obj73.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(961.0,330.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj76=hasObjective(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # ID
    self.obj76.ID.setValue('RPO|4')

    self.obj76.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(961.0,490.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj79=hasObjective(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # ID
    self.obj79.ID.setValue('RPO|5')

    self.obj79.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(961.0,10.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj82=hasObjective(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # ID
    self.obj82.ID.setValue('RPO|6')

    self.obj82.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(961.0,170.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    # Connections for obj93 (graphObject_: Obj43) named Agent
    self.drawConnections(
(self.obj93,self.obj96,[22.575791651860186, 543.009002227856, 69.22335967638305, 517.4856451853975, 122.0, 511.0],"true", 3) )
    # Connections for obj85 (graphObject_: Obj37) named Order
    self.drawConnections(
(self.obj85,self.obj91,[255.65578097031766, 691.6864014417491, 318.56989045732143, 663.2310502930853, 387.0, 654.0],"true", 3) )
    # Connections for obj86 (graphObject_: Obj38) named Factory
    self.drawConnections(
(self.obj86,self.obj92,[484.5363685796382, 211.8773039158953, 590.0642281471572, 202.77604116761697, 692.0, 174.0],"true", 3) )
    # Connections for obj57 (graphObject_: Obj16) named SearchForFactories
    self.drawConnections(
(self.obj57,self.obj64,[444.0, 438.0, 689.0, 810.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj17) named CheckFactoryAvailability
    self.drawConnections(
(self.obj58,self.obj69,[554.0, 518.0, 689.0, 970.0],"true", 0) )
    # Connections for obj59 (graphObject_: Obj18) named WaitForFactoryAnswer
    self.drawConnections(
(self.obj59,self.obj70,[694.0, 498.0, 689.0, 650.0],"true", 0) )
    # Connections for obj60 (graphObject_: Obj19) named StartProduction
    self.drawConnections(
(self.obj60,self.obj73,[814.0, 318.0, 961.0, 330.0],"true", 0) )
    # Connections for obj61 (graphObject_: Obj20) named FinishProduction
    self.drawConnections(
(self.obj61,self.obj76,[864.0, 618.0, 961.0, 490.0],"true", 0) )
    # Connections for obj62 (graphObject_: Obj21) named AnswerQuery
    self.drawConnections(
(self.obj62,self.obj79,[964.0, 628.0, 961.0, 10.0],"true", 0) )
    # Connections for obj63 (graphObject_: Obj22) named Produce
    self.drawConnections(
(self.obj63,self.obj82,[1064.0, 638.0, 961.0, 170.0],"true", 0) )
    # Connections for obj44 (graphObject_: Obj0) named ProduceRecipePart
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj1) named SelectFactory
    self.drawConnections(
(self.obj45,self.obj54,[581.0, 215.0, 1194.0, 490.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj2) named ProductionStarted
    self.drawConnections(
(self.obj46,self.obj54,[731.0, 235.0, 1194.0, 490.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj3) named ProductionFinished
    self.drawConnections(
(self.obj47,self.obj54,[861.0, 235.0, 1194.0, 490.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj4) named SearchSuitableFactories
    self.drawConnections(
(self.obj48,self.obj55,[402.0, 335.0, 961.0, 810.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj5) named CheckIfFactoryAvailable
    self.drawConnections(
(self.obj49,self.obj55,[542.0, 355.0, 961.0, 810.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj6) named ReceiveAnswer
    self.drawConnections(
(self.obj50,self.obj55,[687.0, 355.0, 961.0, 810.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj7) named ProduceSingleRecipePart
    self.drawConnections(
 )
    # Connections for obj52 (graphObject_: Obj8) named ReplyToOrder
    self.drawConnections(
(self.obj52,self.obj56,[1011.0, 425.0, 1194.0, 170.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj9) named ProducePart
    self.drawConnections(
(self.obj53,self.obj56,[1201.0, 415.0, 1194.0, 170.0],"true", 2) )
    # Connections for obj96 (graphObject_: Obj44) of type canHaveRole
    self.drawConnections(
(self.obj96,self.obj85,[122.0, 511.0, 196.86741898010212, 595.3962702875339, 255.65578097031766, 691.6864014417491],"true", 3),
(self.obj96,self.obj86,[122.0, 511.0, 268.0, 524.0, 451.0, 488.0, 484.5363685796382, 211.8773039158953],"true", 4) )
    # Connections for obj91 (graphObject_: Obj39) of type hasActions
    self.drawConnections(
(self.obj91,self.obj57,[387.0, 654.0, 461.46470681648617, 739.9343290223869, 519.7213363485772, 837.586090815781],"true", 3),
(self.obj91,self.obj58,[387.0, 654.0, 471.7765744388135, 821.7926325347081, 538.247736543302, 997.6420559485656],"true", 3),
(self.obj91,self.obj59,[387.0, 654.0, 460.4592970739628, 655.9601823679303, 530.669409274105, 677.6546698327152],"true", 3),
(self.obj91,self.obj60,[387.0, 654.0, 527.0, 379.0, 756.0, 329.0, 810.8661076219305, 357.77674768073325],"true", 4),
(self.obj91,self.obj61,[387.0, 654.0, 527.0, 539.0, 756.0, 489.0, 816.3560722767493, 518.3066228040634],"true", 4) )
    # Connections for obj92 (graphObject_: Obj41) of type hasActions
    self.drawConnections(
(self.obj92,self.obj62,[692.0, 174.0, 755.6389222053291, 112.55029135748798, 803.8480357967005, 38.37576420402513],"true", 3),
(self.obj92,self.obj63,[692.0, 174.0, 736.6242350152664, 195.7002065879654, 786.1907229796132, 198.02067799230903],"true", 3) )
    # Connections for obj54 (graphObject_: Obj10) of type isPartOfObjective
    self.drawConnections(
(self.obj54,self.obj44,[611.0, 155.0, 641.0, 95.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj12) of type isPartOfObjective
    self.drawConnections(
(self.obj55,self.obj45,[546.0, 270.0, 601.0, 215.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj14) of type isPartOfObjective
    self.drawConnections(
(self.obj56,self.obj51,[1056.0, 345.0, 1101.0, 265.0],"true", 2) )
    # Connections for obj64 (graphObject_: Obj23) of type hasObjective
    self.drawConnections(
(self.obj64,self.obj48,[423.0, 386.5, 402.0, 335.0],"true", 2) )
    # Connections for obj69 (graphObject_: Obj25) of type hasObjective
    self.drawConnections(
(self.obj69,self.obj49,[689.0, 970.0, 755.971823025478, 997.1427782860313, 827.8185697899128, 1004.8887754334471],"true", 3) )
    # Connections for obj70 (graphObject_: Obj27) of type hasObjective
    self.drawConnections(
(self.obj70,self.obj50,[689.0, 650.0, 749.1021385415502, 658.1804593898914, 803.2767280578552, 685.4623365950476],"true", 3) )
    # Connections for obj73 (graphObject_: Obj29) of type hasObjective
    self.drawConnections(
(self.obj73,self.obj46,[961.0, 330.0, 1014.5279164410483, 356.99651949618647, 1073.9572439996005, 364.88352966266484],"true", 3) )
    # Connections for obj76 (graphObject_: Obj31) of type hasObjective
    self.drawConnections(
(self.obj76,self.obj47,[961.0, 490.0, 1016.217446997954, 517.1056351470739, 1077.2121087456812, 525.0638477591172],"true", 3) )
    # Connections for obj79 (graphObject_: Obj33) of type hasObjective
    self.drawConnections(
(self.obj79,self.obj52,[961.0, 10.0, 1014.898199599497, 17.82126724221567, 1062.3389021618968, 44.57136783506019],"true", 3) )
    # Connections for obj82 (graphObject_: Obj35) of type hasObjective
    self.drawConnections(
(self.obj82,self.obj53,[961.0, 170.0, 1006.3686991224516, 196.7612538413273, 1058.4433828660513, 204.6802739971032],"true", 3) )

newfunction = recipeWorld2_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
