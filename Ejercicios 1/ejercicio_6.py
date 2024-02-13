import ply.lex as lex

tokens = (
    "NOMBRE_APELLIDOS",
    "DNI",
    "EMAIL",
    "CIUDAD_PAIS",
    "TELFONO",
    "MATRICULA"
)

t_NOMBRE_APELLIDOS = r'\w+\s\w+'
t_DNI = r'\d{8}[A-Z]'
t_EMAIL = r'[\w\.-]+@[\w\.-]+\.\wvxs?com?edu?gov?int?mil?(arpa)?net?'
t_CIUDAD_PAIS = r'\w+\s\(\w+\)'
t_MATRICULA = r'^\d{4}-\d{3,4}$'