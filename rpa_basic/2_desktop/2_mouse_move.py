import pyautogui

# pyautogui.moveTo(100, 100)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 00, duration=1)

pyautogui.moveTo(100, 100, duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y
      
      
      
      )