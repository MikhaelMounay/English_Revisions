import bs4
import requests
import pyautogui
import pyperclip
import time

pyautogui.FAILSAFE = True

title1 = "test notion"
title2 = "Google Translate - Google Chrome"



def getWordsDict ():
    words = input("words: ")
    words = words.split(", ")
    print(words)

    words_dict = {word: {"meaningA": "","meaningE": "", "eg": ""} for word in words}
    print(words_dict)

    for word in words:
        res = requests.get('https://dictionary.cambridge.org/dictionary/english-arabic/' + word, headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        defs = soup.select("div.def.ddef_d.db")
        for i in defs:
            words_dict[word]["meaningE"] += i.getText() + " --- "

        examples = soup.select("div.examp.dexamp span.eg.deg")
        for i in examples:
            words_dict[word]["eg"] += i.getText() + " --- "

        pyperclip.copy(word)
        pyautogui.getWindowsWithTitle(title2)[0].maximize()
        time.sleep(0.5)
        pyautogui.click(521, 359)
        time.sleep(0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('a', interval=0.05)
            pyautogui.press('v', interval=0.05)
        time.sleep(1)
        pyautogui.click(1583, 514)
        time.sleep(0.1)
        words_dict[word]["meaningA"] = pyperclip.paste()


    print(words_dict)
    return words_dict

getWordsDict()
