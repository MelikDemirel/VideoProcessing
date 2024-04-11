# OpenCV kütüphanesini içe aktar
import cv2

# VideoCapture nesnesi oluştur ve "Rocky.mp4" adlı video dosyasını aç
cap = cv2.VideoCapture("Rocky.mp4")
# Eğer bir web kamerası kullanacaksanız, 0 kullanabilirsiniz.

# Sonsuz bir döngü başlat
while True:
    # Video dosyasından bir çerçeve al
    ret, frame = cap.read()
    
    # Eğer çerçeve alınamazsa (video sona erdiyse), döngüden çık
    if ret == 0:
        break
    
    # Çerçeveyi yatay olarak çevir
    frame = cv2.flip(frame, 1)
    
    # Çerçeveyi ekranda göster
    cv2.imshow("webcam", frame)
    
    # Eğer kullanıcı 'q' tuşuna basarsa, döngüden çık
    if cv2.waitKey(10) & 0xff == ord("q"):
        break

# Video yakalama nesnesini serbest bırak
cap.release()

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
