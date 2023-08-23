import os
import uvicorn
from src.index import app



#uvicorn.run(app,host='0.0.0.0',port=8000)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=True)