import time
import winsound
import pyttsx3
import threading

##音が鳴る　はい
def beep(freq, duration):
    winsound.Beep(freq, duration)

##入力された時間より一秒だけ短い時間待つ（ビープ音で一秒使うので）
def countdown(seconds):
        time.sleep(seconds-1)

##読み上げ
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


##ビープ
def process1():
    beep(150, 1000)  # 短いビープ音を再生

##読み上げ「あとn回」
def process2():
    global yomiage
    yomiage-= 1
    print(f"{yomiage} rounds left.")
    speak_text("あと"+str(yomiage)+"回") 

##ビープと読み上げを同時にするよ    
def multitask():
    thread1 = threading.Thread(target=process1)
    thread2 = threading.Thread(target=process2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()


def main():
    u = int(input("Enter the interval time for 'u' in seconds: "))
    d = int(input("Enter the interval time for 'd' in seconds: "))
    m = int(input("Enter the number of repetitions: "))
    global yomiage
    yomiage=m
    print("準備")
    speak_text("準備")
    time.sleep(3)
    speak_text("よーい")
    u_beep_freq = 200  # u秒後のビープ音の周波数
    d_beep_freq = 150  # d秒後のビープ音の周波数

    for rep in range(m):
        print(f"Round {rep + 1}")
        
        print("Starting 'u' interval...")
        countdown(u)
        beep(u_beep_freq, 1000)  # 短いビープ音を再生
        
        print("Starting 'd' interval...")
        countdown(d)
        multitask()

    print("Workout completed!")
    speak_text("お疲れさまでした！次も頑張りましょうね！")


if __name__ == "__main__":

    main()
