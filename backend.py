from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        # Return operation code for GET request
        return jsonify({"operation_code": 1}), 200

    elif request.method == 'POST':
        try:
            data = request.json.get('data', [])
            user_id = "john_doe_17091999"  # Replace with dynamic user details as needed
            email = "john@xyz.com"
            roll_number = "ABCD123"
            
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            highest_lowercase = [max([char for char in data if char.islower()])] if any(char.islower() for char in data) else []

            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase
            }

            return jsonify(response), 200
        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
