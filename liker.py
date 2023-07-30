import pyautogui,time

time.sleep(10)

#to find out the co-ordinates
#print(pyautogui.position())

n=0

while n < 5:
    #it clicks at a certain place
    pyautogui.click(x=739, y=564)
    #presses right to go to the next post
    pyautogui.press('right') 
    n+=1   
    time.sleep(3)
