from flask import Flask, render_template, request
import os
import cv2
from datetime import datetime

from utils.face_detect import detect_faces
from utils.face_recognize import recognize_faces
from utils.database import init_db

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PROCESSED_FOLDER = "static/processed"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    image = cv2.imread(path)

    boxes = detect_faces(image)

    # ✅ generate session id for this upload
    session_id = datetime.now().strftime("%Y%m%d%H%M%S")

    processed_img, attendance = recognize_faces(
        image,
        boxes,
        session_id
    )

    output_path = os.path.join(
        app.config["PROCESSED_FOLDER"],
        "output.jpg"
    )

    cv2.imwrite(output_path, processed_img)

    return render_template(
        "result.html",
        processed_image=output_path,
        attendance=attendance
    )

from utils.database import get_total_attendance


@app.route("/total_attendance")
def total_attendance():

    data = get_total_attendance()

    return render_template(
        "total_attendance.html",
        records=data
    )
if __name__ == "__main__":
    app.run(debug=True)