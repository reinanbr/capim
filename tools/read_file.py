from tools.objects import DataPlantio
import numpy as np
import pandas as pd




# read excel
def read_data(file_excel:str):
    data_prime = pd.read_excel(file_excel)
    data_end = {'input':np.array([list(data_prime['adubo']),
        list(data_prime['nitrato']),
        list(data_prime['agua'])
    ]),'output':np.array(list(data_prime['caixas']))}

    dp = DataPlantio()
    dp.read(data_end,data_base=data_prime)
    return dp