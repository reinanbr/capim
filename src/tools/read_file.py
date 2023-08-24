from src.tools.objects import DataPlantio
import numpy as np
import pandas as pd




# read excel
def read_data(file_excel:str)->dict[np.array]:
    data_prime = pd.read_excel(file_excel)
    data_end = {'input':np.array([list(data_prime['adubo']),
        list(data_prime['nitrato']),
        list(data_prime['agua'])
    ]),'output':np.array(list(data_prime['caixas']))}
    
    return DataPlantio(data_end)