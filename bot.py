import pyautogui
from python_imagesearch.imagesearch import imagesearch  # Görsel arama fonksiyonunu içe aktarıyoruz
import time

pyautogui.FAILSAFE = False  # PyAutoGUI için güvenlik önlemi devre dışı bırakılıyor
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
            print("Maç kabul edildi!")  # Ekrana mesaj yazdırıyoruz
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
