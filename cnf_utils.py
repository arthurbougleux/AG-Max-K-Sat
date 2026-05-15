def satisfies(lit, val):
    return ( val and (lit > 0) ) or ( (not val) and (lit < 0) )

def var_i(lit):
    return abs(lit)-1

def read_cnf(filename):

    with open(filename, "r") as file:

        clauses = []

        for line in file:

            if line.startswith("c "):
                continue
            
            if line.startswith("p "):
                n, m = list(map(int, line.split()[2:]))
                break


        for line in file:

            if line.startswith("c "):
                continue
            
            cl = list(map(int, line.split()[:-1]))
            clauses.append(cl)

        
        if len(clauses) != m:
            print("Nº cláusulas lidas difere do informado no header")
            exit(1)
        
        return n, m, clauses