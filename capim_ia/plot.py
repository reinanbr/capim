import matplotlib.pyplot as plt
import numpy as np
from tools.objects import DataPlantio as dp
from tools.constants import PATH_DIR_TMP
import os

PATH_DIR_TMP_PLOT = PATH_DIR_TMP+'/plots'
if not os.path.isdir(PATH_DIR_TMP_PLOT):
    os.mkdir(PATH_DIR_TMP_PLOT)

plt.style.use('seaborn')

name_base = '_plot_'
def set_base_name_plot(name:str):
    global name_base
    name_base = name
    


def plot_gradient_caixa(data:dp):
    data = data.data_base
    caixas = np.array(data['caixas'])
    time = np.array(data['trimestre'])
    print(time)
    
    
    plt.cla()
    plt.clf()
    
    plt.plot(time,np.gradient(caixas))
    plt.title('Varição da Produção de Caixas')
    plt.xlabel('Trimestre')
    plt.ylabel('Quantidade de Caixas')
    
    filename_plot = f'plot_{name_base}_gradient_caixas.png'
    path_plot_save = os.path.join(PATH_DIR_TMP_PLOT,filename_plot)
    
    try:
        plt.savefig(path_plot_save,dpi=700)
        if os.path.isfile(path_plot_save):
            print('sucess save plot gradient caixas')
            return {"sucess":True,"plot_file_path":path_plot_save,
                    "plot_filename":filename_plot}
        else:
            return {"sucess":False,"error":f"file {path_plot_save} not found!"}
        
    except Exception as e:
        print(f' errorSavePlotGradientCaixas: error -> Not save {e}')
        return {"sucess":False,"error":f'file plot gradient caixas not save. error -> {e}'}