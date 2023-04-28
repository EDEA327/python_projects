import pandas as pd
import turtle as t

# List of colombian departments
departments_colombia = [
    'Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bolívar', 'Boyacá',
    'Caldas', 'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Chocó', 'Córdoba',
    'Cundinamarca', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena',
    'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío', 'Risaralda',
    'San Andrés y Providencia', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca', 'Vaupés', 'Vichada'
]

img = "mapa_colombia.gif"
screen = t.Screen()
screen.setup(width=800, height=600)
screen.addshape(img)
t.shape(img)


def get_click_coors(x, y):
    print(x, y)
    return x, y


# creating a dictionary to convert it to Dataframe
coors = []

for dep in departments_colombia:
    print(dep)
    t.onclick(get_click_coors)


screen.mainloop()




