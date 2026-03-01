from deepface import DeepFace
import cv2
import os
from utils.database import mark_attendance

DATASET_PATH = "dataset"


def recognize_faces(image, boxes, session_id):

    marked_people = set()

    for (x1, y1, x2, y2) in boxes:

        face = image[y1:y2, x1:x2]

        if face.size == 0:
            continue

        temp_path = "temp.jpg"
        cv2.imwrite(temp_path, face)

        try:
            result = DeepFace.find(
                img_path=temp_path,
                db_path=DATASET_PATH,
                model_name="Facenet512",
                detector_backend="opencv",
                enforce_detection=False
            )

            if len(result[0]) > 0:

                identity = result[0].iloc[0]["identity"]
                name = os.path.basename(os.path.dirname(identity))

                # prevent duplicate inside same upload
                if name not in marked_people:
                    mark_attendance(name, session_id)
                    marked_people.add(name)

            else:
                name = "Unknown"

        except:
            name = "Unknown"

        # draw box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(image, name, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    return image, list(marked_people)