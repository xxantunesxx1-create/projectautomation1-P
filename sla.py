import time
import pyautogui
import pandas as pd

time.sleep(2)
pyautogui.click(123,764)
time.sleep(2)
pyautogui.click(330,101)
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")

time.sleep(7)

pyautogui.click(472,354)
pyautogui.write("seu email")
pyautogui.click(586,462)
pyautogui.write("sua senha")
pyautogui.click(595,525)

time.sleep(2)
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linhas in tabela.index:
    pyautogui.click(574, 260)
    codigo = tabela.loc[linhas, codigo]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linhas, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linhas, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)






