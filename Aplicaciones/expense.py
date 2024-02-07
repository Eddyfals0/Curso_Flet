"""Apicacion de cobranza"""

#Modulos
from flet import flet, UserControl, Column, Row, Container, Text, padding, alignment

#clase main
class Expense(UserControl):
    
    def build(self):
        return Column(
            controls = []
        )

def start(page: flet.Page):
    page.title = "Flet Expense"