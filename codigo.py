import pyautogui
import time

#Passo 1: Entrar no sitema da empresa
#Site https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#espera 3 segundos
time.sleep(3)

#Passo 2: Fazer Login
pyautogui.click(x=601, y=504)
pyautogui.write("pythonimpressionador@gmail.com")

#preencher senha
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep (3)

#Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: cadastrar produtos 

for linha in tabela.index: #para cada linha da minha tabela

    pyautogui.click(x=596, y=364)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) #string = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
     
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos





