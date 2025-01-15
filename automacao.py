# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1 #Pode variar com a velocidade do seu computador para abrir o navegador, menor o tempo menos tempo para o seu PC pensar

# abrir o navegador (google chrome) pode variar de acordo com as suas necessidades
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(15) #Pode variar com a velocidade do seu computador para abrir o navegador
pyautogui.press('f11')
time.sleep(3)
pyautogui.click(x=675, y=453) #Pode variar com o tamanho da tela do seu computador
time.sleep(4)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(6) #Pode variar com a velocidade do seu computador para abrir o navegador

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=526, y=429) #Pode variar com o tamanho da tela do seu computador
# escrever o seu email
pyautogui.write("Coloque um email, apenas visual")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("Coloque uma senha, apenas visual")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter") # clicando para login
time.sleep(3)
pyautogui.click(x=763, y=111) #Pode variar com o tamanho da tela do seu computador

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=704, y=314) #Pode variar com o tamanho da tela do seu computador
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000) #Número grande apenas para ter certeza que ele irá subir a tela inteira
    # Passo 5: Repetir o processo de cadastro até o fim
