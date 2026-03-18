from flask import Flask, request, jsonify

app = Flask(__name__)

devices = {}

@app.route('/')
def home():
    return "Mobile Tracker Server Running"

@app.route('/track', methods=['POST'])
def track():
    data = request.json

    device_id = data.get("device_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    sim_changed = data.get("sim_changed")
    ip = request.remote_addr

    devices[device_id] = {
        "latitude": latitude,
        "longitude": longitude,
        "ip": ip,
        "sim_changed": sim_changed
    }

    if sim_changed:
        print("[🚨 ALERT] SIM CHANGE DETECTED!")

    print(f"[+] Device: {device_id}")
    print(f"    Location: {latitude}, {longitude}")

    return jsonify({"status": "success"})

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
