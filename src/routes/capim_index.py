from fastapi import FastAPI, UploadFile, File, HTTPException, Request,APIRouter

from fastapi.responses import FileResponse
import os
from ipaddress import ip_address

from src.capim import Capim,read_data
from src.tools.ip_tools import get_filename_from_ip

PATH_DIR = '/usr/tmp'
router = APIRouter(prefix='/main',tags=['capim'])





@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:

        client_ip = file.client.host
        
        filename = get_filename_from_ip(client_ip)
        save_path = os.path.join(PATH_DIR, filename)
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        
        data_xlsx = read_data(save_path)
        cp = Capim()
        cp.train(data=data_xlsx)
        

        return {"message": "Upload e leitura de dados bem-sucedido!", "filename": filename, "path": save_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

