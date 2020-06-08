#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# Função DEF 03
# BATALHA NAVAL - 

def main():
   mapa = posicaoNavios()
   pontos = 0
   total = totalpontos(mapa)
   chances = 0
   print("-"*60)
   print("BATALHA NAVAL - 5x5\n(1 navio de 1x1 e 1 navio 1x2)")
   print("Você tem que fazer %d pontos."%total)
   print("Digite as coordenadas separadas por vírgula,\npor exemplo: (3,4) ")
   print("Você tem 5 chances...")
   print("-"*60)
   while chances < 5:
       x, y = input("Digite a coordenada do tiro: ").split(',')
       x, y = int(x), int(y)
       chances +=1
       print("Você atirou em (%d,%d)."%(x,y))
       if (x,y) in mapa and mapa[x,y] > 0:
           valor = mapa[x,y]
           print("BOOOOM... você acertou um navio: +%d pontos."%valor)
           print("-" * 25)
           pontos += valor
           mapa[x,y] = 0
       else:
           print("Água..")
           print("-"*25)
   print("-" * 25)
   print("PONTUAÇÃO FINAL: %d pontos."%pontos)
   if pontos == 160:
       print("YOU WIN..")
   else:
       print("YOU LOOSE..")
 
def totalpontos(dic):
   soma = 0
   for i in dic:
       soma += dic[i]
   return soma
 
def posicaoNavios():
   return {(3,1):100, (4,3):30, (4,4):30}
 
main()
