from flask import Flask, request


app = Flask(__name__)

"""
@app.route("/send2", methods=["POST"])
def _from_rasp_zero2():
    try:
        recv_file = request.json
        print(f"recv file: {recv_file}")
        return "Success!"
    except Exception as e:
        return str(e)
"""

@app.route('/send', methods=['PUT'])
def _from_rasp_zero():
    try:
        data = request.json
        print(f"send {data}")
        return "Sucess!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='192.168.137.87', port='8083')
