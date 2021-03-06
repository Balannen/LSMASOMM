"""
__graph_isPartOfOrgUnit_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_isPartOfOrgUnit_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 20, 20
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        self.image_gf164 = PhotoImage(format='gif',data=self.imageDict['isPartOfOrgUnitNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf164)
        self.gf164 = GraphicalForm(drawing, h, 'gf164', 'isPartOfOrgUnitNew.gif')
        self.graphForms.append(self.gf164)

        h = drawing.create_oval(self.translate([-1.0, 0.0, -1.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'isPartOfOrgUnitNew.gif' ] = ''+\
'R0lGODlhFAAUAPAAAP/MAAAAACH5BAEAAAEALAAAAAAUABQAAAIqhH8RyJ3rolFS0uouZno/z0HgJDbK'+\
'iabqyqZWCXYx7Mk1vdk5juk9DygAADs='        

        imageDict[ 'isPartOfOrgUnit.gif' ] = ''+\
'R0lGODlhMgA0AOMIAP/dK//dLP/dLf/eK//eLP/eLf/fK//fLP//////////////////////////////'+\
'/yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAgALAAAAAAyADQAAATrEMlJKyKYCMu7/9SQZWBpWsY4'+\
'nmyprm3MvaRsTzR270G+77TfTzUQAmFGmyqpVBWYJ0EuUwgYp9gsbQPSerXcz3ecC3vI6JG5k26vZ230'+\
'2xJPu+rkO947r+zHen9YB4GCOVZdSD2GOokEcIYmT2yRFSKNhXg4LyaMWZmeSGehPo6CEqVipxSLNR+X'+\
'e4QWBQSTl5CrH60AFKElB6RBpsEYvMNaIgOtX6BTHMBaiKpa05/HqZRYBs1LILTW1c7cGH29WdLhL+Wb'+\
'4B7LW+Ouo1jrqF7XKvUX9/P08aKs+IwDVmDAJA4DEiakgc5DBAA7'        

        return imageDict

new_class = graph_isPartOfOrgUnit_Center
