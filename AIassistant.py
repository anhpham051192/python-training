# 音声認識のライブラリをインポート（Them thu vien nhan dien giong noi)
import speech_recognition
# アシスタントの話をレコーディングしMP3ファイルを保存するためのライブラリ
import gtts
# ファイルを読む、ファイルを書くためのライブラリ(Doc va ghi file)
import os
# 時間習得ため（Lay ngay gio may tinh)
from datetime import date,datetime

# khoi tao suy nghi cua AI # Ban dau no chua hoc duoc gi ca nen chua co thong tin
ai_brain = " "
# Khoi tao cho AI tai de co the nghe nguoi dung noi 
ai_ear = speech_recognition.Recognizer()
# Lay mic cua pc gan cho bien mic
with speech_recognition.Microphone() as mic:
    print ("LEアシスタント: 聴いています")
    # Tao bien audio chua am thanh ma tai cua AI nghe duoc ,mic: chua am thanh nguoi dung noi,duration: sau 5 giay se dong mic 
    audio = ai_ear.record(mic,duration = 6)
    print("\n LEアシスタント : ....")
try:
    you = ai_ear.recognize_google(audio, language="ja-JP")#nghe noi tieng viet
    print("\n 利用者 : " + you)
except:
#Neu khong nghe thay hoac co tap am
    ai_brain = "よく聞き取れないです。!"
    print("\LEアシスタント: " + ai_brain)
# Neu co cau konnichiha trong cau doi thoai cua you thi se in ra konnichiha
if "こんにちは" in you:
    ai_brain = "こんにちは"
elif "天気" in you:
    ai_brain = "AIなので今日の天気よくわかりません。"
elif "何日" in you:
    today = date.today()
    ai_brain = today.strftime("%d/%m/%Y")
elif "何時" in you:
    now = datetime.now()
    ai_brain = now.strftime("%H:%M:%S")
else:
    ai_brain = "ありがとうございます。"
    print ("\nLEアシスタント: " + ai_brain)
print ("\nLEアシスタント :" + ai_brain)
