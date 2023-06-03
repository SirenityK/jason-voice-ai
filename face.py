import face_recognition as fr
import pickle
import cv2
import os
import re

class Recognition:
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture(0)
        self.image_files = os.listdir('images')
        self.names = [re.sub('(.)?(jpg|png)', '', i).capitalize() for i in self.image_files]

    def save_encodings(self):
        known_images = [fr.load_image_file(os.path.join('images', i)) for i in self.image_files]
        image_encodings = [fr.face_encodings(i, num_jitters=50, model='large')[0] for i in known_images]
        with open('face_encodings.pkl', 'wb') as f:
            pickle.dump(image_encodings, f)
        
    def initialize_encodings(self):
        with open('face_encodings.pkl', 'rb') as f:
            self.image_encodings = pickle.load(f)
        
    def detect_face(self):
        print('Detecting face...')
        ret, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = frame[:, :, ::-1]
        
        if not fr.face_locations(frame):
            return '[No se detectó una cara en la cámara]'

        try:
            unknown_encoding = fr.face_encodings(frame)[0]
            face_detected_index = fr.compare_faces(self.image_encodings, unknown_encoding).index(1)
            print('Finish!')
            return self.names[face_detected_index]
        except (IndexError, ValueError):
            print('Finish!')
            return 'Alguien que no reconoces'
    
if __name__ == '__main__':
    recognition = Recognition()
    recognition.save_encodings()