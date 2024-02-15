#번역
import webbrowser
import googletrans
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import pyperclip
import whisper

model = whisper.load_model('medium')
result = model.transcribe('audio-path')
voice_str = str(result['text'])
voice_str = voice_str + "your-prompt"

f = open("txt-path", "w", encoding = 'utf-8')
f.write(voice_str)
f.close()





to_trans = []

translator = googletrans.Translator()




def joonyeong_trans(string):
    history_list_en = []
    history_list_kor = []
    history_list_cn = []
    history_list_ja = []
    what_lang = str(translator.detect(string))
    print(what_lang)
    what_lang_start_idx = what_lang.find('lang=')
   # print(what_lang_start_idx)
    used_lang = str(what_lang[14:16])
    print(used_lang)
    if used_lang == 'en':
        history_list_en.append(string)
        print("대기열 등록")
        for li in history_list_en:
            print(li)
        to_trans.append(string)
    if used_lang == 'ko':
        history_list_kor.append(string)
        print('번역을 진행합니다.(한 -> 영)')
        for li in history_list_kor:
            print(li)
            
        translated_string = translator.translate(string, dest = 'en')
        history_list_kor.append(translated_string)
        translated_string = str(translated_string)
        str_idx_start = translated_string.find('text=')
        str_idx_end = translated_string.find('pronunciation')
        #print(str_idx_start)
        #print(str_idx_end)
        new_translated = translated_string[str_idx_start+5:str_idx_end]
        print(new_translated)
        to_trans.append(new_translated)
        #print(to_trans[0])
    if used_lang == 'zh':
        history_list_cn.append(string)
        print('번역을 진행합니다.(중 -> 영')
        for li in history_list_cn:
            print(li)
        
        translated_string = translator.translate(string, dest = 'en')
        translated_string = str(translated_string)
        str_idx_start = translated_string.find('text=')
        str_idx_end = translated_string.find('pronunciation')
        new_translated = translated_string[str_idx_start+5:str_idx_end]
        print(new_translated)
        to_trans.append(new_translated)
    if used_lang == 'ja':
        history_list_ja.append(string)
        print('번역을 진행합니다.(일 -> 영')
        for li in history_list_ja:
            print(li)
        
        translated_string = translator.translate(string, dest = 'en')
        translated_string = str(translated_string)
        str_idx_start = translated_string.find('text=')
        str_idx_end = translated_string.find('pronunciation')
        new_translated = translated_string[str_idx_start+5:str_idx_end]
        print(new_translated)
        to_trans.append(new_translated)
        
        
        
    
f = open("txt-path", "r", encoding = 'utf-8')

str_list = []
i = 0
for string in f.readlines():
    str_list.append(string)    
    string = str_list[i]
    i = i + 1
    first_step = joonyeong_trans(string)

i = 0
    
f = open("txt-path", "w", encoding = 'utf-8')

i = 0
for string in to_trans:
    f.write(string)
    i = i + 1
    
f.close()

if i != 0: 
    #webbrowser.open("http://127.0.0.1:7860")
    path = "chromedriver.path"
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    url = "http://127.0.0.1:7860"
    driver.get(url)

        
        
driver.maximize_window()
print(pyautogui.size())
fore = pyautogui.getActiveWindow()
print(fore.title)
print(fore.size)
print(fore.left, fore.top, fore.right, fore.bottom)

for win in pyautogui.getAllWindows():
    print(win)

    

time.sleep(2)
print(pyautogui.position())


time.sleep(2)
pyautogui.moveTo(138, 344)

pyautogui.moveTo(138, 344) 
    
pyautogui.click()


string_copy = ""

f = open("txt-path", 'r', encoding = 'utf-8')
string_copy = f.readlines()
string_copy = str(string_copy)
string_copy = string_copy.replace('[', "")
string_copy = string_copy.replace(']',"")
#print(string_copy)
f.close()

#pyautogui.write(string_copy, interval=0.25)
pyperclip.copy(string_copy) # 클립보드에 텍스트를 복사합니다. 

pyautogui.hotkey('ctrl', 'v') # 붙여넣기 (hotkey)


time.sleep(2)
pyautogui.moveTo(1588, 374) 

pyautogui.moveTo(1588, 374)
pyautogui.click()
pyautogui.sleep(10)

for i in range(0, 150):
    pyautogui.sleep(0.001)
    pyautogui.moveTo(1395, 674)


            
pyautogui.click(button='right')
pyautogui.press(['down', 'down'])
pyautogui.press(['enter'])
pyautogui.sleep(1)
pyautogui.press(['enter'])
print("사진이 저장되었습니다.")                


 
    
    
    
    
