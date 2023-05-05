from flask import Flask, request, render_template, redirect
from sqlite3 import connect
loyiha = Flask("Flaskda birinchi loyiha")

@loyiha.route('/')
def df():
    return render_template('todo.html')

@loyiha.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nomi = request.form.get('n')
        sanasi = request.form.get('s')
        batafsili = request.form.get('b')
        holati = request.form.get('h')
        with connect('todo.db') as ombor:
            kursor = ombor.cursor()
            kursor.execute(
                """
                Insert into Reja
                values(?,?,?,?)
                """, (nomi, sanasi, batafsili, holati)
            )
        return redirect('/')
    with connect("todo.db") as ombor:
        kursor = ombor.cursor()
        kursor.execute(
            """
            select * from Reja
            """
        )
        plans = kursor.fetchall()
    return render_template('todo.html', rejalar=plans)

@loyiha.route('/ochirish/<nomi>')
def ochirish(nomi):
    with connect('todo.db') as ombor:
        kursor = ombor.cursor()
        kursor.execute(
            """
            Delete from Reja
            where nom=?
            """, (nomi,)
        )
    return redirect('/')
    # return redirect('/')
# @dastur.route('/register', methods=['GET', 'POST'])
# def registera():
#     if request.method == 'POST':
#         ism = request.form.get('I')
#         hy = request.form.get('I')
#         ism = request.form.get('I')
#         ism = request.form.get('I')
loyiha.run()