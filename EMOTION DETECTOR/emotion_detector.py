import cv2

cascade_face = cv2.CascadeClassifier('face.xml') 
cascade_eye = cv2.CascadeClassifier('eye.xml') 
cascade_smile = cv2.CascadeClassifier('smile.xml')

def detection(bw_video , img):
    face = cascade_face.detectMultiScale(bw_video, 1.3, 5)
    for (x_face, y_face, w_face, h_face) in face:
        cv2.rectangle(img, (x_face, y_face), (x_face+w_face, y_face+h_face), (255, 130, 0), 2)
        ri_grayscale = bw_video[y_face:y_face+h_face, x_face:x_face+w_face]
        ri_color = img[y_face:y_face+h_face, x_face:x_face+w_face] 


        eye = cascade_eye.detectMultiScale(ri_grayscale, 1.2, 18) 
        for (x_eye, y_eye, w_eye, h_eye) in eye:
            cv2.rectangle(ri_color,(x_eye, y_eye),(x_eye+w_eye, y_eye+h_eye), (0, 180, 60), 2) 
        smile = cascade_smile.detectMultiScale(ri_grayscale, 1.7, 20)
        for (x_smile, y_smile, w_smile, h_smile) in smile: 
            cv2.rectangle(ri_color,(x_smile, y_smile),(x_smile+w_smile, y_smile+h_smile), (0, 0, 255), 2)
    return img 

webcam = cv2.VideoCapture(0) 

while True:
    _, img = webcam.read() 
    bw_video = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    final = detection(bw_video, img) 

    
    cv2.imshow('Video', final) 
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break
webcam.release() 
cv2.destroyAllWindows() 