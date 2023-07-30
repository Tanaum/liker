import pyautogui,time

time.sleep(10)

#print(pyautogui.position())

n=0

while n < 5:
    pyautogui.click(x=739, y=564)
    pyautogui.press('right') 
    n+=1   
    time.sleep(3)