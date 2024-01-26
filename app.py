from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name is None:
        return "Missing 'n' parameter", 400

    file_path = f'/tmp/data/{file_name}.txt'

    if line_number is not None:
        try:
            line_number = int(line_number)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= line_number <= len(lines):
                    return lines[line_number - 1].strip()
                else:
                    return "Invalid 'm' parameter", 400
        except ValueError:
            return "Invalid 'm' parameter", 400

    else:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return f"File '{file_path}' not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
