import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
import tensorflow_datasets as tfds

datos, metadatos = tfds.load("fashion_mnist", as_supervised = True, with_info =  True)

metadatos

datos_entrenamiento, datos_pruebas = datos["train"], datos["test"]

nombres_objetos = ["Camiseta", "Pantalon", "Pull-over", "Saco", "Sandalia", "Camisa", "Zapatilla de deporte", "Bolsa", "Botin", "Vestidos"]
nombres_clases = metadatos.features["label"].names
nombres_objetos

def normalizar(imagenes, nombres_objetos):
  imagenes = tf.cast(imagenes, tf.float32)
  imagenes /= 255
  return imagenes, nombres_objetos

datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)

datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()

for imagen, etiqueta in datos_entrenamiento.take(1):
  break
imagen = imagen.numpy().reshape((28,28))
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(imagen, cmap = plt.cm.binary)
plt.colorbar()
plt.grid(True)
plt.show()


