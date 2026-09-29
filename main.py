# Importação
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados do formulário
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        #OBSERVE OS IDS E NAMES DO INSPUTS E PROCURE PELO NOME DAS VARIÁVEIS QUE VOCÊ PRECISA COMO NO EXEMPLO ABAIXO
        # OBTENDO A IMAGEM DO MEME
        selected_image = request.form.get('image-selector')
        
        #TAREFA #2.1 OBTENHA O TEXTO SUPERIOR E INFERIOR DO MEME 
        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')

        #TAREFA #2.2 OBTENHA A POSIÇÃO SUPERIOR E INFERIOR DO TEXTO DO MEME
        textTop_y = request.form.get('textTop_y')
        textBottom_y = request.form.get('textBottom_y')

        #TAREFA #2.3 OBTENHA A COR DO TEXTO DO MEME
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               #OBSERVE O EXEMPLO ABAIXO DE COMO PASSAR AS VARIÁVEIS PARA O HTML
                               #EXIBINDO A IMAGEM SELECIONADA
                               selected_image=selected_image,
                               #TAREFA 2.4 ADICIONE AS OUTRAS VARIÁVEIS AQUI PARA EXIBIÇÃO NO HTML
                               textTop=textTop,
                               textBottom=textBottom,
                               textTop_y=textTop_y,
                               textBottom_y=textBottom_y,
                               selected_color=selected_color
                               
            
            
                               )
    else:
        # exibindo a primeira imagem por padrão
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)