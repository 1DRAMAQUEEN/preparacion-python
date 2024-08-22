productos=[{
    "nombre": "melón",
    "precio": 1200,
    "categoria": "fruta"
},
{
    "nombre": "sandia",
    "precio": 2990,
    "categoria": "fruta"

},
{
    "nombre": "esparrago",
    "precio": 1990,
    "categoria": "verdura"
},
{
     "nombre": "zanahoria",
     "precio": 1790,
     "categoria": "verdura"
}]
for producto in productos: 
    print(f"El producto es  {producto['nombre']} y su precio es ${producto['precio']}")