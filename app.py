from flask import Flask, jsonify, request
import os

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Suhani",
        "course": "MCA",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Ananya",
        "course": "BCA",
        "marks": 78
    }
]


# Home / API status
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Python Student API is running!"
    })


# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# Get one student by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({
        "error": "Student not found"
    }), 404


# Add a new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"],
        "marks": data["marks"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


# Run the application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )