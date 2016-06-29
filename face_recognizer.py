import cv2, os
from PIL import Image
import pickle

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


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

pickle.dump(images, open("pickle.p","wb"))
