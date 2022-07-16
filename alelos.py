import scipy

def build_population (N, p):
    population = []
    for i in range (N):
        alelo1 = "A"
        if scipy.ramdom.rand() > p:
            alelo1= "a"
        alelo2 = "A"
        if scipy.random.rand () > p:
            alelo2 = "a"
        population.append ((alelo1, alelo2))
    return population

def compute_frequencies (population) :
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

def reproduce_population(population):
    new_generation = []
    N = len(population)
    for i in range(N):
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        new_generation.append(offspring)
    return new_generation
            
                      
                 