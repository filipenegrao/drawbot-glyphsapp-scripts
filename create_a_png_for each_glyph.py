# A primeira coisa é importar o GlyphsApp para dentro do Drawbot, para que eles conversem
from GlyphsApp import *

# agora, pegamos a fonte atual, aberta
my_font = Glyphs.font

# precisamos descobrir o UPM da fonte, para definir a altura da página
# mas é possível definir qualquer tamanho de página que vc quiser.
UPM = my_font.upm

# também precisamos do valor dos descendentes da fonte,
# já que o Drawbot tem o ponto 0,0 no canto inferior esquerdo.
# O nosso ponto 0,0 precisa ser, na verdade, o ponto em que o glifo comecará a ser desenhado.
# Ou seja: (x_origem, y_origem) precisam ser igual a (margem esquerda, descendente) 
D = my_font.masters[0].descender

# para cada glifo dentro da fonte aberta:    
for glyph in my_font.glyphs:
    # l = descobrimos a margem esquerda
    l = glyph.layers[0].LSB
    # r = descobrimos a margem direita
    r = glyph.layers[0].RSB
    # w = descobrimos a largura do glifo
    w = glyph.layers[0].width
    # bd = descobrimos os limites do glifo, nesta caso, a altura máxima que o glifo tem quando selecionado.
    bd = glyph.layers[0].bounds.size.height
    
    # Se a altura do glifo, somando o valor das descendentes for menor do que o UPM,
    # fazemos uma página do mesmo valor do UPM
    if bd+(-D) < UPM:
        newPage(w+l+r, UPM)
    # Do contrário, fazemos uma página que tem a altura do descendente + o tamanho do bound
    else:
        newPage(w+l+r, bd+(-D))
        
    # fill é a cor, neste caso 0 é preto
    fill(0)
    
    # translate move o objeto (no caso, cada glifo) para um ponto x, y.
    # x aqui é igual à margem esquerda e y ao valor das descendentes. 
    translate(x=l, y=-D)
    
    for thisInstance in my_font.instances:
        instanceFont = thisInstance.interpolatedFontProxy
        instanceGlyph = instanceFont.glyphForName_(glyph.name)
        instanceLayer = instanceGlyph.layers[instanceFont.fontMasterID()]
        
        # completeBezierPath inclui todos os paths dentro de uma instância, dentro de um glifo,
        # incluindo eventuais componentes
        drawPath(instanceLayer.completeBezierPath)
        
        # salva da glifo em um arquivo png no desktop.
        # Importante: neste caso eu estou assumindo que existe um folder no desktop
        # chamado 'fontname' (que pode ser qualquer nome)
        # dá pra jogar os arquivos em qualquer lugar e criar o folder automaticamente se ele
        # não existir, mas agora estou com preguiça de escrever isso :)
        saveImage("~/Desktop/fontname/{0}.png".format(glyph.name)) 
        
    
