import cv2#opencv kütüphanesi
video=cv2.VideoCapture(1)#Anlık kamerada tespit yapması için

yuztanima=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#tanınmış yüzlerle eğitilmiş yüz tanıma için hazır veritabanı

sayıcı=0
#Video framelerden oluştuğu için yeni frameler oluştuğu sürece bu kod çalışacak
while True:
	ret,frame=video.read()
	yuzler=yuztanima.detectMultiScale(frame,1.3, 5)
	#Yüzleri tanımamız için tanıma oranı ve hassaslık değerleri
	for x,y,w,h in yuzler:
		sayıcı=sayıcı+1
		veri='./resimler/a/'+ str(sayıcı) + '.jpg'#Veri toplanıyor..
		print("Resimler oluşturuluyor..." +veri)
		cv2.imwrite(veri, frame[y:y+h,x:x+w])
		# yüzün etrafına dikdörtgen koyduk
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 4)
	cv2.imshow("Kamera", frame)#Kullanıcıya göstermek için
	cv2.waitKey(1)#Bir işlem yapılana kadar açık kalsın
	if sayıcı>50:#3500 kere yüz tanıdığında kamerayı kapat
		break
video.release()
cv2.destroyAllWindows()