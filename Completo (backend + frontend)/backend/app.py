from flask import Flask, jsonify
from flask_cors import CORS
from data import (
    get_total_consumption,
    get_max_consumption,
    get_equipment_efficiency,
    get_renewable_energy_percentage,
    get_estimated_cost,
    get_sensors_data,
    get_current_temperature,
    get_energy_savings,
)

app = Flask(__name__)
CORS(app)

@app.route("/api/dashboard", methods=["GET"])
def get_dashboard_data():
    data = {
        "totalConsumption": get_total_consumption(),
        "maxConsumption": get_max_consumption(),
        "equipmentEfficiency": get_equipment_efficiency(),
        "renewableEnergy": get_renewable_energy_percentage(),
        "estimatedCost": get_estimated_cost(),
        "currentTemperature": get_current_temperature(),
        "energySavings": get_energy_savings()
    }
    return jsonify(data)

@app.route("/api/sensors", methods=["GET"])
def get_sensors():
    sensors_data = get_sensors_data()
    return jsonify(sensors_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
