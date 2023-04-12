#  Python tip you need to know: Create a GUI in 1 min  https://www.youtube.com/shorts/n594oH_dtvI

import pyautogui

var = pyautogui.alert(text='Do a Sub!', title='PyChamp', button='OK')
print(var)

var = pyautogui.confirm(text='PyChamp', title='PyChamp', buttons=['YES', 'NO'])
print(var)

var = pyautogui.prompt(text='PyChamp', title='PyChamp' , default='Test')
print(var)

var = pyautogui.password(text='password', title='PyChamp', default='', mask='*')
print(var)