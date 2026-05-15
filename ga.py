import sys
import random as rand
from cnf_utils import *

def satisfied(sol, clause):

    for lit in clause:
        curr_var = var_i(lit)

        if satisfies(lit, sol[curr_var]):
            return True
        
    return False

def n_satisfied_clauses(sol, clauses):
    return sum([satisfied(sol, cl) for cl in clauses])

def populacao_inicial(n, nsol):
    return [[ True if rand.randint(0,1) else False for _ in range(n) ] for _ in range(nsol) ]

def mutacao_caotica(sol, p):
    for i in range(len(sol)):
        if rand.random() < p : sol[i] = not sol[i]

def mutacao_limitada(sol, maxmutacoes):

    if not maxmutacoes:
        return

    n = len(sol)
    nmutacoes = rand.randint(1, maxmutacoes)

    targets = rand.sample(range(n), nmutacoes)
    for t in targets:
        sol[t] = not sol[t]

def crossover_proporcional(s1, s2, f1, f2):

    p = f1 / (f1 + f2)
    if verb : print("Escolhendo s1 com ", p)

    filho = []

    for i in range(len(s1)):

        gene = s2[i]
        if rand.random() < p : gene = s1[i]
        filho.append(gene)

    if verb:
        print("P1: ", s1)
        print("P2: ", s2)
        print(f1, f2)
        print("Filho: ", filho)

    return filho


def best_breeds_all(ppl, aptidao):

    best = max(ppl, key=aptidao) ##
    ppl.pop(ppl.index(best))
    apt_best = aptidao(best)

    return [best] + list(map(lambda x : crossover_proporcional(best, x, apt_best, aptidao(x)), ppl))


def genetico(populacao, aptidao, cruzar, mutar, desenvolver, max_gens):
    
    while max_gens:

        população = cruzar(populacao)
        for idv in populacao : mutar(idv)
        for idv in populacao : desenvolver(idv)

        max_gens -= 1

    return max(população, key=aptidao)




if __name__ == "__main__":

    verb = False
    if "-v" in sys.argv or "v" in sys.argv: 
        verb = True

    nsol = 10
    maxgens = 100

    n, m, cdb = read_cnf(sys.argv[1])
    aptidao = lambda x : n_satisfied_clauses(x, cdb)
    cruzamento = lambda x : best_breeds_all(x, aptidao)
    mutacao = lambda x : mutacao_caotica(x, 0.05)

    sol = genetico(populacao_inicial(n, maxgens), aptidao, cruzamento, mutacao, lambda _ : _, 20)
    print(sol)