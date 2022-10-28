from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

port = 3000

temperaturas = pd.read_csv('temperaturas.csv', sep=";")
print(temperaturas)

#datos de entrenamiento
k = temperaturas["k"]
c = temperaturas["c"]

#modelo de entrenamiento, con 1 capa densa (Oculta)
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar el modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss="mean_squared_error")

#entrenar el modelo
epocas = modelo.fit(k,c, epochs=200, verbose=0)

#probar nuestra IA
resp = modelo.predict([5778])
print(resp)


class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()
            