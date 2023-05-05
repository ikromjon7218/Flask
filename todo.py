from flask import Flask, request, render_template
from sqlite3 import connect
dastur = Flask("Flaskda birinchi loyiha")

@dastur.route('/')
def home():
    with connect("todo.db") as ombor:
        kursor= ombor.cursor()
        kursor.execute(
            """
            select * from Reja
            """
        )
dastur.run()