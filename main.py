import argparse
from ga import *


parser = argparse.ArgumentParser(description="Aplica um algoritmo genético a uma instância de MAXSAT em formato cnf")
parser.add_argument('filename', help='Input file')
parser.add_argument('population', help='Número de indivíduos na população')
parser.add_argument('generations', help='Número máximo de gerações')
parser.add_argument('--uniforme', action='store', default=1, help='Probabilidade de uma cruzamento uniforme ser aplicado na geração. Ajuda a evitar convergências precoces e evita processamento de aptidao', metavar='p', type=float)
parser.add_argument('--chaos', action='store', help='Mutações invertem bits quaisquer da solução com probabilidade p', metavar='p', type=float)
parser.add_argument('--order', action='store', help='Mutações sempre invertem k variávels na solução', metavar='n', type=int)
parser.add_argument('--search', action='store', help='Aplica uma busca local a cada geração', metavar='reckless/cautious')
parser.add_argument('--steps', action='store', help='Número de passos feitos pela busca local a cada geração (default: até encontrar um mínimo local)', metavar='k', type=int, default=math.inf)
parser.add_argument('-v', '--verbose', action='count', default=0)
args = parser.parse_args()

nsol = int(args.population)
max_gens = int(args.generations)
n, m, cdb = read_cnf(args.filename)



aptidao = lambda x : n_satisfied_clauses(x, cdb)

mutacao = lambda x : mutacao_caotica(x, 0.05)
cruzamento = lambda x, y : best_breeds_all(x, aptidao, y)

if args.search:
    if args.search == 'reckless':
        escolha = lambda x : reckless_choice(x, cdb)
    elif args.search == 'cautious':
        escolha = lambda x : cautious_choice(x, cdb)
    else:
       print("Método de busca desconhecido")
       exit(1)

    desenvolvimento = lambda x : running_up_that_hill(x, escolha, aptidao, args.steps)
else:
    desenvolvimento = lambda x : x


sol = genetico(populacao_inicial(n, nsol), aptidao, cruzamento, mutacao, desenvolvimento, max_gens, args.uniforme)
apt = aptidao(sol)

if args.verbose > 1: 
   print("Solução:")
   for i in range(len(sol)): 
     print(f"x{i} = {sol[i]}")

if args.verbose:
   for v in sol : print(v, end=' ')
   print()


print(f"Cláusulas satisfeitas: {apt}/{m} ({apt/m:.1%})")