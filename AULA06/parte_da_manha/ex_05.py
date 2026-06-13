import pyautogui
import time

def abrir_wordpad():
    # Abre o menu Iniciar
    pyautogui.press("win")
    time.sleep(1)

    # Digita o nome do aplicativo
    pyautogui.write("Word", interval=0.05)
    time.sleep(1)

    # Pressiona Enter para abrir
    pyautogui.press("enter")
    time.sleep(2)

    print("✅ Word aberto com sucesso!")

abrir_wordpad()