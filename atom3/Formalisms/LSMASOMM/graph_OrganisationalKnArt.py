"""
__graph_OrganisationalKnArt.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_OrganisationalKnArt(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 40, 70
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
        h = drawing.create_oval(self.translate([20.0, 20.0, 20.0, 20.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf191 = PhotoImage(format='gif',data=self.imageDict['OrgKnArtNew.gif' ])
        h = drawing.create_image(self.translate([20.0, 20.0]), tags = self.tag, image = self.image_gf191)
        self.gf191 = GraphicalForm(drawing, h, 'gf191', 'OrgKnArtNew.gif')
        self.graphForms.append(self.gf191)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([20.0, 60.0, 20.0, 50.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf89 = GraphicalForm(drawing, h, 'gf89', fontObject=font)
        self.graphForms.append(self.gf89)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'OrgKnArtNew.gif' ] = ''+\
'R0lGODlhKAAoAPEAAAAAAICz/wAAAAAAACH5BAEAAAIALAAAAAAoACgAAAKRhI8mEu3fVpp0LoiDrNyy'+\
'/GzdCFygI5KceWqCOrJnCntt9NaVDNL6wcv4fqVPa/gLYpA6JYRZc4ZyRIQURa0qjLOs9orTWrk9bxXs'+\
'EgPJQjMRDYXB3Un2kt60P/FR/VS9dZMGuFBoeBingrhYCFhEkgjJt+WYGBkz+UiYedlhmSkZuimq9lnJ'+\
'CYpJKmY6qjpSAAA7'        

        return imageDict

new_class = graph_OrganisationalKnArt
