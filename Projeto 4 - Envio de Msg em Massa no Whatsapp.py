# Para enviar mensagens em massa existem alguns requisitos:
# 1. Ter uma lista de números para contato
# 2. Enviar individualmente uma mensagem para cada pessoa
# 3. Pausar entre cada envio (para não ser identificado como bot e, consequentemente, bloqueado)

# A título de teste, enviar mensagem para 1 contato

# API do whatsapp que envia mensagem pra o número especificado no final da URL
# https://api.whatsapp.com/send?phone=559xxxxxxxx

import webbrowser
import pyautogui
from time import sleep

telefones          = ['55219xxxxxxxx', '55219xxxxxxxx']
total_de_telefones = len(telefones)
contador_telefones = 0

# Caso a lista de contatos estivesse em um arquivo:
# 1. Criar uma lista para receber os números de telefone
# 2. Acessar o arquivo e ler linha a linha
# 3. Extrair o valor de cada linha e colocar dentro da lista

#telefones = []
#with open("lista_contatos.txt", "r") as arquivo:
#    for contato in arquivo:
#        telefones.append(contato.split('\n')[0])

for nro in telefones:
    
    if contador_telefones == 0:
        
        link_api = f'https://api.whatsapp.com/send?phone={nro}'
        webbrowser.open(link_api)
        sleep(10)
        pyautogui.click(775, 246, duration = 1)
        sleep(20)
        pyautogui.click(538, 694)
        sleep(15)
        # Lembrando que para enviar msgs com acentuação, usar piperclip
        pyautogui.typewrite("Oie! To testando rs")
        sleep(10)
        pyautogui.press("enter")
        sleep(300)

        contador_telefones = contador_telefones + 1
    
    else:
        # Clicar na barra de pesquisa e procurar contato
        pyautogui.click(105, 118, duration = 1)
        sleep(5)
        # Digitar número desejado
        pyautogui.typewrite(str(nro))
        sleep(5)
        # Clicar no contato encontrado
        pyautogui.click(202, 185, duration = 1)
        sleep(20)
        pyautogui.click(538, 694)
        sleep(15)
        pyautogui.typewrite("Oie! To só testando rs")
        sleep(10)
        pyautogui.press("enter")
        sleep(300)

        contador_telefones = contador_telefones + 1

