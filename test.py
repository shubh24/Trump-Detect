import cv2, os
from PIL import Image
import pickle
import numpy as np
import urllib2
from bs4 import BeautifulSoup

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

images = pickle.load(open("pickle.p"))
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.train(images, np.array([1]*len(images)))


def doIt(url):

    req = urllib2.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
    response = urllib2.urlopen(req)
    image_path = open("./Testing/yo.jpg",'wb')
    data = response.read()
    image_path.write(data)
    response.close();

    predict_image_pil = Image.open(open("yo.jpg","r")).convert("L")

    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    min_conf = 32768
    
    for (x, y, w, h) in faces:
        pred, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        if conf < min_conf:
            min_conf = conf
    if min_conf <= 50:
        return "Trump Detected"
    else:
        return "Not here"

#doIt("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWBLHT-nkouhdDKqy5kLxXEUQ3MlCsGxOOB6fTbXBlVUReFcWUmCr0n9g")