import cv2
yüztanıma = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#Yüz tanıma kütüphanesi
maskCascade = cv2.CascadeClassifier("cascade.xml") #maske tespiti yapan sınıflandırıcı

video=cv2.VideoCapture(1)#Kamerayı çalıştırmak için
video.set(3, 640)
video.set(4, 480)
font=cv2.FONT_HERSHEY_COMPLEX

def maskeBul(img1, x, y, w, h):  #verilen koordinat ve boyutlarda maske bulan fonksiyon

    maskeler = maskCascade.detectMultiScale(img1, 1.1, 4)  #tespit edilen maskeleri maskeler dizisine atar
    maske_varmi = False

    for (x1,y1,w1,h1) in maskeler: #tespit edilen her maskenin koordinat ve boyutları için

            if abs(x-x1) < (w)*0.1  and abs(y-y1)<(h)*0.1  : #maske koordinatları yüz koordinatlarına çok yakınsa


                cv2.rectangle(img1, (int(x1), int(y1+(h1/2))), (x + w, y + h), (233, 213, 21), 3)
                #maske koordinatı yüz koordinatına çok yakın olduğu için  maske için genişliğin yarısı kadar dikdörtgen çizer

                maske_varmi = True


    return maske_varmi#maske varsa true yoksa false döndürür


while True:
    sucess, img = video.read()  # Görüntüyü yakalayıp kontrol ediyoruz.
    yüzler = yüztanıma.detectMultiScale(img, 1.3, 5)  # Yüzleri tanımamız için
    for x, y, w, h in yüzler:  # yüzün konumlarını bulup fonksiyona yolluyor.
        cv2.rectangle(img, (int(x), (y)), (x + w, y + h), (0, 0, 0), 3)
        if maskeBul(img, x, y, w, h):#yüz bulursa fonksiyona yolluyor
            cv2.putText(img, 'Maske Var', (x, y - 10), font, 1.3, (0, 255, 0), 2, cv2.LINE_AA)
            # Yüzün üstüne yazı koydum
        else:
            cv2.putText(img, 'Maske Yok', (x, y - 10), font, 1.3, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Sonuc", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()