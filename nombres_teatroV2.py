nombres = [
        "Aaron", "Abel", "Abelardo", "Abrahán", "Adalberto", "Adán", "Adolfo", "Adrián", "Agustín", 
        "Alan", "Alberto", "Alejandro", "Alex", "Alfonso", "Alfredo", "Alonso", "Álvaro", "Amadeo", 
        "Amador", "Amando", "Ambrocio", "Anastasio", "Andrés", "Ángel", "Aníbal", "Antonio", "Ariel", 
        "Armando", "Arnaldo", "Arturo", "Asdrúbal", "Atilio", "Augusto", "Aurelio", "Baltasar", 
        "Bartolomé", "Benito", "Benjamín", "Bernabé", "Bernardo", "Berto", "Blas", "Bonifacio", 
        "Boris", "Bruno", "Calixto", "Camilo", "Carlos", "Casimiro", "Cayetano", "Cecilio", "César", 
        "Cesáreo", "Christian", "Christopher", "Ciro", "Claudio", "Clemente", "Columbano", "Conrado", 
        "Constantino", "Cornelio", "Cristian", "Cristóbal", "Damián", "Daniel", "Dante", "David", 
        "Demetrio", "Diego", "Dionisio", "Domingo", "Donato", "Eduardo", "Efraín", "Elías", "Eliseo", 
        "Emilio", "Enrique", "Erico", "Ernesto", "Esteban", "Eugenio", "Eusebio", "Evaristo", "Fabián", 
        "Federico", "Felipe", "Félix", "Fernando", "Fermín", "Fidel", "Flavio", "Florencio", "Francisco", 
        "Froilán", "Fructuoso", "Fulgencio", "Gabriel", "Gastón", "Gaudencio", "Gerardo", "Germán", 
        "Gilberto", "Gonzalo", "Gregorio", "Guillermo", "Gustavo", "Héctor", "Heliodoro", "Heriberto", 
        "Hernán", "Hilario", "Homero", "Horacio", "Hugo", "Humberto", "Ignacio", "Iker", "Ildefonso", 
        "Indalecio", "Inocencio", "Ireneo", "Isaac", "Isaias", "Isidro", "Ivan", "Jacinto", "Jacobo", 
        "Jaime", "Javier", "Jeremías", "Jesús", "Joaquín", "Jorge", "José", "Josué", "Juan", "Julio", 
        "Justo", "Lázaro", "Leandro", "Leonardo", "Leoncio", "Leopoldo", "Lino", "Lorenzo", "Lucas", 
        "Luciano", "Lucio", "Luis", "Manuel", "Marcelo", "Marcio", "Marco", "Marcos", "Mariano", 
        "Mario", "Martín", "Mateo", "Matías", "Mauricio", "Maximiliano", "Melchor", "Miguel", "Modesto", 
        "Narciso", "Natalio", "Nazario", "Nicanor", "Nicolás", "Nicomedes", "Noé", "Norberto", "Octavio", 
        "Olegario", "Omar", "Orestes", "Oscar", "Osvaldo", "Oswaldo", "Pablo", "Pancracio", "Patricio", 
        "Pedro", "Pepe", "Plinio", "Plácido", "Poncio", "Porfirio", "Primitivo", "Prudencio", "Rafael", 
        "Raimundo", "Ramiro", "Ramón", "Raúl", "Reinaldo", "Renato", "Ricardo", "Roberto", "Rodolfo", 
        "Rodrigo", "Rogelio", "Rolando", "Román", "Roque", "Rosendo", "Rubén", "Rufino", "Ruperto", 
        "Salomón", "Salvador", "Samuel", "Sancho", "Sandro", "Santiago", "Santos", "Sebastián", 
        "Segismundo", "Sergio", "Servando", "Severino", "Simón", "Sixto", "Tadeo", "Teodoro", "Teófilo", 
        "Tiburcio", "Timoteo", "Tobías", "Tomás", "Torcuato", "Ubaldo", "Ulises", "Urbano", "Valentín", 
        "Valerio", "Vicente", "Victor", "Víctor", "Vidal", "Virgilio", "Vladimir", "Wilfredo", "Xavier", 
        "Yago", "Zacarías", 
        "Abril", "Adela", "Adelina", "Adriana", "Agustina", "Aida", "Aitana", "Alba", "Alejandra", 
        "Alicia", "Alina", "Alma", "Alondra", "Amalia", "Amanda", "Amelia", "Ana", "Anabel", "Anastasia", 
        "Andrea", "Ángela", "Angélica", "Anita", "Anna", "Antonia", "Araceli", "Ariadna", "Aurora", 
        "Barbara", "Beatriz", "Begoña", "Belén", "Berta", "Blanca", "Bruna", "Camilia", "Candela", 
        "Carla", "Carlota", "Carmen", "Carolina", "Catalina", "Cecilia", "Celeste", "Celia", "Clara", 
        "Claudia", "Cleopatra", "Concepción", "Constanza", "Cristina", "Dafne", "Daniela", "Débora", 
        "Diana", "Dolores", "Dorotea", "Elena", "Elisa", "Elizabeth", "Eloísa", "Elvira", "Emilia", 
        "Emiliana", "Emma", "Encarnación", "Esmeralda", "Esperanza", "Estefanía", "Estela", "Ester", 
        "Eugenia", "Eva", "Evelyn", "Fátima", "Felicia", "Felicidad", "Fernanda", "Florencia", "Francisca", 
        "Gabriela", "Gema", "Georgina", "Geraldine", "Gertrudis", "Gisela", "Gloria", "Graciela", 
        "Guadalupe", "Guillermina", "Hannah", "Helena", "Hilda", "Irene", "Iris", "Isabel", "Isabela", 
        "Ivonne", "Jacinta", "Jazmín", "Jennifer", "Jessica", "Jimena", "Joaquina", "Josefa", "Josefina", 
        "Juana", "Julia", "Juliana", "Justina", "Karen", "Karina", "Katherine", "Laura", "Leandra", 
        "Leire", "Leonor", "Leticia", "Lidia", "Ligia", "Liliana", "Lola", "Lorena", "Lourdes", "Lucía", 
        "Luciana", "Lucrecia", "Luisa", "Luz", "Macarena", "Magdalena", "Manuela", "Marcela", "Margarita", 
        "María", "Mariana", "Mariángel", "Maribel", "Maricarmen", "Marina", "Marta", "Martina", "Matilde", 
        "Maura", "Maya", "Melania", "Mercedes", "Micaela", "Miguela", "Milagros", "Miriam", "Mónica", 
        "Nadia", "Natalia", "Nayara", "Nerea", "Nicolasa", "Nicole", "Nieves", "Noelia", "Noemí", 
        "Nora", "Norma", "Nuria", "Olga", "Olivia", "Ondina", "Orquídea", "Palmira", "Paloma", "Paola", 
        "Patricia", "Paula", "Paz", "Pedrina", "Pilar", "Priscila", "Purificación", "Rafaela", "Raquel", 
        "Rebeca", "Regina", "Reina", "Remedios", "Reyes", "Rita", "Rocío", "Rosa", "Rosalía", "Rosario", 
        "Ruth", "Sabrina", "Salomé", "Samantha", "Sandra", "Sara", "Silvia", "Sofía", "Soledad", "Sonia", 
        "Susana", "Talia", "Tamara", "Tania", "Tatiana", "Teresa", "Teresita", "Tiffany", "Tina", 
        "Tomasa", "Trinidad", "Úrsula", "Valentina", "Valeria", "Vanessa", "Vega", "Vera", "Verónica", 
        "Victoria", "Violeta", "Virginia", "Virtudes", "Viviana", "Ximena", "Yolanda", "Yvette", "Zoe"
    ]

tipos_show = [
    "Concierto musical",
    "Espectáculo      ",
    "Show de stand    ",
    "Show de magia    ",
    "Show de danza    "
]



ubicacion = ["platea    "
             ,"campo    "
             ,"vip      "]

datos_globales_usuarios = []

#MATRIZ DE PRECIOS



precios_show = []

dni_en_uso = []

id_usuarios = []

ids_usuario = []

solo_ids_show = []

datos_globales_contraseñas=[]

dni_usuarios= []

dni_global=[]

datos_de_ingreso_dni=[]

contraseñas_admin=["admin", 0]

dni_admins=[47346945, 46915515,46624535,44414250, 0]

ids_shows=[]

shows_con_capacidad=[]

ids_reserva=[]
#MATRICES
datos_globales = []

datos_globales_reserva = []

matriz = datos_globales
