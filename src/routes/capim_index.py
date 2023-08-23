from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
from ipaddress import ip_address

from src.capim import Capim,read_data


app = FastAPI()

def get_filename_from_ip(client_ip):
    ip = ip_address(client_ip)
    filename = str(ip).replace('.', '') + '.xlsx'
    return filename

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:

        client_ip = file.client.host
        
        filename = get_filename_from_ip(client_ip)
        save_path = os.path.join('/usr/tmp', filename)
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        
        

        return {"message": "Upload e leitura de dados bem-sucedido!", "filename": filename, "path": save_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

