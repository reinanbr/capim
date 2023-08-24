from fastapi import UploadFile, File, HTTPException, Request,APIRouter
import os


from src.capim_ia.capim import Capim,read_data
from src.tools.ip_tools import get_filename_from_ip
from src.tools.constants import PATH_DIR_TMP



router = APIRouter(prefix='/capim',tags=['capim'])



@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:

        client_ip = file.client.host
        
        filename_excel = get_filename_from_ip(client_ip,type_file='.xlsx')
        save_path_excel = os.path.join(PATH_DIR_TMP, filename_excel)
        with open(save_path_excel, "wb") as f:
            f.write(file.file.read())
            
        data_xlsx = read_data(save_path_excel)
        cp = Capim()
        cp.train(data=data_xlsx)
        filename_model_trained = get_filename_from_ip(client_ip,type_ip='.h5')
        save_path_model = os.path.join(PATH_DIR_TMP,filename_model_trained)
        cp.save_model(save_path_model)
        return {"message": "Upload e leitura de dados bem-sucedido!", "filename_excel": filename_excel, "path": save_path_excel}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

