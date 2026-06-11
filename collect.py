import sys

def read_results(file):

    results = []

    with open(file) as f:

        r = {}

        for line in f:

            if line.startswith("--"):
                
                if r.get("trails"):
                    results.append(r)

                r = {}
                r["opts"] = line.removeprefix("-- Abordagem: ")
                r["trails"] = []
                r["sat"] = []

            if line.startswith("Trail:"):

                trail = list(map(int, line.split()[1:]))
                r["trails"].append(trail)
            
            if line.startswith("Cláusula"):
                
                sat = int(line.split()[2].split("/")[0])
                r["sat"].append(sat)
            
        results.append(r)

    return results

results = read_results(sys.argv[1])
gens = int(sys.argv[2])

for r in results:

    n = len(r["trails"])

    medfit = [ 0 for _ in range(gens)]

    for i in range(n):

        for gen in range(gens):

            medfit[gen] += r["trails"][i][gen]
    
    for i in range(gens):
        medfit[i] = medfit[i]/n

    medsat = sum(r["sat"])/n



    if "search" in r["opts"]:
        name="Busca Local + Mutação Alta"

    elif "--chaos" in r["opts"]:
        name="Mutação Alta"

    else:
        name="Mutação Uniforme"

    print(name,end=",")
    for x in medfit : print(f"{x:.1f}", end=",")
    print(f"{medsat:.1f}")