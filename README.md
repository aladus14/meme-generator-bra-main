# 😂 Gerador de Memes — Projeto da Turma

Projeto feito em **Python (Flask)** para praticar **elementos interativos**: um formulário onde o usuário escolhe uma imagem de meme, digita um texto superior e inferior, escolhe a cor do texto e a posição, e vê o resultado atualizado na hora.

Este README foi feito para ajudar você a **rodar o projeto na sua máquina** e **entender onde mexer** para completar a atividade.

---

## ✅ O que você precisa ter instalado

1. **Python 3** — [baixe aqui](https://www.python.org/downloads/) se ainda não tiver.
   - Para conferir se já tem, abra o terminal e digite:
     ```bash
     python --version
     ```
2. **Flask** — instalamos no passo a seguir, não precisa baixar nada agora.

---

## 🚀 Passo a passo para rodar o projeto

**1. Baixe o projeto** e entre na pasta dele pelo terminal.

**2. Instale o Flask**
```bash
pip install flask
```
> Se der erro de "comando não encontrado", tente `pip3 install flask` ou `python -m pip install flask`.

**3. Rode a aplicação**
```bash
python main.py
```

**4. Abra no navegador**

O terminal vai mostrar algo como:
```
Running on http://127.0.0.1:5000
```
Copie esse endereço e cole no navegador. 🎉

> Para parar a aplicação, volte ao terminal e aperte `Ctrl + C`.

---

## 🧭 Como o projeto está organizado

```
gerador-de-memes/
├── main.py                → rota principal e lógica que recebe os dados do formulário
├── templates/
│   └── index.html          → página com o formulário e a pré-visualização do meme
└── static/
    ├── css/
    │   └── style.css        → estilo visual da página
    └── img/                 → imagens dos memes (logo.svg, meme_1.jpg, meme_2.jpg, etc.)
```

- **`main.py`**: recebe o que o usuário preencheu no formulário (imagem, textos, cor, posição) e devolve a página atualizada com esses dados.
- **`templates/index.html`**: tem o formulário (`<select>`, `<input>`) e a área onde o meme aparece, usando variáveis do Jinja (`{{ }}`) para mostrar o que o backend enviou.
- **`static/`**: CSS e as imagens usadas nos memes.

---

## 🖱️ Como funciona

1. O usuário abre a página (`GET /`) e vê o formulário com a imagem padrão (`logo.svg`).
2. Ele escolhe um meme, digita os textos, escolhe cor e posição, e clica em **"Gerar meme"**.
3. O formulário envia os dados por `POST` para a rota `/`.
4. O `main.py` lê esses dados (`request.form.get(...)`) e reenvia a página (`render_template`) já com o meme montado.

---

## 📝 Atividades — o que precisa ser feito

O código está cheio de comentários `TAREFA` marcando onde você precisa completar algo. Siga a ordem abaixo — ela segue o fluxo da aula.

### Tarefa 1 — Adicionar mais opções de meme
📄 Arquivo: `templates/index.html`

Dentro do `<select id="image-selector">`, já existem duas opções de meme prontas:
```html
<option value="meme_1.jpg" {% if selected_image == 'meme_1.jpg' %}selected{% endif %}>Garota Desastre</option>
<option value="meme_2.jpg" {% if selected_image == 'meme_2.jpg' %}selected{% endif %}>Dois botões</option>
```
No comentário `TAREFA #1`, adicione novas opções seguindo esse mesmo padrão. Lembre de:
- Colocar a imagem correspondente dentro de `static/img/`
- O `value` deve ser exatamente igual ao nome do arquivo da imagem

### Tarefa 2 — Adicionar mais opções de cor
📄 Arquivo: `templates/index.html`

Logo abaixo, no `<select id="color-selector">`, já existem duas cores prontas:
```html
<option value="white" {% if selected_color == 'white' %}selected{% endif %}>Branco</option>
<option value="black" {% if selected_color == 'black' %}selected{% endif %}>Preto</option>
```
No comentário `TAREFA` (sem número, logo depois dessas duas opções), adicione mais cores seguindo o mesmo padrão. Exemplo:
```html
<option value="red" {% if selected_color == 'red' %}selected{% endif %}>Vermelho</option>
```

### Tarefa 2.1 a 2.4 — Backend: receber os dados do formulário
📄 Arquivo: `main.py`

A imagem selecionada já é capturada como exemplo:
```python
selected_image = request.form.get('image-selector')
```
Você precisa fazer o mesmo para os outros campos, seguindo o padrão `name="..."` de cada input/select no `index.html`:

- **Tarefa #2.1** — texto superior e inferior:
  ```python
  textTop = request.form.get('textTop')
  textBottom = request.form.get('textBottom')
  ```
- **Tarefa #2.2** — posição do texto (superior e inferior):
  ```python
  textTop_y = request.form.get('textTop_y')
  textBottom_y = request.form.get('textBottom_y')
  ```
- **Tarefa #2.3** — cor do texto:
  ```python
  selected_color = request.form.get('color-selector')
  ```
- **Tarefa #2.4** — envie todas essas variáveis para o template, junto da `selected_image` que já está lá:
  ```python
  return render_template('index.html',
                         selected_image=selected_image,
                         textTop=textTop,
                         textBottom=textBottom,
                         textTop_y=textTop_y,
                         textBottom_y=textBottom_y,
                         selected_color=selected_color,
                         )
  ```

> 💡 O nome usado em `request.form.get('...')` precisa ser **exatamente igual** ao `name="..."` do campo no `index.html`.

### Tarefa 3 — Aplicar a cor e a posição no estilo do texto
📄 Arquivo: `templates/index.html`

Depois que o backend (Tarefa 2) estiver enviando `selected_color`, `textTop_y` e `textBottom_y`, você precisa usar essas variáveis para estilizar o texto do meme.

No texto de cima, o comentário `TAREFA #3` pede para completar:
```html
<p class="text_top" style="color: {{preencha}}; top: {{preencha}}%;">
```
Troque `{{preencha}}` pelas variáveis certas:
```html
<p class="text_top" style="color: {{ selected_color }}; top: {{ textTop_y }}%;">
```

No texto de baixo, o segundo `TAREFA #3` pede a mesma coisa, mas usando `bottom` em vez de `top`:
```html
<p class="text_bottom" style="color: {{ selected_color }}; bottom: {{ textBottom_y }}%;">
```

---

## 🛠️ Problemas comuns

| Problema | Possível solução |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Rode `pip install flask` novamente, verifique se está na pasta certa |
| A imagem do meme não aparece | Confira se o arquivo está dentro de `static/img/` e se o `value` do `<option>` é igual ao nome do arquivo |
| O texto do meme não muda de posição/cor | Verifique se completou a Tarefa 2 (backend) **antes** da Tarefa 3, já que a Tarefa 3 depende das variáveis enviadas pelo backend |
| Nada acontece ao clicar em "Gerar meme" | Confira se o `name` de cada `<input>`/`<select>` bate exatamente com o nome usado em `request.form.get('...')` no `main.py` |

---

## 📚 Aprendizados desse projeto

- Como trabalhar com elementos interativos (`<select>`, `<input>`) em um formulário
- Como capturar dados de um formulário com `request.form.get(...)`
- Como reenviar dados para o HTML com `render_template`
- Como usar variáveis do Jinja dentro de atributos CSS (`style="color: {{ variavel }}"`) para deixar a página dinâmica
