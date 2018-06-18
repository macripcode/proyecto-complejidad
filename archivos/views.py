from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from pulp import *
from itertools import product
from itertools import combinations
import re

def combinacion_parcelas(arr, r):
  return list(combinations(arr, r))


def handle_uploaded_file(input_file):
    
    foo = -1
   
    #Obtener el numero de parcelas k
    k = input_file.readline()
    k = k.replace('\n', '')
    k = k.replace('\r', '')
    k = int(k)

    #Obtener la duracion de las cosechas por cada parcela D sub i
    d_i = input_file.readline()
    d_i = d_i.replace('\n', '')
    d_i = d_i.replace('\r', '')
    d_i = d_i.split(' ')
    d_i.insert(0, foo)
    for i in range(1, k + 1):
        d_i[i] = int(d_i[i])

    #Obteniendo la suma total de las cosechas en cada parcela
    b = input_file.readline()
    b = b.replace('\n', '')
    b = b.replace('\r', '')
    b = int(b)

    #Obteniendo utilidades por cada parcela
    u_ij = []
    for x in range(0, k):
        u_ij.append(input_file.readline())
    for i in range(0, k):
        u_ij[i] = u_ij[i].replace('\n', '')
        u_ij[i] = u_ij[i].replace('\r', '')
        u_ij[i] = u_ij[i].split(' ')
    for i in range(0, k):
        for j in range(0, b):
            u_ij[i][j] = int(u_ij[i][j])

    for i in range(0, k + 1):
        if (i == 0):
            u_ij.insert(0, [])
        for j in range(0, j + 1):
            if (j == 0):
                u_ij[i].insert(0, foo)

    #mostrando parametros de entrada
    print("--------------------------------------->")
    print("        Parametros de entrada           ")
    print("--------------------------------------->")
    print("k: " + str(k))
    print("")
    print("Di:")
    print(d_i)
    print("")
    print("b: " + str(b))
    print("")
    print("Uij:")
    for i in range(0, k + 1):
        print(u_ij[i])
        print("")
    print("--------------------------------------->")
    #finalizando parametros de entrada
    
    print("--------------------------------------->")
    print("       Operaciones con Parcelas         ")
    print("--------------------------------------->")
    
    # Creando un array del tamano k+1 para "crear las parcelas"
    parcelas = []
    
    for i in range(1, k + 1):
        parcelas.append(i)
    
    print("Parcelas:")
    print(parcelas)
    
    #creando las combinaciones entre parcelas
    comb_parcelas = combinacion_parcelas(parcelas, 2)
    no_combinaciones = len(comb_parcelas)
    print("Combinaciones entre parcelas:")
    print(comb_parcelas)
    print("")
    print("Numero de combinaciones: " + str(no_combinaciones))
    print("--------------------------------------->")
    
    # Instantiate our problem class
    model = pulp.LpProblem("Problema de cultivo de parcelas", pulp.LpMaximize)
    
    #Variables de decision

    # Xij  1 -> Si la cosecha de la parcela i inicio en el periodo j
    #      0 -> Sino
    x_ij = []
    
    # Yi   = Unidad de tiempo j en donde se inicia la cosecha de la parcela i
    y_i = []
    
    #Aux_x_y = Variable auxiliar decision para cada pareja de parcelas
    aux = []
    
    #Inicializacion de matrices para variables
    for i in range(k + 1):
        x_ij.append([])
        y_i.append([])
        for j in range(b + 1):
            x_ij[i].append(None)
    
    for i in range(0, len(comb_parcelas)):
        aux.append(None)
    
    #Finalizando inicializacion de matrices para variables
    
    #Asignacion de variables en las matrices creadas

    for i in range(1, k + 1):
        stri = str(i) + "_"
        nameVarY_i = "y_" + stri
        y_i[i] = pulp.LpVariable(nameVarY_i, lowBound=0, cat='Integer')
        for j in range(1, b + 1):
            strj = str(j) + "_"
            nameVarX_ij = "x_" + stri + strj
            x_ij[i][j] = pulp.LpVariable(nameVarX_ij, lowBound=0, cat='Binary')
            
    for i in range(0, len(comb_parcelas)):
        x = str(comb_parcelas[i][0])
        y = str(comb_parcelas[i][1])
        stri = x + "_" + y
        nameVarAux_i = "aux_" + stri
        aux_var = pulp.LpVariable(nameVarAux_i, lowBound=0, cat='Binary')
        aux[i] = aux_var
        
    
    # Objective function
    model += lpSum( x_ij[i][j] * u_ij[i][j] for i, j in product(range(1, k + 1), range(1, b + 1))), "Max parcelas"
    
    # Constraints

    # Una parcela solo se puede cosechar una vez
    for i in range(1, k + 1):
        model += lpSum(x_ij[i][j] for j in range(1, b + 1)) == 1
    
    # No se puede empezar a cosechar en dos o mas parcelas
    for j in range(1, b + 1):
        model += lpSum(x_ij[i][j] for i in range(1, k + 1)) <= 1
    
    # Relacionando y_i con Xij
    
    for i in range(1, k + 1):
        model += y_i[i] == lpSum((x_ij[i][j] * j) for j in range(1, b + 1))
    
    # Evitando que hayan espacios en blanco
    
    for i in range(1, k + 1):    
        model += (y_i[i] + d_i[i] - 1) <= b 
        
    # Evitar solapamiento entre cosechas
  
    #Creando big M  
    
    big_m = 10000000000
    
    for i in range(0,len(comb_parcelas)):
        x = comb_parcelas[i][0]
        y = comb_parcelas[i][1]
        model += y_i[x] + d_i[x]  <= y_i[y] + big_m*aux[i]
        model += y_i[y] + d_i[y]  <= y_i[x] + big_m * (1 - aux[i])
        
    #----------------------------------->
    #Nota:Para cada combinacion de parejas se debe usar una variable de decision llamada Aux
    #para realizar la combinacion entre las parcelas se usa la funcion combinacion_parcelas
    #----------------------------------->

    print(model)
    
    print(model.solve())
    print(pulp.LpStatus[model.status])
    
    total_cosechas = 0
    tiempo_de_inicio_por_parcela = []
    
    tiempo_de_inicio_por_parcela.insert(0, foo)
    
    for i in range(1, k + 1):
        tiempo_de_inicio_por_parcela.append(0)
    
    for variable in model.variables():
        print "{} = {}".format(variable.name, variable.varValue)
        if (variable.varValue == 1) and (re.match(r'x_\d*_\d*_', variable.name) != None):
            nombre_variable = str(variable.name)
            nombre_variable = nombre_variable.replace('x_', '')
            nombre_variable = nombre_variable.split('_')
            i = int(nombre_variable[0])
            j = int(nombre_variable[1])
            total_cosechas += u_ij[i][j]
            tiempo_de_inicio_por_parcela[i] = j
    
    #--------------------------------------------
    #Generando la salida
    salida = ""
    salida += str(total_cosechas)
    salida += "\n"
    for i in range(1, k + 1):
        salida += str(tiempo_de_inicio_por_parcela[i]) + " "
    
    salida += "\n"
    
    #Imprimiendo la salida en la terminal
    print("--------------------------------------->")
    print("               Salida                   ")
    print("--------------------------------------->")
    print(salida)
    print("--------------------------------------->")


    
    
    #--------------------------------------------
    
    #Imprimiendo la salida en el archivo
    output_file = open('static/salida.txt', 'w')
    output_file.write(salida)
    output_file.close()
    
    return output_file
    
            


def public_page(request):
    
    output_file = 'vacio'
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            output_file = handle_uploaded_file(request.FILES['file'])
           
    else:
        form = UploadFileForm()
    
    context= {
        'form': form,
        'output_file': output_file,
    }
    
    return render(request, 'home.html', context )
    
    
    
