# O * na definição do parâmetro faz com que ele aceite mais de um elemento para um único parâmetro
def contador(*parametro):
    tam = len(parametro)
    print("Recebi o parâmetro {} e ele possui {} elementos.".format(parametro,tam))

contador(1,2,3,4)