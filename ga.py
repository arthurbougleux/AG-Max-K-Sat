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


def best_breeds_all():
    pass




def genetico(populacao, adequação, cruzar, mutar, desenvolver, max_gens):
    
    while max_gens:

        população = cruzar(populacao)
        for idv in populacao : mutar(idv)
        for idv in populacao : desenvolver(idv)

        max_gens -= 1

    return max(população, key=adequação)

l = populacao_inicial(5, 5)
print(l)
for owo in l: mutacao_limitada(owo, 1)
print(l)