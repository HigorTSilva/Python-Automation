#Passo a passo do projeto

#Passo 1 - Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
#pip install pyautogui
import pyautogui
import time
import pandas as pd

#clicar -> pyauyogui.click
#escrever -> pyautogui.write
#pressionar -> pyautogui.press
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(5)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

#Passo 2 - Fazer login
pyautogui.click(x=610, y=345)
pyautogui.write("kjhgfd.gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=680, y=474)
time.sleep(3)

#Passo 3 - Importar a base de dados
    #pip install pandas numpy openpyxl
tabela = pd.read_csv("produtos.csv")

#Passo 4 - Cadastrar produtos

for linha in tabela.index:
    pyautogui.click(x=573, y=259)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) #ou "1"
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(1000)

#Passo 5 - Repetir até acabar a base de dados