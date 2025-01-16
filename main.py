import pyautogui
import time
import cv2 #permite rodar 'confidence' na linha 15


#Passo 1 - entrar no site 
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# primeira maneira de localizar algo na tela:
local = pyautogui.locateOnScreen('perfil chrome.png', confidence=0.9)
if local is not None:
    #Calcula o centro da regiao encontrada
    center = pyautogui.center(local)
    pyautogui.click(center)
else:
    print("Perfil não encontrado na tela.")

pyautogui.moveTo(221, 62, duration=0.5) #2 maneira de localizar na tela
pyautogui.click()
pyautogui.press("backspace")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#Passo 2 - Fazer o login

local = pyautogui.locateOnScreen('login.png', confidence=0.8)
if local is not None:
    #Calcula o centro da regiao encontrada
    center = pyautogui.center(local)
    pyautogui.click(center)
else:
    print("Perfil não encontrado na tela.")

pyautogui.write("abcdefgh")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("enter")

time.sleep(2)

local = pyautogui.locateOnScreen('ok.png', confidence=0.9)
if local is not None:
    #Calcula o centro da regiao encontrada
    center = pyautogui.center(local)
    pyautogui.click(center)
else:
    print("Perfil não encontrado na tela.")

#Passo 3 - importar base de dados dos produtos
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

#Passo 4 - Cadastrar o primeiro produto

for linha in tabela.index:
    pyautogui.click(x=367, y=294)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write("obs")
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000)
