import sys
import random as rand

def produce_cl(n, k, p):

    rejected = True
    while rejected:

        rejected = False
        cl = []

        while len(cl) < k:
            
            lit = rand.randint(1, n)
            if rand.random() < p :
                lit = -lit

            if -lit in cl or lit in cl:

                if verb: print("Rejeitando: ", cl, "\nPor adicionar: ", lit)
                rejected = True
                break
            
            cl.append(lit)

    if verb: print("Gerando: ", cl)

    return " ".join(list(map(str, cl))) + " 0\n"

def gen_cnf(n, m, k, p, filename):
    
    with open(filename, "w") as f:

        f.write("p cnf " + str(n) + " " + str(m) + "\n")

        while m:
            f.write(produce_cl(n, k, p))
            m = m-1


if __name__ == "__main__":

    verb=False
    if "v" in sys.argv or "-v" in sys.argv: verb = True

    if len(sys.argv) < 4:
        print("Uso: gen.py filename n m k")
        if verb: print("Args: ", sys.argv)
        exit(1)


    out = sys.argv[1]
    n, m, k = list(map(int, sys.argv[2:5]))
    p = 0.5

    for s in sys.argv:
        if s.startswith("p="):
            p = float(s[2:])

    if verb: print(" N=", n, " M=", m, " K=", k, " P=", p)


    gen_cnf(n, m, k, p, out)