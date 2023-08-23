import numpy as np
import tensorflow as tf
import pandas as pd

from tools.objects import DataPlantio
from tools.read_file import read_data




# croando leitor de dados para treinamento
class Capim:
    def __init__(self,learning_rate=0.01):
        self.model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(3,)),              
        tf.keras.layers.Dense(64, activation='relu'),     
        tf.keras.layers.Dense(1, kernel_regularizer=tf.keras.regularizers.l2(learning_rate))
    ])
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
        self.model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])
        


    def train(self,data:DataPlantio,epochs=1000):
        inputs,outputs = data.input, data.output
        history = self.model.fit(inputs, outputs, epochs=1000, verbose=0)
        return history.history


    def predict(self,new_inputs):
        predictions = self.model.predict(new_inputs)
        return predictions
