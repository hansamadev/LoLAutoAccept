import pyautogui
from python_imagesearch.imagesearch import imagesearch  
import time

pyautogui.FAILSAFE = False  
TIMELAPSE = 1  # Bekleme süresi (saniye cinsinden)

acceptButtonImg = 'C:\\Users\\han\\Desktop\\bot\\sample.png'


def maçKabulEt():
    """
    Bu fonksiyon, 'acceptButtonImg' görselini arar ve bulunduğunda
    o konumda tıklayarak maçı kabul eder.
    """
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)  
        
        if not pos[0] == -1:  # Görsel bulunduysa
            pyautogui.click(pos[0], pos[1])  # Tıklama işlemi yapılıyor
            print("Maç kabul edildi!") 
            break  
        
        time.sleep(TIMELAPSE)  

def main():
    """
    Ana fonksiyon. Burada sadece maç kabul etme işlemi çalıştırılıyor.
    """
    print("Çalışıyor...")  # Programın çalıştığını belirten mesaj
    maçKabulEt()  # Maç kabul etme fonksiyonunu çağırıyoruz

if __name__ == '__main__':
    main()  
