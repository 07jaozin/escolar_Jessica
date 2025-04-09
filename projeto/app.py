import os
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import datetime




app=Flask(__name__)


#db_path = os.path.join(os.getcwd(), 'site.db')f'sqlite:///{db_path}'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'instance/static/img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key="curso_flask"
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=900)

#tabelas
class Materias(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   titulo = db.Column(db.String(100), nullable = False)
   materia = db.Column(db.String(100), nullable = False)
   link = db.Column(db.String(1000), nullable = False)
   nome_link = db.Column(db.String(100), nullable = False)
   foto = db.Column(db.String(600), nullable = False)
   
with app.app_context():  
    
    #db.drop_all()
    db.create_all()  

@app.route('/')
def principal():
   return render_template("index.html")
  
@app.route('/form')
def form():
   #if session not in('adm'):
    # return redirect('/')
   return render_template("form.html")   
@app.route('/adiciona_materia', methods = ['POST'])
def adiciona():
   titulo = request.form.get('titulo')
   link = request.form.get('link')
   nome_link = request.form.get('nome_link')
   materia = request.form.get('materia')
   foto = request.files['foto']
   caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], foto.filename)
   print(caminho_imagem)
   foto.save(caminho_imagem)
   novo_material = Materias( titulo = titulo, materia = materia, link = link, nome_link = nome_link, foto = caminho_imagem)
   db.session.add(novo_material)
   db.session.commit()
   return redirect('/')
@app.route('/fisica')
def material():
   
   materias = Materias.query.filter_by(materia = 'fisica').all()
   for materiais in materias:
      print(materiais.titulo)
      print(materiais.foto)
  
   return render_template("material.html", materias = materias)
@app.route('/educacao_financeira')
def educacao_financeira():
   
   materias = Materias.query.filter_by(materia = 'educacao_financeira').all()
   for materiais in materias:
      print(materiais.titulo)
      print(materiais.foto)
  
   return render_template("material.html", materias = materias)
@app.route('/matematica')
def matematica():
   
   materias = Materias.query.filter_by(materia = 'matematica').all()
   for materiais in materias:
      print(materiais.titulo)
      print(materiais.foto)
  
   return render_template("material.html", materias = materias)

@app.route('/excluir/<int:id>')
def excluir(id):
   if 'adm' not in session:
      return redirect('/')
   excluido = Materias.query.filter_by(id = id).first()
   db.session.delete(excluido)
   db.session.commit()
   return redirect('/')
@app.route('/formEdit/<int:id>')
def formEdit(id):
   if 'adm' not in session:
      return redirect('/')
   item = Materias.query.filter_by(id = id).first()
   return render_template("editar.html", item = item)

@app.route('/editando/<int:id>', methods = ['POST'])
def editando(id):
   if 'adm' not in session:
      return redirect('/')
   print(id)
   editando = Materias.query.get(id)
   titulo = request.form.get('titulo-editar')
   link = request.form.get('link-editar')
   nome_link = request.form.get('nome_link-editar')

   if editando:
      editando.titulo = titulo
      editando.link = link
      editando.nome_link = nome_link
   db.session.commit()
   return redirect('/')
    
@app.route('/log')
def log():
    return render_template("logar.html")
@app.route('/log_adm', methods = ['POST'])
def log_adm():
   nome = request.form.get('nome')
   senha = request.form.get('senha')
   nomeSemEspacos = nome.strip()
   senhaSemEspacos = senha.strip()

   if nomeSemEspacos == 'desen' and senhaSemEspacos == 'desen':
      session['adm'] = True
      return redirect('/')
   return redirect('/log')
   
@app.route('/logout')
def logout():
    if 'adm' not in session:
      return redirect('/')
    session.pop('adm', default=None)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)