import pygetwindow as gw
import pydirectinput
import time
import keyboard
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

# janela do otp 
game_window = gw.getWindowsWithTitle("otPokemon | Soysatos")[0]



# funções para fazer o macro funcionar / parar de funcionar...
def fullHit():
    for key in range(1, 11):
        pydirectinput.keyDown(f'f{key}')
        time.sleep(0.1)
        
def stopFullHit():    
    for key in range(1, 11):
        pydirectinput.keyUp(f'f{key}')
        time.sleep(0.1)


game_window.activate()

while True:

    fullHit()
    keyboard.wait('q')
    stopFullHit()
    keyboard.wait('e')
    time.sleep(0.1)