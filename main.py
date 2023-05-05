from sqlite3 import connect
from flask import Flask, request, render_template

dastur = Flask("Flaskda birinchi loyiha")

@dastur.route('/')
def home():
    with connect("todo.db") as ombor:
        kurs= ombor.cursor()










# with connect("todo.db") as ombor:
#     kursor = ombor.cursor()
#     kursor.execute(
#         """
#         insert into Reja
#         Values("Uxlash", "14.1.2022", "Algebra", "Kech qoldi")
#         """
#     )
#
# with connect("todo.db") as ombor:
#
#         kursor = ombor.cursor()
#         kursor.execute(
#         """
#         Create table Reja(
#             nom varchar,
#             vaqt varchar,
#             batafsil varchar,
#             status varchar
#         )
#         """
#         )
#
