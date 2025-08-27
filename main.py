from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from config import app

from models import *
from formulario import FormularioEvento

"""
pip install flask, flask-wtf
flask_sqlalchemy, flask_login

"""


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterForm

    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data
        print(f'-- {usu} -- {sen}')

        usu_ex = User.query.filter_by(username=usu).first()

        if usu_ex:
            print('Usuario ja existe')
            flash('Usuário já existe!', 'error')
        else:
            novo_usuario = User(username=usu)
            novo_usuario.set_password(sen)
            db.session.add(novo_usuario)
            db.session.commit()
            print('Usuario Criado')
            flash('Usuário criado com sucesso!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from forms import LoginForm
    
    formulario = LoginForm()
    
    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data
        
        usuario = User.query.filter_by(username=usu).first()
        
        if usuario and usuario.check_password(sen):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha incorretos!', 'error')
    
    return render_template('login.html', form=formulario)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    todos_eventos = Evento.query.all()
    meus_eventos = Evento.query.filter_by(id_usuario=current_user.id).all()
    
    return render_template('dashboard.html', todos_eventos=todos_eventos, meus_eventos=meus_eventos)


@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():

    formulario = FormularioEvento()

    if formulario.validate_on_submit():
        nome = formulario.nome.data
        desc = formulario.descricao.data
        dat = formulario.data.data

        novoEvento = Evento(nome=nome, descricao=desc, dataEvento=dat, id_usuario=current_user.id)
        db.session.add(novoEvento)
        db.session.commit()

        print('-'*10)
        print(f'> {nome}')
        print(f'> {desc}')
        print(f'> {dat}')
        print('-'*10)

        flash('Evento criado com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_event.html', form=formulario)


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    evento = Evento.query.get_or_404(event_id)
    
    # Verificar se o usuário é dono do evento
    if evento.id_usuario != current_user.id:
        flash('Você não tem permissão para editar este evento!', 'error')
        return redirect(url_for('dashboard'))
    
    formulario = FormularioEvento()
    
    if formulario.validate_on_submit():
        evento.nome = formulario.nome.data
        evento.descricao = formulario.descricao.data
        evento.dataEvento = formulario.data.data
        
        db.session.commit()
        flash('Evento atualizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    
    # Preencher formulário com dados existentes
    formulario.nome.data = evento.nome
    formulario.descricao.data = evento.descricao
    formulario.data.data = evento.dataEvento
    
    return render_template('edit_event.html', form=formulario, evento=evento)


@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    evento = Evento.query.get_or_404(event_id)
    
    # Verificar se o usuário é dono do evento
    if evento.id_usuario != current_user.id:
        flash('Você não tem permissão para excluir este evento!', 'error')
        return redirect(url_for('dashboard'))
    
    db.session.delete(evento)
    db.session.commit()
    
    flash('Evento excluído com sucesso!', 'success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
