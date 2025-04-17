import pyautogui
import time
import pandas as pd

def preencher_campo(valor, espera=1, interval=0.1):
    try:
        pyautogui.PAUSE = 0.3
        if pd.isna(valor):
            raise ValueError("Valor nulo ao tentar preencher campo.")
        time.sleep(espera)
        pyautogui.press('tab')
        time.sleep(espera)
        pyautogui.write(valor, interval=interval)
    except Exception as e:
        print(f'Erro ao preencher o campo "{valor}": {e}')

    
def marcar_por_posicao(valor, esperado, espera=3, x=0, y=0):
    try:
        pyautogui.PAUSE = 0.3
        if pd.isna(valor):
            raise ValueError("Valor nulo ao tentar marcar campo.")
        if valor == esperado:
            time.sleep(espera)
            pyautogui.click(x=x, y=y)
    except Exception as e:
        print(f'Erro ao marcar o campo "{valor}": {e}')

def marcar(valor, esperado, espera=3):
    try:
        pyautogui.PAUSE = 0.3
        if pd.isna(valor):
            raise ValueError("Valor nulo ao tentar marcar campo.")
        time.sleep(espera)
        if valor == esperado:
            pyautogui.press('tab')
            time.sleep(espera)
            pyautogui.press('enter')
    except Exception as e:
        print(f'Erro ao marcar o campo "{valor}": {e}')        
        
def preencher_campo_por_posicao(valor, espera=1, x=0, y=0, interval=0.1):
    try:
        pyautogui.PAUSE = 0.3
        if pd.isna(valor):
            raise ValueError("Valor nulo ao tentar preencher campo.")
        time.sleep(espera)
        pyautogui.click(x=x, y=y)
        pyautogui.write(str(valor), interval=interval)
    except Exception as e:
        print(f'Erro ao preencher o campo na posição ({x}, {y}) com valor "{valor}": {e}')

def organizar_area_trabalho(x=0, y=0, espera=1):
    try:
        pyautogui.PAUSE = 0.3
        time.sleep(espera)
        pyautogui.click(x=x, y=y)
    except Exception as e:
        print(f'Erro ao organizar a área de trabalho na posição ({x}, {y}): {e}')

def abrir_arquivo():
    try:
        pyautogui.PAUSE = 0.3
        time.sleep(3)
        pyautogui.doubleClick() # passe a posição 'x' e 'y'.
        time.sleep(3)
        pyautogui.doubleClick()# passe a posição 'x' e 'y'.
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')

def salvar_arquivo(nome, interval=0.1):
    try:
        pyautogui.PAUSE = 0.3
        time.sleep(3)
        pyautogui.hotkey('shift', 'ctrl', 's')
        time.sleep(5)
        pyautogui.click() # passe a posição 'x' e 'y'.
        time.sleep(2)
        pyautogui.write(nome, interval=interval)   
        time.sleep(2)
        pyautogui.click() # passe a posição 'x' e 'y'.
        time.sleep(2)
        pyautogui.click() # passe a posição 'x' e 'y'.
    except Exception as e:
        print(f'Erro ao salvar o arquivo com nome: {e}')
    
def fechando_arquivo():
    try:
        pyautogui.PAUSE = 0.3       
        time.sleep(2)
        pyautogui.click() # passe a posição 'x' e 'y'.
        time.sleep(2)
        pyautogui.click() # passe a posição 'x' e 'y'.
    except Exception as e:
        print(f'Erro ao fechar o arquivo: {e}')



