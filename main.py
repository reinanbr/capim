import os
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, render_template,request,session, redirect,url_for,flash, send_from_directory
from flask_cors import CORS, cross_origin

from tools.read_file import read_data
from tools.ip_tools import get_filename_from_ip
from tools.constants import PATH_DIR_TMP

from capim_ia.plot import plot_gradient_caixa


from routes import tmp

app = Flask(__name__,static_url_path='/static',template_folder='templates')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(tmp.tmp_blueprint)


@app.route('/',methods=['GET'])
def index():
    ip = request.remote_addr
    print(request.headers)

    #save_ip(user)
    # sodf(user)
    return render_template('capim.html')




@app.route("/upload",methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify(message='Nenhum arquivo enviado'), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify(message='Nenhum arquivo selecionado'), 400
        
        if file:
            client_ip = request.remote_addr
            filename_excel = get_filename_from_ip(client_ip,type_file='.xlsx')
            save_path_excel = os.path.join(PATH_DIR_TMP, filename_excel)
            file.save(save_path_excel)
            if os.path.isfile(save_path_excel):
                print('sucess upload file')
                data_xlsx = read_data(save_path_excel)
                
                plot_file_gradient_caixas = plot_gradient_caixa(data_xlsx)
                files_plot_dict = {'plotGradientCaixas':plot_file_gradient_caixas}
                #cp = Capim()
                #cp.train(data=data_xlsx)
                filename_model_trained = get_filename_from_ip(client_ip,type_file='.h5')
                save_path_model = os.path.join(PATH_DIR_TMP,filename_model_trained)
                #cp.save_model(save_path_model)
                return jsonify(message="sucess",filesPlots=files_plot_dict),200
    except Exception as e:
        print('error in upload: ',str(e))
        return jsonify(mensagem=f"Error: {str(e)}")


