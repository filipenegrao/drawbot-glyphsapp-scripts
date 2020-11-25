import os 
import datetime

# create a formatted string
txt = FormattedString()
NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

fonts_folder = u"/Library/Application Support/Adobe/Fonts"

otf_list = os.listdir(fonts_folder)

# depends on the order of your fonts appear in the folder they are in 
my_order = [6, 1, 3, 5, 8, 0, 4, 7]
otf_list = [otf_list[i] for i in my_order]

fontname_list = list()

for letter in alphabet:
    for filename in otf_list:
        if filename.split('.')[-1] == 'otf':
            
            path = fonts_folder + '/' + filename
            font_name = installFont(path)
            fontname_list.append(font_name)
            
            # adding some text with some formatting
            txt.append(letter, font=font_name, fontSize=72)
    txt += '\n'

fontname_list = set(fontname_list)
footnote =  ", ".join(otf_list)

# drawing the formatted string
# text(txt, (50, 480))
# A4 ~= 595 × 842 points
x, y, w, h = 50, 0, 842, 595

while len(txt):
    newPage('A4Landscape')
    font("Times-Italic", 10)
    text(NOW, (55, 45))
    text(footnote, (55, 30))
    
    txt = textBox(txt, (x, y, w, h))

saveImage("~/Desktop/ArSans.pdf")

for filename in otf_list:
        if filename.split('.')[-1] == 'otf':
            # uninstall font
            uninstallFont(path)
            
