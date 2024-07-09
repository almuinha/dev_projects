# Link do site do jogo: https://guitarflash.com/?lg=pt

# Teclas do jogo:
# A --> verde
# S --> vermelho
# J --> amarelo
# K --> azul
# L --> laranja

# 1. Abrir página do jogo no navegador web: https://guitarflash.com/?lg=pt (SLEEP - aguardar a página carregar)
# 2. Rolar a tela um pouco para baixo, até aparecer o botão "JOGAR", se precisar (para o caso de aparecerem propagandas grandes na parte de cima)
# 3. Clicar no botão "JOGAR"
# 4. Rolar a tela um pouco para baixo
# 5. Clicar no campo de preenchimento "BUSCAR POR", digitar o nome da música, clicar em "OK"
# 6. Cliar no resultado da pesquisa ao lado esquerdo do botão de pesquisa
# 7. Rolar a tela um pouco para baixo
# 8. Pressionar uma letra do teclado para iniciar o jogo
# 9. Jogar
#   Presisonar as teclas A, S, J, K, L quando aparecerem na linha de notas
#   Existem ainda as teclas de especial, que tem formato de estrela

#------------------#
# INICIANDO CÓDIGO #
#------------------#

# Executar comandos no CMD da máquina para obter coordenadas do mouse na tela:
# from mouseinfo import mouseInfo
# mouseInfo()

#-------------------------#
# BIBLIOTECAS NECESSÁRIAS #
#-------------------------#
import pyautogui
import webbrowser
from time import sleep
import pyperclip
import keyboard
import win32api
import win32con

#---------------------#
# FUNÇÃO PARA DIGITAR #
#---------------------#
def escrever_frase(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

#---------------------------------------#
# FUNÇÃO PARA PRESSIONAR TECLAS DO JOGO #
#---------------------------------------#
def pressionar_teclas_do_jogo():
    # VERDE
    if pyautogui.pixelMatchesColor(490, 603, (0, 152, 0)):
        pyautogui.press("a")
        sleep(0.05)
    # VERMELHO
    elif pyautogui.pixelMatchesColor(581, 602, (255, 0, 0)):
        pyautogui.press("s")
        sleep(0.05)
    # AMARELO
    elif pyautogui.pixelMatchesColor(670, 600, (244, 244, 2)):
        pyautogui.press("j")
        sleep(0.05)
    # AZUL
    elif pyautogui.pixelMatchesColor(761, 603, (0, 152, 255)):
        pyautogui.press("k")
        sleep(0.05)
    # LARANJA
    elif pyautogui.pixelMatchesColor(851, 602, (255, 101, 0)):
        pyautogui.press("l")
        sleep(0.05)

#--------------------------------#
# EXECUTANDO ETAPAS DA AUTOMAÇÃO #
#--------------------------------#

# 1. Abrir página do jogo no navegador web
webbrowser.open("https://guitarflash.com/?lg=pt")

# 2. Aguardando a página carregar
sleep(5)

# 3. Clicar no botão "JOGAR"
coordenadas_botao_jogar = pyautogui.locateCenterOnScreen("P2_botao_jogar.png")
pyautogui.click(coordenadas_botao_jogar, duration = 2)
sleep(3)

# 4. Rolar a tela um pouco para baixo
#pyautogui.scroll(-1000)

# 5. Clicar no campo de preenchimento "BUSCAR POR", digitar o nome da música, clicar em "OK"
#coordenadas_campo_busca = pyautogui.locateCenterOnScreen("P2_buscar_por_musica_para_jogar.png")
musica_para_pesquisar = "Somewhere I Belong"
pyautogui.click(817, 556, duration = 2)
escrever_frase(musica_para_pesquisar)

# 6. Cliar no resultado da pesquisa ao lado esquerdo do botão de pesquisa
#coordenadas_musica_pesquisada = pyautogui.locateCenterOnScreen("P2_musica_linkin_park.png")
pyautogui.click(478, 593, duration = 2)
sleep(5)

# 7. Rolar a tela um pouco para baixo
pyautogui.scroll(-450)
sleep(5)

# 8. Pressionar uma letra do teclado para iniciar o jogo
pyautogui.press("a")

# 9. Jogar
# A música tem 226 segundos
# Iniciando o loop temporizado
# while keyboard.is_pressed('1') == False:
#for segundo in range(230):
    #pressionar_teclas_do_jogo()

# Rodei aqui e não consegui zerar o jogo com essa música, mas valeu a tentativa

while keyboard.is_pressed('1') == False:
    
    # VERDE
    if pyautogui.pixelMatchesColor(490, 603, (0, 152, 0)):
        pyautogui.press("a")
        sleep(0.05)
    # VERMELHO
    elif pyautogui.pixelMatchesColor(581, 602, (255, 0, 0)):
        pyautogui.press("s")
        sleep(0.05)
    # AMARELO
    elif pyautogui.pixelMatchesColor(670, 600, (244, 244, 2)):
        pyautogui.press("j")
        sleep(0.05)
    # AZUL
    elif pyautogui.pixelMatchesColor(761, 603, (0, 152, 255)):
        pyautogui.press("k")
        sleep(0.05)
    # LARANJA
    elif pyautogui.pixelMatchesColor(851, 602, (255, 101, 0)):
        pyautogui.press("l")
        sleep(0.05)

# Dessa forma também não deu pra zerar o jogo

