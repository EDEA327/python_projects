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
    coors.append((x, y))
    print(coors)
    print(len(coors))


# creating a dictionary to convert it to Dataframe
coors = [(42.0, -154.0), (-93.0, 59.0), (37.0, 72.0), (-90.0, 175.0), (-62.0, 115.0), (-18.0, 35.0), (-83.0, 24.0),
         (-40.0, -108.0), (17.0, 30.0), (-124.0, -67.0), (-43.0, 154.0), (-132.0, 23.0), (-108.0, 101.0), (-49.0, 11.0),
         (103.0, -31.0), (15.0, -63.0), (-83.0, -52.0), (-30.0, 198.0), (-68.0, 163.0), (-23.0, -29.0), (-161.0, -98.0),
         (-20.0, 114.0), (-89.0, -116.0), (-94.0, -4.0), (-105.0, 16.0), (-190.0, 234.0), (-37.0, 69.0), (-84.0, 124.0),
         (-83.0, -19.0), (-125.0, -32.0), (64.0, -96.0), (81.0, 31.0)]

x_coors = [coord[0] for coord in coors]
y_coors = [coord[1] for coord in coors]
print(x_coors, y_coors)

data_dict = {
    "Departments": departments_colombia,
    "x": x_coors,
    "y": y_coors,

}
# t.onclick(get_click_coors)
data = pd.DataFrame(data_dict)
data.to_csv("colombian_departments.csv")
screen.mainloop()
