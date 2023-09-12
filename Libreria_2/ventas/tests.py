from django.test import TestCase

import random
from datetime import datetime, timedelta

users = [
    (1),
    (2),
    # ... Agrega el resto de los usuarios aquí
]

# Generar 50 sentencias SQL de inserción
for _ in range(1):
    user_id, username = random.choice(users)
    conexion_time = datetime(2023, random.randint(1, 8), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    desconexion_time = conexion_time + timedelta(hours=random.randint(1, 8))
    
    sql_insert = f"INSERT INTO libreria.tb_historial_actividad (fecha_hora_conexion, fecha_hora_desconexion, tiempo_conexion, username) VALUES ('{conexion_time}', '{desconexion_time}', {random.uniform(1, 8):.2f}, '{username}');"
    print(sql_insert)