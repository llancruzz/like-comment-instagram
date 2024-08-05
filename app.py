import pyautogui
import webbrowser
from time import sleep

while True:
    # 1.	Navigate to the site https://www.instagram.com
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)
    # 2.	Log in with my username
    pyautogui.click(1071, 345, duration=1)
    sleep(1)
    pyautogui.typewrite('username')
    sleep(1)
    # 3.	Log in with my password
    pyautogui.click(1069, 389, duration=1)
    sleep(1)
    pyautogui.typewrite('password')
    sleep(1)
    # 4.	Click on login
    pyautogui.click(1083, 442, duration=1)
    sleep(20)
    # 5.	Click on “Not now” to not save the browser
    pyautogui.click(1083, 621, duration=1)
    sleep(20)
    # 6.	Close the window asking to save the password
    pyautogui.click(1662, 88, duration=1)
    sleep(1)
    # 7.	Search for the page
    pyautogui.click(1182, 179, duration=1)
    sleep(1)
    pyautogui.typewrite('any user')
    sleep(1)
    # 8.	Enter the page
    pyautogui.move(0, 100, duration=1)
    sleep(1)
    pyautogui.click()
    sleep(20)
    # 9.	Click on the most recent post
    pyautogui.click(845, 642, duration=1)
    sleep(10)
    # 10.	Check if the post has already been liked or not
    heart = pyautogui.locateCenterOnScreen('heart.png')
    sleep(1)
    # 11.	If it has already been liked, do nothing and pause the bot for 24 hours.
    if heart is not None:
        sleep(86400)
    # 12.	If it hasn’t been liked, like the photo
    elif heart == None:
        pyautogui.click(845, 642, duration=1)
        sleep(5)
        # 13.	If it hasn’t been liked, comment on the photo
        pyautogui.click(985, 732, duration=1)
        sleep(3)
        pyautogui.click(1035, 822, duration=1)
        sleep(1)
        pyautogui.typewrite('I love that picture!')
        sleep(5)
        pyautogui.click(1715, 832, duration=1)
        # 14.	Pause for 24 hours
        sleep(86400)

    # 15.	After 24 hours, run everything again (While loop)
