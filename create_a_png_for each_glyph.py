'''
This script was written to work inside DrawBot for Glyphs App.
You can install it usign Window > Plugin Manager or from the source:
https://github.com/schriftgestalt/DrawBotGlyphsPlugin

'''

# The first thing to be done is export GlyphsApp inside the
# Drawbot, so they can talk to each other
from GlyphsApp import *

# Now, we get the font that is opened in Glyphs
my_font = Glyphs.font

# We need to find the UPM so we can define the height of the page
UPM = my_font.upm

# The descender's value is also need, since DrawBot
# has the origin point 0,0 on the inferior left side.  
# So, the 0,0 needs to point to (LSB, descender)
D = my_font.masters[0].descender

# For each glyph in the open font:    
for glyph in my_font.glyphs:
    # l = left margin
    l = glyph.layers[0].LSB
    # r = right margin
    r = glyph.layers[0].RSB
    # w = the width of the glyph
    w = glyph.layers[0].width
    # bd = the boundaries of the glyph, to pick the height
    bd = glyph.layers[0].bounds.size.height
    

    # If the height of the glyphs + descenders are less than the UPM, the
    # page should be the same size of the UPM
    if bd+(-D) < UPM:
        newPage(w+l+r, UPM)
    # Otherwise, we make the descenders height + the boundaries of the glyph
    else:
        newPage(w+l+r, bd+(-D))
        
    # fill colour = 0, meaning black.
    fill(0)
    
    # move the glyph to the 0,0 point
    translate(x=l, y=-D)
    
    for thisInstance in my_font.instances:
        instanceFont = thisInstance.interpolatedFontProxy
        instanceGlyph = instanceFont.glyphForName_(glyph.name)
        instanceLayer = instanceGlyph.layers[instanceFont.fontMasterID()]
        
        # completeBezierPath includes all paths within the instances inside a glyph,
        # including components
        drawPath(instanceLayer.completeBezierPath)
        
        # save the glyphs in a png in the desktop.
        # Important: in this case, I'm assuming that there is a folder on the desktop that
        # is called 'fontname'
        saveImage("~/Desktop/fontname/{0}.png".format(glyph.name)) 

