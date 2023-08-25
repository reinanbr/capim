from dataclasses import dataclass
import numpy as np



class DataPlantio:

    def read(self,data,data_base):
        self.output = data.get('output',None)
        self.input = data.get('input',None)
        self.data_base = data_base
    def __call__(self):
        print('data plantio is called')
        return self