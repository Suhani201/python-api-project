from flask import Flask, jsonify, request

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


@app.route("/")
def home():
    return jsonify({
        "message": "Python Student API is running!"
    })


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


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


if __name__ == "__main__":
    app.run(debug=True)