#métodos
import flet as ft

# Se está definiendo un diccionario llamado 'nav_icon_style' que parece ser un conjunto de estilos para un icono de navegación.
nav_icon_style: dict = {
    # 'offset' parece ser una propiedad que define el desplazamiento del icono. Se está utilizando la clase 'Offset' del módulo 'flet.transform' para definir un desplazamiento de (0,0).
    "offset": ft.transform.Offset(0,0),
    # 'opacity' es una propiedad que define la opacidad del icono. Se está estableciendo a 1, lo que significa que el icono es completamente opaco.
    "opacity": 1,
    # 'animate_offset' parece ser una propiedad que define una animación para el desplazamiento del icono. Se está utilizando la clase 'Animation' del módulo 'flet' para definir una animación que dura 500 unidades de tiempo y se desacelera hacia el final.
    "animate_offset": ft.Animation(500, "decelerate"),
    # 'animate_opacity' parece ser una propiedad que define una animación para la opacidad del icono. Se está utilizando la clase 'Animation' del módulo 'flet' para definir una animación que dura 300 unidades de tiempo y se desacelera hacia el final.
    "animate_opacity": ft.Animation(300, "decelerate"),
    # 'disabled' es una propiedad que define si el icono está deshabilitado o no. Se está estableciendo a True, lo que significa que el icono está deshabilitado.
    #"disabled": True,
}



#navegación iconos y clases
class NavIcon(ft.Icon):
    def __init__(self, icon_name: str):
        super(NavIcon, self).__init__(name=icon_name, **nav_icon_style)

nav_item_style: dict = {
    "width": 40,
    "height": 40,
    "shape": ft.BoxShape("circle")
}

#navegación clase item...
class NavItem(ft.Container):
    def __init__(self, icon_name: str):
        super(NavItem,self).__init__(**nav_item_style)


        #crea instancias en NavIcon...
        self.icon = NavIcon(icon_name)
        self.content = self.icon

nav_text_style: dict = {
    "width": 105,
    "size": 11.5,
    "text_align": "center",
    "offset": ft.transform.Offset(0,1),
    "opacity": 0,
    "animate_offset": ft.Animation(350, "decelerate"),
    "animate_opacity": ft.Animation(500, "decelerate"),
}


#creando una clase para el texto de cada icono: 
class navText(ft.Text):
    def __init__(self, value: str):
        super(navText, self).__init__(value = value)
    


#columna de estilo
row_style: dict = {
    "top": 0,
    "bottom": 0,
    "left": 0,
    "right": 0,
    "alignment": "spaceAround",
    "vertical_alignment": "center",
    "expand": True,
    
}

def main (page: ft.Page) :
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#E1E6ED"
    
    #hace una lista de icones listados por nombre...
    icons: list = ["home", "person", "notifications", "settings", "copy"]
        
    stack: ft.Stack = ft.Stack(
        expand=True,
        controls = [
            ft.Row(
                **row_style,
                spacing = 0,
                controls = [NavItem(name) for name in icons],
            )
        ]
    )
    
    # Se llama al método 'add' del objeto 'page'. Este método se utiliza para agregar elementos a la página.
    page.add(
        # Se está creando un nuevo objeto 'Container' del módulo 'flet'. Un 'Container' es un tipo de elemento que puede contener otros elementos.
        ft.Container(
            # Se establece el ancho del contenedor en 500 unidades. El tipo de unidad no está especificado, pero podría ser píxeles.
            width=500,
            # Se establece la altura del contenedor en 55 unidades. Al igual que con el ancho, el tipo de unidad no está especificado.
            height=55,
            # Se establece la forma del contenedor como un rectángulo utilizando la clase 'BoxShape' del módulo 'flet'.
            shape = ft.BoxShape("rectangle"),
            # Se establece el radio del borde del contenedor en 10 unidades. Esto determina cuánto se redondean las esquinas del contenedor.
            border_radius = 10,
            # Se establece el color de fondo del contenedor en negro.
            bgcolor = "black",
        )
    )

    
    
    page.update()
    

if __name__ =="__main__":
    ft.app(target=main)