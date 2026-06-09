from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def find_max_min(arr, low, high):

    # Base Case: One Element
    if low == high:
        return arr[low], arr[low]

    # Base Case: Two Elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_max, left_min = find_max_min(arr, low, mid)
    right_max, right_min = find_max_min(arr, mid + 1, high)

    # Conquer
    maximum = max(left_max, right_max)
    minimum = min(left_min, right_min)

    return maximum, minimum


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/find", methods=["POST"])
def find():

    data = request.get_json()
    arr = data["numbers"]

    maximum, minimum = find_max_min(arr, 0, len(arr)-1)

    return jsonify({
        "maximum": maximum,
        "minimum": minimum
    })


if __name__ == "__main__":
    app.run(debug=True)