"""
__graph_Process.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Process(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 172, 63
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
        h = drawing.create_oval(self.translate([28.0, 41.0, 28.0, 41.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf199 = PhotoImage(format='gif',data=self.imageDict['ProcessNew.gif' ])
        h = drawing.create_image(self.translate([28.0, 41.0]), tags = self.tag, image = self.image_gf199)
        self.gf199 = GraphicalForm(drawing, h, 'gf199', 'ProcessNew.gif')
        self.graphForms.append(self.gf199)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='FreeSans', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([28.0, 7.0, 28.0, 10.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf201 = GraphicalForm(drawing, h, 'gf201', fontObject=font)
        self.graphForms.append(self.gf201)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='FreeSans', size=8, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([28.0, 54.0, 28.0, 8.0])[:2], tags = self.tag, font=font, fill = 'white', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf202 = GraphicalForm(drawing, h, 'gf202', fontObject=font)
        self.graphForms.append(self.gf202)

        if self.semanticObject: drawText = self.semanticObject.hasActions.toString()
        else: drawText = "<hasActions>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([60.0, 20.0, 60.0, -180.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'nw', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["hasActions"] = h
        self.gf203 = GraphicalForm(drawing, h, 'gf203', fontObject=font)
        self.graphForms.append(self.gf203)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'Process2.gif' ] = ''+\
'R0lGODlhMgAdAIABAACAAP///yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAyAB0AAAKR'+\
'hG+hu3gMg0uxzaomrRpgqX2deJFlNGIpF6ote6Iv1HmwY+JuTM89b/EFdTfiz3hE5JRFpkyYWSWd080T'+\
'CIJmsVvk0BvV1prUb9n8IFsZ4yu4Zquuw9y2+9zF2+VxttQvFlj3hzaXl3ZnSId32Ac4CAm2iJjoWLgT'+\
'yUh4iakpKNnYSSm3pHhYaroZKmr5OMpQAAA7'        

        imageDict[ 'Process.gif' ] = ''+\
'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'        

        imageDict[ 'ProcessNew.gif' ] = ''+\
'R0lGODlhKAAoAPAAAABVAAAAACH5BAAAAAAALAAAAAAoACgAAAInhI+py+0Po5y02ouz3rz7D4biSJbm'+\
'iabqyrbuC8fyTNf2jef6ziMFADs='        

        return imageDict

new_class = graph_Process
