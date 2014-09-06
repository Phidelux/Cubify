
#!/usr/bin/env python
import sys, codecs
from lxml import etree

sys.path.append('/usr/share/inkscape/exetnsions')
import inkex
from simplestyle import *

class Cubify(inkex.Effect):
    def __init__(self):
        # Call the base class constructor.
        inkex.Effect.__init__(self)
        
        # Definition of script parameters (Ensure that the second parameter matches the names in the inx file).
        self.OptionParser.add_option('--textColor', action='store', type='string', dest='textColor', help='Color of normal text')
        self.OptionParser.add_option('--titleColor', action='store', type='string', dest='titleColor', help='Color of the title')
        self.OptionParser.add_option('--titleBgColor', action='store', type='string', dest='titleBgColor', help='The title background color')
        self.OptionParser.add_option('--hintColor', action='store', type='string', dest='hintColor', help='Color of the hint')
        self.OptionParser.add_option('--hintBgColor', action='store', type='string', dest='hintBgColor', help='The hint background color')
        self.OptionParser.add_option('--mainBgColor', action='store', type='string', dest='mainBgColor', help='The main background color')
        self.OptionParser.add_option('--borderColor', action='store', type='string', dest='borderColor', help='Color of the basic shape')

        self.OptionParser.add_option('--logoPath', action='store', type='string', dest='logoPath', help='Path to the main logo')
        self.OptionParser.add_option('--logoStyle', action='store', type='string', dest='logoStyle', help='The logo display options')
        self.OptionParser.add_option('--logoBgColor', action='store', type='string', dest='logoBgColor', help='The logo side background color')

        self.OptionParser.add_option('--sideOneHint', action='store', type='string', dest='sideOneHint', help='Subhead text')
        self.OptionParser.add_option('--sideTwoHint', action='store', type='string', dest='sideTwoHint', help='Subhead text')
        self.OptionParser.add_option('--sideThreeHint', action='store', type='string', dest='sideThreeHint', help='Subhead text')
        self.OptionParser.add_option('--sideFourHint', action='store', type='string', dest='sideFourHint', help='Subhead text')
        self.OptionParser.add_option('--sideFiveHint', action='store', type='string', dest='sideFiveHint', help='Subhead text')

        # Inkscape param workaround.
        self.OptionParser.add_option("--cubify_config")
        self.OptionParser.add_option("--display_options")
        self.OptionParser.add_option("--cubify_logo_side")
        self.OptionParser.add_option("--cubify_side_i")
        self.OptionParser.add_option("--cubify_side_ii")
        self.OptionParser.add_option("--cubify_side_iii")
        self.OptionParser.add_option("--cubify_side_iv")
        self.OptionParser.add_option("--cubify_side_v")

    def effect(self):
        self.log('Applying effect ...')

        # Fetch the svg root element ...
        svg = self.document.getroot()

        # ... as well as the image width and height.
        width  = inkex.unittouu(svg.get('width'))
        height = inkex.unittouu(svg.attrib['height'])

        # Fetch the extention parameters.
        textColor = self.options.textColor
        titleColor = self.options.titleColor
        titleBgColor = self.options.titleBgColor
        hintColor = self.options.hintColor
        hintBgColor = self.options.hintBgColor
        mainBgColor = self.options.mainBgColor
        borderColor = self.options.borderColor

        sideOneHint = self.options.sideOneHint
        sideTwoHint = self.options.sideTwoHint
        sideThreeHint = self.options.sideThreeHint
        sideFourHint = self.options.sideFourHint
        sideFiveHint = self.options.sideFiveHint

        # Create a new layer, ...
        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'Basic Shape')
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        # ... calculate the dimensions of the basic cube shape ...
        wingHeight = width / 23

        if wingHeight * 19 > height:
            wingHeight = height / 19

        wingWidth = wingHeight * 5

        padding = wingHeight

        blockWidth = blockHeight = wingWidth
        borderWidth = 1

        # ... and the headline boxes.
        boxWidth = blockWidth
        boxHeight = wingHeight
        boxBorderColor = 'ffffff'
        boxBorder = 0
        
        # Draw the basic shape (cutting edges), ...
        self.drawPolygon(
            borderWidth, borderColor, False, layer,
            (padding + wingHeight, padding + wingHeight + blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + blockHeight),
            (padding + 2 * blockWidth, padding + blockHeight),
            (padding + 2 * blockWidth, padding + 2 * wingHeight),
            (padding + 2 * wingHeight + 2 * blockWidth, padding),
            (padding + 3 * blockWidth, padding),
            (padding + 2 * wingHeight + 3 * blockWidth, padding + 2 * wingHeight),
            (padding + 2 * wingHeight + 3 * blockWidth, padding + blockHeight),
            (padding + wingHeight + 3 * blockWidth, padding + wingHeight + blockHeight),
            (padding + wingHeight + 3 * blockWidth, padding + wingHeight + blockHeight),
            (padding + wingHeight + 4 * blockWidth, padding + wingHeight + blockHeight),
            (padding + wingHeight + 4 * blockWidth, padding + wingHeight + 2 * blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + 2 * blockHeight),
            (padding + 2 * wingHeight + 2 * blockWidth, padding + 2 * wingHeight + 2 * blockHeight),
            (padding + 2 * wingHeight + 2 * blockWidth, padding + 3 * blockHeight),
            (padding + 2 * blockWidth, padding + 2 * wingHeight + 3 * blockHeight),
            (padding + 2 * wingHeight + blockWidth, padding + 2 * wingHeight + 3 * blockHeight),
            (padding + blockWidth, padding + 3 * blockHeight),
            (padding + blockWidth, padding + 2 * wingHeight + 2 * blockHeight),
            (padding + wingHeight + blockWidth, padding + wingHeight + 2 * blockHeight),
            (padding + wingHeight, padding + wingHeight + 2 * blockHeight),
            (padding, padding + 2 * blockHeight),
            (padding, padding + 2 * wingHeight + blockHeight),
            (padding + wingHeight, padding + wingHeight + blockHeight))

        # ... the inner edges ...
        self.drawLine(padding + wingHeight, padding + wingHeight + blockHeight, padding + wingHeight,  padding + wingHeight + 2 * blockHeight, borderWidth, borderColor, True, layer)
        self.drawLine(padding + wingHeight + blockWidth, padding + wingHeight + blockWidth, padding + wingHeight + blockWidth,  padding + wingHeight + 2 * blockWidth, borderWidth, borderColor, True, layer)
        self.drawLine(padding + wingHeight + 2 * blockWidth, padding + wingHeight + blockWidth, padding + wingHeight + 2 * blockWidth,  padding + wingHeight + 2 * blockWidth, borderWidth, borderColor, True, layer)
        self.drawLine(padding + wingHeight + 3 * blockWidth, padding + wingHeight + blockWidth, padding + wingHeight + 3 * blockWidth,  padding + wingHeight + 2 * blockWidth, borderWidth, borderColor, True, layer)

        self.drawPolygon(
            borderWidth, borderColor, True, layer,
            (padding + wingHeight + blockWidth, padding + wingHeight + 2 * blockHeight),
            (padding + wingHeight + blockWidth, padding + wingHeight + 3 * blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + 3 * blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + 2 * blockHeight),
            (padding + wingHeight + blockWidth, padding + wingHeight + 2 * blockHeight))

        self.drawPolygon(
            borderWidth, borderColor, True, layer,
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight), 
            (padding + wingHeight + 3 * blockWidth, padding + wingHeight),
            (padding + wingHeight + 3 * blockWidth, padding + wingHeight + blockHeight),
            (padding + wingHeight + 2 * blockWidth, padding + wingHeight + blockHeight))

        # ... and the headline boxes.
        self.drawSideFooter(padding + wingHeight, padding + 2 * blockHeight, boxWidth, boxHeight, boxBorder, boxBorderColor, layer, 'Hello World!', titleBgColor, titleColor, boxHeight / 4, sideOneHint, hintBgColor, hintColor, boxHeight / 20 * 3)
        self.drawSideFooter(padding + wingHeight + blockWidth, padding + 2 * blockHeight, boxWidth, boxHeight, boxBorder, boxBorderColor, layer, 'Hello World!', titleBgColor, titleColor, boxHeight / 4, sideTwoHint, hintBgColor, hintColor, boxHeight / 20 * 3)
        self.drawSideFooter(padding + wingHeight + 2 * blockWidth, padding + 2 * blockHeight, boxWidth, boxHeight, boxBorder, boxBorderColor, layer, 'Hello World!', titleBgColor, titleColor, boxHeight / 4, sideThreeHint, hintBgColor, hintColor, boxHeight / 20 * 3)
        self.drawSideFooter(padding + wingHeight + 3 * blockWidth, padding + 2 * blockHeight, boxWidth, boxHeight, boxBorder, boxBorderColor, layer, 'Hello World!', titleBgColor, titleColor, boxHeight / 4, sideFourHint, hintBgColor, hintColor, boxHeight / 20 * 3)
        self.drawSideFooter(padding + wingHeight + blockWidth, padding + 3 * blockHeight, boxWidth, boxHeight, boxBorder, boxBorderColor, layer, 'Hello World!', titleBgColor, titleColor, boxHeight / 4, sideFiveHint, hintBgColor, hintColor, boxHeight / 20 * 3)

    def drawSideFooter(self, x, y, w, h, border, borderColor, parent, title, titleBg, titleColor, titleSize, hint, hintBg, hintColor, hintSize):
        self.drawTextBox(x, y, w, h, border, borderColor, titleBg, parent, title, titleColor, titleSize)
        self.drawTextBox(x, y - h / 5 , w, h / 5, border, borderColor, hintBg, parent, hint, hintColor, hintSize)

    def drawTextBox(self, x, y, w, h, border, borderColor, fillColor, parent, msg, fontColor, fontSize):
        # Create a new layer.
        layer = inkex.etree.SubElement(parent, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'Headline Layer')
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        # Draw the actual textbox, ...
        box = self.drawRectangle(x, y, w, h, border, borderColor, fillColor, layer)

        # ... create the text element, ...
        text = inkex.etree.SubElement(layer, inkex.addNS('text','svg'))
        text.set('x', str(x + fontSize))
        text.set('y', str(y + h / 2 + fontSize / 2))
        text.set('fill', '#' + str(fontColor));
        text.text = str(msg)

        # ... define text style and position, ...
        style = {
            'font-weight' : 'bold',
            'font-size': str(fontSize)
        }

        # ... finally set the text style ...
        text.set('style', formatStyle(style))

        # ... and connect it to the parent box.
        # box.append(text)

    def drawLine(self, x1, y1, x2, y2, width, color, dashed, parent):
        dashStyle = '5,3,2' if dashed else 'none'

        style = { 
            'stroke': '#' + str(color),
            'stroke-width' : width,
            'stroke-dasharray' : dashStyle,
            'fill' : 'none'
        }

        attrs = {
            'style' : formatStyle(style),
            inkex.addNS('label','inkscape') : 'A Name',
            'd' : 'M ' + str(x1) + ',' + str(y1) + ' L ' + str(x2) + ',' + str(y2)
        }

        return inkex.etree.SubElement(parent, inkex.addNS('path','svg'), attrs)

    def drawRectangle(self, x, y, w, h, border, borderColor, fillColor, parent):
        # Define the rectangle style ...
        stroke = '#' + str(borderColor) if border > 0 else 'none'

        style = { 
            'stroke' : stroke, 
            'stoke-width' : str(border), 
            'fill' : '#' + str(fillColor)
        }
                
        attrs = {
            'style' : formatStyle(style),
            'x' : str(x),
            'y' : str(y),
            'width' : str(w),
            'height' : str(h)        
        }

        return inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attrs)

    def drawPolygon(self, width, color, dashed, parent, *points):
        dashStyle = '5,3,2' if dashed else 'none'

        style = { 
            'stroke': '#' + str(color),
            'stroke-width' : width,
            'stroke-dasharray' : dashStyle,
            'stroke-linejoin' : 'round', 
            'fill' : 'none'
        }

        counter = 0
        pointList = ''
        for p in points:
            if counter == 0:
                pointList += 'M ' + str(p[0]) + ',' + str(p[1])
            else:
                pointList += ' L ' + str(p[0]) + ',' + str(p[1]) + ' '
            counter += 1

        attrs = {
            'style' : formatStyle(style),
            'd' : pointList
        }        

        return inkex.etree.SubElement(parent, inkex.addNS('path','svg'), attrs)

    def log(self, msg):
        with open('/home/awilhelm/cubify.log', 'a+') as log:
            log.write(msg)

def main(argv):
    cubify = Cubify()
    cubify.affect()

if __name__ == "__main__":
    main(sys.argv[1:])
