{"filter":false,"title":"views.py","tooltip":"/archivos/views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":149,"column":0},"end":{"row":149,"column":2},"action":"remove","lines":["  "],"id":165},{"start":{"row":150,"column":0},"end":{"row":150,"column":2},"action":"remove","lines":["  "]},{"start":{"row":151,"column":0},"end":{"row":151,"column":4},"action":"remove","lines":["    "]},{"start":{"row":153,"column":0},"end":{"row":153,"column":2},"action":"remove","lines":["  "]},{"start":{"row":154,"column":0},"end":{"row":154,"column":2},"action":"remove","lines":["  "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"remove","lines":["    "]},{"start":{"row":157,"column":0},"end":{"row":157,"column":2},"action":"remove","lines":["  "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":2},"action":"remove","lines":["  "]},{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"remove","lines":["    "]},{"start":{"row":162,"column":0},"end":{"row":162,"column":2},"action":"remove","lines":["  "]},{"start":{"row":163,"column":0},"end":{"row":163,"column":2},"action":"remove","lines":["  "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":2},"action":"remove","lines":["  "]},{"start":{"row":165,"column":0},"end":{"row":165,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":149,"column":0},"end":{"row":149,"column":4},"action":"insert","lines":["    "],"id":166},{"start":{"row":150,"column":0},"end":{"row":150,"column":4},"action":"insert","lines":["    "]},{"start":{"row":151,"column":0},"end":{"row":151,"column":4},"action":"insert","lines":["    "]},{"start":{"row":152,"column":0},"end":{"row":152,"column":4},"action":"insert","lines":["    "]},{"start":{"row":153,"column":0},"end":{"row":153,"column":4},"action":"insert","lines":["    "]},{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"insert","lines":["    "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"insert","lines":["    "]},{"start":{"row":156,"column":0},"end":{"row":156,"column":4},"action":"insert","lines":["    "]},{"start":{"row":157,"column":0},"end":{"row":157,"column":4},"action":"insert","lines":["    "]},{"start":{"row":158,"column":0},"end":{"row":158,"column":4},"action":"insert","lines":["    "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":4},"action":"insert","lines":["    "]},{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"insert","lines":["    "]},{"start":{"row":161,"column":0},"end":{"row":161,"column":4},"action":"insert","lines":["    "]},{"start":{"row":162,"column":0},"end":{"row":162,"column":4},"action":"insert","lines":["    "]},{"start":{"row":163,"column":0},"end":{"row":163,"column":4},"action":"insert","lines":["    "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":4},"action":"insert","lines":["    "]},{"start":{"row":165,"column":0},"end":{"row":165,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":151,"column":4},"end":{"row":151,"column":8},"action":"insert","lines":["    "],"id":167}],[{"start":{"row":155,"column":4},"end":{"row":155,"column":8},"action":"insert","lines":["    "],"id":168}],[{"start":{"row":160,"column":4},"end":{"row":160,"column":8},"action":"insert","lines":["    "],"id":169}],[{"start":{"row":165,"column":4},"end":{"row":165,"column":8},"action":"insert","lines":["    "],"id":170}],[{"start":{"row":165,"column":44},"end":{"row":166,"column":0},"action":"insert","lines":["",""],"id":171},{"start":{"row":166,"column":0},"end":{"row":166,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":166,"column":8},"end":{"row":167,"column":0},"action":"insert","lines":["",""],"id":172},{"start":{"row":167,"column":0},"end":{"row":167,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":167,"column":4},"end":{"row":167,"column":8},"action":"remove","lines":["    "],"id":173}],[{"start":{"row":167,"column":4},"end":{"row":179,"column":62},"action":"insert","lines":[" # Evitar solapamiento entre cosechas","  ","  #Creando big M  ","  ","  big_m = 10000000000","","  #Aqui es solo menor","","  for i in range(0,len(comb_parcelas)):","    x = comb_parcelas[i][0]","    y = comb_parcelas[i][1]","    model += y_i[x] + d_i[x]  <= y_i[y] + big_m*aux[i]","    model += y_i[y] + d_i[y]  <= y_i[x] + big_m * (1 - aux[i])"],"id":174}],[{"start":{"row":167,"column":4},"end":{"row":167,"column":5},"action":"remove","lines":[" "],"id":175}],[{"start":{"row":169,"column":0},"end":{"row":169,"column":2},"action":"remove","lines":["  "],"id":176},{"start":{"row":170,"column":0},"end":{"row":170,"column":2},"action":"remove","lines":["  "]},{"start":{"row":171,"column":0},"end":{"row":171,"column":2},"action":"remove","lines":["  "]},{"start":{"row":173,"column":0},"end":{"row":173,"column":2},"action":"remove","lines":["  "]},{"start":{"row":175,"column":0},"end":{"row":175,"column":2},"action":"remove","lines":["  "]},{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"remove","lines":["    "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"remove","lines":["    "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":4},"action":"remove","lines":["    "]},{"start":{"row":179,"column":0},"end":{"row":179,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":169,"column":0},"end":{"row":169,"column":4},"action":"insert","lines":["    "],"id":177},{"start":{"row":170,"column":0},"end":{"row":170,"column":4},"action":"insert","lines":["    "]},{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"insert","lines":["    "]},{"start":{"row":172,"column":0},"end":{"row":172,"column":4},"action":"insert","lines":["    "]},{"start":{"row":173,"column":0},"end":{"row":173,"column":4},"action":"insert","lines":["    "]},{"start":{"row":174,"column":0},"end":{"row":174,"column":4},"action":"insert","lines":["    "]},{"start":{"row":175,"column":0},"end":{"row":175,"column":4},"action":"insert","lines":["    "]},{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"insert","lines":["    "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":4},"action":"insert","lines":["    "]},{"start":{"row":179,"column":0},"end":{"row":179,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":173,"column":4},"end":{"row":173,"column":23},"action":"remove","lines":["#Aqui es solo menor"],"id":178}],[{"start":{"row":173,"column":4},"end":{"row":174,"column":4},"action":"remove","lines":["","    "],"id":179}],[{"start":{"row":173,"column":4},"end":{"row":174,"column":0},"action":"remove","lines":["",""],"id":180}],[{"start":{"row":173,"column":4},"end":{"row":173,"column":8},"action":"remove","lines":["    "],"id":181}],[{"start":{"row":174,"column":0},"end":{"row":174,"column":4},"action":"insert","lines":["    "],"id":182},{"start":{"row":175,"column":0},"end":{"row":175,"column":4},"action":"insert","lines":["    "]},{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":177,"column":66},"end":{"row":178,"column":0},"action":"insert","lines":["",""],"id":183},{"start":{"row":178,"column":0},"end":{"row":178,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":178,"column":8},"end":{"row":179,"column":0},"action":"insert","lines":["",""],"id":184},{"start":{"row":179,"column":0},"end":{"row":179,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":179,"column":4},"end":{"row":179,"column":8},"action":"remove","lines":["    "],"id":185}],[{"start":{"row":179,"column":4},"end":{"row":225,"column":51},"action":"insert","lines":["#----------------------------------->","  #Nota:Para cada combinacion de parejas se debe usar una variable de decision llamada Aux","  #para realizar la combinacion entre las parcelas se usa la funcion combinacion_parcelas","  #----------------------------------->","","  print(model)","","  print(model.solve())","  print(pulp.LpStatus[model.status])","","  total_cosechas = 0","  tiempo_de_inicio_por_parcela = []","","  tiempo_de_inicio_por_parcela.insert(0, foo)","","  for i in range(1, k + 1):","    tiempo_de_inicio_por_parcela.append(0)","","  for variable in model.variables():","    print \"{} = {}\".format(variable.name, variable.varValue)","","    if (variable.varValue == 1) and (re.match(r'x_\\d*_\\d*_', variable.name)","                                     != None):","      nombre_variable = str(variable.name)","      nombre_variable = nombre_variable.replace('x_', '')","      nombre_variable = nombre_variable.split('_')","      i = int(nombre_variable[0])","      j = int(nombre_variable[1])","      total_cosechas += u_ij[i][j]","      tiempo_de_inicio_por_parcela[i] = j","","  #--------------------------------------------","  #Generando la salida","  salida = \"\"","  salida += str(total_cosechas)","  salida += \"\\n\"","  for i in range(1, k + 1):","    salida += str(tiempo_de_inicio_por_parcela[i]) + \" \"","","  salida += \"\\n\"","","  #Imprimiendo la salida en la terminal","  print(\"--------------------------------------->\")","  print(\"               Salida                   \")","  print(\"--------------------------------------->\")","  print(salida)","  print(\"--------------------------------------->\")"],"id":186}],[{"start":{"row":180,"column":0},"end":{"row":180,"column":2},"action":"remove","lines":["  "],"id":187},{"start":{"row":181,"column":0},"end":{"row":181,"column":2},"action":"remove","lines":["  "]},{"start":{"row":182,"column":0},"end":{"row":182,"column":2},"action":"remove","lines":["  "]}],[{"start":{"row":180,"column":0},"end":{"row":180,"column":4},"action":"insert","lines":["    "],"id":188},{"start":{"row":181,"column":0},"end":{"row":181,"column":4},"action":"insert","lines":["    "]},{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":184,"column":0},"end":{"row":184,"column":2},"action":"remove","lines":["  "],"id":189},{"start":{"row":186,"column":0},"end":{"row":186,"column":2},"action":"remove","lines":["  "]},{"start":{"row":187,"column":0},"end":{"row":187,"column":2},"action":"remove","lines":["  "]},{"start":{"row":189,"column":0},"end":{"row":189,"column":2},"action":"remove","lines":["  "]},{"start":{"row":190,"column":0},"end":{"row":190,"column":2},"action":"remove","lines":["  "]},{"start":{"row":192,"column":0},"end":{"row":192,"column":2},"action":"remove","lines":["  "]},{"start":{"row":194,"column":0},"end":{"row":194,"column":2},"action":"remove","lines":["  "]},{"start":{"row":195,"column":0},"end":{"row":195,"column":4},"action":"remove","lines":["    "]},{"start":{"row":197,"column":0},"end":{"row":197,"column":2},"action":"remove","lines":["  "]},{"start":{"row":198,"column":0},"end":{"row":198,"column":4},"action":"remove","lines":["    "]},{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"remove","lines":["    "]},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"remove","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"remove","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"remove","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"remove","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"remove","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"remove","lines":["    "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":4},"action":"remove","lines":["    "]},{"start":{"row":208,"column":0},"end":{"row":208,"column":4},"action":"remove","lines":["    "]},{"start":{"row":210,"column":0},"end":{"row":210,"column":2},"action":"remove","lines":["  "]},{"start":{"row":211,"column":0},"end":{"row":211,"column":2},"action":"remove","lines":["  "]},{"start":{"row":212,"column":0},"end":{"row":212,"column":2},"action":"remove","lines":["  "]},{"start":{"row":213,"column":0},"end":{"row":213,"column":2},"action":"remove","lines":["  "]},{"start":{"row":214,"column":0},"end":{"row":214,"column":2},"action":"remove","lines":["  "]},{"start":{"row":215,"column":0},"end":{"row":215,"column":2},"action":"remove","lines":["  "]},{"start":{"row":216,"column":0},"end":{"row":216,"column":4},"action":"remove","lines":["    "]},{"start":{"row":218,"column":0},"end":{"row":218,"column":2},"action":"remove","lines":["  "]},{"start":{"row":220,"column":0},"end":{"row":220,"column":2},"action":"remove","lines":["  "]},{"start":{"row":221,"column":0},"end":{"row":221,"column":2},"action":"remove","lines":["  "]},{"start":{"row":222,"column":0},"end":{"row":222,"column":2},"action":"remove","lines":["  "]},{"start":{"row":223,"column":0},"end":{"row":223,"column":2},"action":"remove","lines":["  "]},{"start":{"row":224,"column":0},"end":{"row":224,"column":2},"action":"remove","lines":["  "]},{"start":{"row":225,"column":0},"end":{"row":225,"column":2},"action":"remove","lines":["  "]},{"start":{"row":226,"column":0},"end":{"row":226,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":184,"column":0},"end":{"row":184,"column":4},"action":"insert","lines":["    "],"id":190},{"start":{"row":185,"column":0},"end":{"row":185,"column":4},"action":"insert","lines":["    "]},{"start":{"row":186,"column":0},"end":{"row":186,"column":4},"action":"insert","lines":["    "]},{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"insert","lines":["    "]},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"insert","lines":["    "]},{"start":{"row":189,"column":0},"end":{"row":189,"column":4},"action":"insert","lines":["    "]},{"start":{"row":190,"column":0},"end":{"row":190,"column":4},"action":"insert","lines":["    "]},{"start":{"row":191,"column":0},"end":{"row":191,"column":4},"action":"insert","lines":["    "]},{"start":{"row":192,"column":0},"end":{"row":192,"column":4},"action":"insert","lines":["    "]},{"start":{"row":193,"column":0},"end":{"row":193,"column":4},"action":"insert","lines":["    "]},{"start":{"row":194,"column":0},"end":{"row":194,"column":4},"action":"insert","lines":["    "]},{"start":{"row":195,"column":0},"end":{"row":195,"column":4},"action":"insert","lines":["    "]},{"start":{"row":196,"column":0},"end":{"row":196,"column":4},"action":"insert","lines":["    "]},{"start":{"row":197,"column":0},"end":{"row":197,"column":4},"action":"insert","lines":["    "]},{"start":{"row":198,"column":0},"end":{"row":198,"column":4},"action":"insert","lines":["    "]},{"start":{"row":199,"column":0},"end":{"row":199,"column":4},"action":"insert","lines":["    "]},{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "]},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"insert","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"insert","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"insert","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":4},"action":"insert","lines":["    "]},{"start":{"row":208,"column":0},"end":{"row":208,"column":4},"action":"insert","lines":["    "]},{"start":{"row":209,"column":0},"end":{"row":209,"column":4},"action":"insert","lines":["    "]},{"start":{"row":210,"column":0},"end":{"row":210,"column":4},"action":"insert","lines":["    "]},{"start":{"row":211,"column":0},"end":{"row":211,"column":4},"action":"insert","lines":["    "]},{"start":{"row":212,"column":0},"end":{"row":212,"column":4},"action":"insert","lines":["    "]},{"start":{"row":213,"column":0},"end":{"row":213,"column":4},"action":"insert","lines":["    "]},{"start":{"row":214,"column":0},"end":{"row":214,"column":4},"action":"insert","lines":["    "]},{"start":{"row":215,"column":0},"end":{"row":215,"column":4},"action":"insert","lines":["    "]},{"start":{"row":216,"column":0},"end":{"row":216,"column":4},"action":"insert","lines":["    "]},{"start":{"row":217,"column":0},"end":{"row":217,"column":4},"action":"insert","lines":["    "]},{"start":{"row":218,"column":0},"end":{"row":218,"column":4},"action":"insert","lines":["    "]},{"start":{"row":219,"column":0},"end":{"row":219,"column":4},"action":"insert","lines":["    "]},{"start":{"row":220,"column":0},"end":{"row":220,"column":4},"action":"insert","lines":["    "]},{"start":{"row":221,"column":0},"end":{"row":221,"column":4},"action":"insert","lines":["    "]},{"start":{"row":222,"column":0},"end":{"row":222,"column":4},"action":"insert","lines":["    "]},{"start":{"row":223,"column":0},"end":{"row":223,"column":4},"action":"insert","lines":["    "]},{"start":{"row":224,"column":0},"end":{"row":224,"column":4},"action":"insert","lines":["    "]},{"start":{"row":225,"column":0},"end":{"row":225,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":195,"column":4},"end":{"row":195,"column":8},"action":"insert","lines":["    "],"id":191}],[{"start":{"row":198,"column":4},"end":{"row":198,"column":8},"action":"insert","lines":["    "],"id":192}],[{"start":{"row":200,"column":75},"end":{"row":201,"column":0},"action":"remove","lines":["",""],"id":193}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":194}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":195}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":196}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":197}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":198}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":199}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":200}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":201}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":202}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":203}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":204}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":205}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":206}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":207}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":208}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":209}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":210}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":211}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":212}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":213}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":214}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":215}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":216}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":217}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":218}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":219}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":220}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":221}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":222}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":223}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":224}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":225}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":226}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":227}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":228}],[{"start":{"row":200,"column":75},"end":{"row":200,"column":76},"action":"remove","lines":[" "],"id":229}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"remove","lines":["    "],"id":230},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"remove","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"remove","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"remove","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"remove","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"remove","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"remove","lines":["    "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":201,"column":0},"end":{"row":201,"column":2},"action":"remove","lines":["  "],"id":231},{"start":{"row":202,"column":0},"end":{"row":202,"column":2},"action":"remove","lines":["  "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":2},"action":"remove","lines":["  "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":2},"action":"remove","lines":["  "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":2},"action":"remove","lines":["  "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":2},"action":"remove","lines":["  "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":2},"action":"remove","lines":["  "]}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "],"id":232},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"insert","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"insert","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"insert","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "],"id":233},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"insert","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"insert","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"insert","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":198,"column":64},"end":{"row":199,"column":4},"action":"remove","lines":["","    "],"id":234}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"remove","lines":["    "],"id":235},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"remove","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"remove","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"remove","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"remove","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"remove","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "],"id":236},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"insert","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"insert","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"insert","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "],"id":237},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"insert","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"insert","lines":["    "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"insert","lines":["    "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":4},"action":"insert","lines":["    "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":214,"column":4},"end":{"row":214,"column":8},"action":"insert","lines":["    "],"id":238}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["    "],"id":239}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"insert","lines":["    "],"id":240}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["#"],"id":241}],[{"start":{"row":16,"column":3},"end":{"row":16,"column":42},"action":"remove","lines":[" #input_file = open('entrada.txt', 'r')"],"id":242}],[{"start":{"row":14,"column":12},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":243}],[{"start":{"row":227,"column":49},"end":{"row":228,"column":0},"action":"insert","lines":["",""],"id":244},{"start":{"row":228,"column":0},"end":{"row":228,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":228,"column":4},"end":{"row":229,"column":0},"action":"insert","lines":["",""],"id":245},{"start":{"row":229,"column":0},"end":{"row":229,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":229,"column":4},"end":{"row":232,"column":21},"action":"insert","lines":["#Imprimiendo la salida en el archivo","  output_file = open('salida.txt', 'w')","  output_file.write(salida)","  output_file.close()"],"id":246}],[{"start":{"row":230,"column":0},"end":{"row":230,"column":2},"action":"remove","lines":["  "],"id":247},{"start":{"row":231,"column":0},"end":{"row":231,"column":2},"action":"remove","lines":["  "]},{"start":{"row":232,"column":0},"end":{"row":232,"column":2},"action":"remove","lines":["  "]}],[{"start":{"row":230,"column":0},"end":{"row":230,"column":4},"action":"insert","lines":["    "],"id":248},{"start":{"row":231,"column":0},"end":{"row":231,"column":4},"action":"insert","lines":["    "]},{"start":{"row":232,"column":0},"end":{"row":232,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":234,"column":4},"end":{"row":239,"column":49},"action":"remove","lines":["#--------------------------------------------","    #Generando la salida","    #output_file = open('static/salida.txt','w')","    #output_file.write('Hello World') ","    #output_file.close() ","    #--------------------------------------------"],"id":249}],[{"start":{"row":232,"column":23},"end":{"row":233,"column":4},"action":"remove","lines":["","    "],"id":250}],[{"start":{"row":232,"column":23},"end":{"row":233,"column":4},"action":"remove","lines":["","    "],"id":251}],[{"start":{"row":234,"column":26},"end":{"row":234,"column":27},"action":"remove","lines":["\""],"id":252}],[{"start":{"row":234,"column":25},"end":{"row":234,"column":26},"action":"remove","lines":["\""],"id":253}],[{"start":{"row":234,"column":24},"end":{"row":234,"column":25},"action":"remove","lines":["\""],"id":254}],[{"start":{"row":234,"column":23},"end":{"row":234,"column":24},"action":"remove","lines":[" "],"id":255}],[{"start":{"row":234,"column":4},"end":{"row":234,"column":5},"action":"remove","lines":["#"],"id":256}],[{"start":{"row":236,"column":4},"end":{"row":236,"column":12},"action":"remove","lines":["return 0"],"id":257}],[{"start":{"row":234,"column":22},"end":{"row":235,"column":4},"action":"remove","lines":["","    "],"id":258}],[{"start":{"row":230,"column":24},"end":{"row":230,"column":25},"action":"insert","lines":["s"],"id":259}],[{"start":{"row":230,"column":25},"end":{"row":230,"column":26},"action":"insert","lines":["t"],"id":260}],[{"start":{"row":230,"column":26},"end":{"row":230,"column":27},"action":"insert","lines":["a"],"id":261}],[{"start":{"row":230,"column":27},"end":{"row":230,"column":28},"action":"insert","lines":["t"],"id":262}],[{"start":{"row":230,"column":28},"end":{"row":230,"column":29},"action":"insert","lines":["i"],"id":263}],[{"start":{"row":230,"column":29},"end":{"row":230,"column":30},"action":"insert","lines":["c"],"id":264}],[{"start":{"row":230,"column":30},"end":{"row":230,"column":31},"action":"insert","lines":["/"],"id":265}]]},"ace":{"folds":[],"scrolltop":2940,"scrollleft":0,"selection":{"start":{"row":260,"column":0},"end":{"row":260,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1528455382199,"hash":"d9cf37cdda5f9c5507c4e6a27a266f7ca2e312ec"}