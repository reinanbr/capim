from dataclasses import dataclass
import numpy as np


@dataclass
class DataPlantio:
    output:np.array or None
    input:np.array or None

    def __init__(self,data: dict):
        self.output = data.get('output',None)
        self.input = data.get('ipnut',None)