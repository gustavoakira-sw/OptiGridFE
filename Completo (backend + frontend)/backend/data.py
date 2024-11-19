import random
from datetime import datetime, timedelta
from typing import Tuple


def get_total_consumption():
    # Simula o consumo total de energia em kWh (com variação entre 3000 e 5000 kWh)
    return round(random.uniform(3000, 5000), 2)

def get_max_consumption():
    # Simula o consumo máximo configurado
    return 5000

def get_equipment_efficiency():
    # Simula a eficiência dos equipamentos em % (valor aleatório entre 80 e 95)
    return random.randint(80, 95)

def get_renewable_energy_percentage():
    # Simula a porcentagem de energia renovável usada (valor aleatório entre 70% e 90%)
    return random.randint(70, 90)

def get_estimated_cost():
    # Simula o custo estimado com base no consumo total (preço por kWh = 0.35)
    total_consumption = get_total_consumption()
    cost_per_kwh = 0.35
    return round(total_consumption * cost_per_kwh, 2)

def get_current_temperature() -> float:
    # Simula a temperatura atual em graus Celsius
    return round(random.uniform(20, 30), 1)

def get_energy_savings() -> int:
    # Simula a redução de energia por otimização em %
    return random.randint(5, 25)

def get_sensors_data():
    # Simula os dados dos sensores
    sensors = [
        {
            "id": 1,
            "name": "Sensor de Temperatura",
            "status": "Online",
            "metric": f"{random.randint(20, 30)}°C",  # Temperatura entre 20 e 30 graus
            "lastReading": (datetime.now() - timedelta(minutes=random.randint(10, 60))).strftime("%d/%m/%Y %H:%M")
        },
        {
            "id": 2,
            "name": "Sensor de Consumo de Energia",
            "status": "Online",
            "metric": f"{round(random.uniform(1000, 5000), 2)} kWh",  # Consumo entre 1000 e 5000 kWh
            "lastReading": (datetime.now() - timedelta(minutes=random.randint(10, 60))).strftime("%d/%m/%Y %H:%M")
        },
        {
            "id": 3,
            "name": "Sensor de Umidade",
            "status": "Offline" if random.random() < 0.1 else "Online",
            "metric": f"{random.randint(40, 60)}%",  # Umidade entre 40% e 60%
            "lastReading": (datetime.now() - timedelta(minutes=random.randint(10, 60))).strftime("%d/%m/%Y %H:%M")
        },
        {
            "id": 4,
            "name": "Sensor de Ar Condicionado",
            "status": "Online",
            "metric": f"{random.randint(800, 1200)} W",  # Potência do ar condicionado entre 800W e 1200W
            "lastReading": (datetime.now() - timedelta(minutes=random.randint(10, 60))).strftime("%d/%m/%Y %H:%M")
        }
    ]
    return sensors
