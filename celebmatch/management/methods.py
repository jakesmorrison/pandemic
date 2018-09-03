import math
from sklearn import neighbors
import pickle
import face_recognition
import numpy as np
import os

class Methods():
    def __init__(self):
        self.current_folder = os.path.dirname(__file__)
    def train_classifier(self, knn_algo='ball_tree'):

        with open(self.current_folder+'/celeb.pickle', 'rb') as handle:
            d = pickle.load(handle)

        X = list(d["encode"])
        X = np.array(X)
        X = X.reshape(-1, 1)

        y = list(d["name"])
        y = np.array(y)
        y = y.reshape(-1, 1)


        # Determine how many neighbors to use for weighting in the KNN classifier
        n_neighbors = int(round(math.sqrt(len(X))))

        # Create and train the KNN classifier
        knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
        knn_clf.fit(X, y)

        with open(self.current_folder+'/trained_knn_model.clf', 'wb') as f:
            pickle.dump(knn_clf, f)

        return knn_clf


    def predict(self, singe_face_encoding):
        # Load a trained KNN model (if one was passed in)
        with open(self.current_folder+'/trained_knn_model.clf', 'rb') as f:
            knn_clf = pickle.load(f)

        closest_distances = knn_clf.kneighbors(singe_face_encoding, n_neighbors=1)
        closest_distances = closest_distances[0][0][0]

        # Predict
        return knn_clf.predict(singe_face_encoding), closest_distances


    def get_lookalike(self):
        back_folder = '/'.join(self.current_folder.split("/")[0:-1])
        image = face_recognition.load_image_file(back_folder+'/static/celebmatch/images/user_submitted.bmp')
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        face_encodings = np.array(face_encodings)

        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]
            predictions, closest_distances = self.predict(face_encoding)
            return predictions[0], closest_distances
        else:
            return "Face Not Found", 1