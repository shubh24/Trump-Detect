import cv2, os
import numpy as np
from PIL import Image

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    images = []

    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        faces = faceCascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
    return images

path = './Script-Positive'
images = get_images_and_labels(path)
cv2.destroyAllWindows()

recognizer.train(images, np.array([1]*len(images)))

path = './Testing'
image_paths = [os.path.join(path, f) for f in os.listdir(path)]

for image_path in image_paths:
    print image_path    
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    
    for (x, y, w, h) in faces:
        pred, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        print pred, conf
