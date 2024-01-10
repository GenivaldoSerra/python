import pyautogui
import time
import pandas as pd

# Prcipais comandos do PyAutoGUI
# pyautogui.position() -> retorna a posição do mouse
# pyautogui.moveTo(x, y, duration) -> move o mouse para a posição x, y em um tempo duration
# pyautogui.click(x, y) -> clica na posição x, y
# pyautogui.doubleClick(x, y) -> clica duas vezes na posição x, y
# pyautogui.rightClick(x, y) -> clica com o botão direito na posição x, y
# pyautogui.dragTo(x, y, duration) -> arrasta o mouse para a posição x, y em um tempo duration
# pyautogui.write('texto') -> escreve o texto
# pyautogui.press('enter') -> pressiona a tecla enter

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 1

# Acessar o navegador Edge
pyautogui.press("win")

pyautogui.write("edge")

pyautogui.press("enter")

# Digitar o link
pyautogui.write(link)

# Pressionar a tecla enter
pyautogui.press("enter")

# Aguardar 5 segundos
# pyautogui.sleep(5)
time.sleep(10)

# Clicar no campo de e-mail
pyautogui.click(x=-770, y=300)

# Digitar o e-mail
pyautogui.write('teste@teste.com')

# Clicar no campo de senha
pyautogui.click(x=-835, y=374)

# Digitar a senha
pyautogui.write('teste')

# Clicar no botão entrar
pyautogui.click(x=-651, y=434)

# Aguardar 5 segundos
time.sleep(5)

# Importar a base de dados
tabela = pd.read_csv('produtos.csv', sep=';')
print(tabela)