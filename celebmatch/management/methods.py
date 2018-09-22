import math
from sklearn import neighbors
import pickle
import face_recognition
import numpy as np
import os

class Methods():
    def __init__(self):
        self.current_folder = os.path.dirname(__file__)
        with open(self.current_folder+'/celeb_new.pickle', 'rb') as handle:
            d = pickle.load(handle)

        self.X = list(d["encode"])
        self.X = np.array(self.X)

        self.y = list(d["name"])
        self.y = np.array(self.y)

    def train_classifier(self, knn_algo='ball_tree'):
        # Determine how many neighbors to use for weighting in the KNN classifier
        n_neighbors = int(round(math.sqrt(len(self.X))))

        #Create and train the KNN classifier
        knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
        knn_clf.fit(self.X, self.y)

        with open(self.current_folder+'/trained_knn_model.clf', 'wb') as f:
            pickle.dump(knn_clf, f)


    def predict(self, singe_face_encoding):
        # Load a trained KNN model (if one was passed in)
        with open(self.current_folder+'/trained_knn_model.clf', 'rb') as f:
            knn_clf = pickle.load(f)

        closest_distances = knn_clf.kneighbors(singe_face_encoding, n_neighbors=5)
        rating = closest_distances[0][0]
        celeb = closest_distances[1][0]

        # knn_clf.predict(singe_face_encoding)

        return rating, celeb

    def get_lookalike(self):
        back_folder = '/'.join(self.current_folder.split("/")[0:-1])
        image = face_recognition.load_image_file(back_folder+'/static/celebmatch/images/user_submitted.bmp')
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        face_encodings = np.array(face_encodings)

        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]
            rating, celeb = self.predict(face_encoding)
            celeb_name = []
            for x in celeb:
                celeb_name.append(self.y[x])
            return rating, celeb_name
        else:
            return 1, "Face Not Found"

    def get_lookalike_test(self):
        back_folder = '/'.join(self.current_folder.split("/")[0:-1])
        image = face_recognition.load_image_file(back_folder+'/static/celebmatch/images/user_submitted.bmp')
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        face_encodings = np.array(face_encodings)

        matches = face_recognition.compare_faces(self.X, face_encodings)
        matches = [i for i, x in enumerate(matches) if x]
        matches = [ self.y[x] for x in matches ]

        return matches