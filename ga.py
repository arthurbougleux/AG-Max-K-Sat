import sys
import math
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
    nmutacoes = rand.randint(0, maxmutacoes)

    targets = rand.sample(range(n), nmutacoes)
    for t in targets:
        sol[t] = not sol[t]

def crossover_proporcional(s1, s2, p):

    filho = []
    #print(p(1,2))

    for i in range(len(s1)):

        if rand.random() < p : gene = s1[i]
        else : gene = s2[i]

        filho.append(gene)

    return filho

def best_breeds_all(ppl, aptidao, calc_p):
    
    best = max(ppl, key=aptidao) ##
    apt_best = aptidao(best)

    return apt_best, best, list(map(lambda x : crossover_proporcional(best, x, calc_p(best, x)) if x != best else x, ppl))

def reckless_choice(sol, clauses):

    n = len(sol)
    score = [ 0 for _ in range(n) ]

    for cl in clauses:

        if not satisfied(sol, cl):
            for lit in cl: score[var_i(lit)] += 1

    return score.index(max(score))

def cautious_choice(sol, clauses):

    n = len(sol)
    score = [ 0 for _ in range(n) ]

    for cl in clauses:

        satlits = []

        for lit in cl:
            if satisfies(lit, sol[var_i(lit)]): satlits.append(lit)


        if len(satlits) == 0:
            for lit in cl: score[var_i(lit)] += 1
        
        if len(satlits) > 0:
            for lit in satlits: score[var_i(lit)] -= 1


    return score.index(max(score))

def running_up_that_hill(sol, choice, aptidao, steps=math.inf):

    old_apt = chosen_i = -1
    apt = aptidao(sol)

    while old_apt < apt and steps:

        chosen_i = choice(sol)
        sol[chosen_i] = not sol[chosen_i]

        old_apt = apt
        apt = aptidao(sol)
        
    if old_apt > apt:
        sol[chosen_i] = not sol[chosen_i]   

def proporcao(x,y):
    return x / (x+y)

def genetico(populacao, aptidao, cruzar, mutar, desenvolver, max_gens, p_uniforme):

    trail = []

    while max_gens:
        
        proporcao_genes = (lambda _, __ : 0.5) if rand.random() < p_uniforme else (lambda x, y : proporcao(aptidao(x), aptidao(y)))

        apt_best, best, população = cruzar(populacao, proporcao_genes)
        for idv in populacao : 
            if idv != best : mutar(idv)
        for idv in populacao : desenvolver(idv)

        max_gens -= 1
        trail.append(apt_best)

    return max(população, key=aptidao), trail