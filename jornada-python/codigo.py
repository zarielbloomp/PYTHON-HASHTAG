import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.PAUSE = 0.3

pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

link_login = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyperclip.copy(link_login)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=959, y=405)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=976, y=558)
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=742, y=293)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
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
    pyautogui.press("enter")
    pyautogui.scroll(5000)
