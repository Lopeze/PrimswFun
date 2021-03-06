import timeit
import random
# my modules
import graphgen
import io_utils
import primbasic
import primbad
import primthreaded
'''
This is the code to benchmark both graphs of density = 1.25, 1.5, 1.75, and 2.0
The graphs are created using the erdos-renyi model

You will have to change the density parameter and size paramter to change how 
many edges in the graph there will and how many vertices you want. What is below
is just an example of density = 1.25 and size of graph in terms of vertices 
maxing out at 2000 vertices.
'''


'''
This is the code to generate graphs based on the erdos-renyi model of a graph
denseness of the input "density" parameter
'''
size = 0
t = 0
density = 1.25 # the density of our graph (#(V^density) edges)
iters = 100

with open("primsbad.txt", "a") as myfile:
    myfile.write("[")
with open("prims.txt", "a") as myfile:
    myfile.write("[")
with open("primsthread.txt", "a") as myfile:
    myfile.write("[")
with open("primsizes.txt", "a") as myfile:
    myfile.write("[")

while size <= 2000:
    size += 100
    V, E = graphgen.erdos_connected(size, density)
    weights = graphgen.createweights(E)
    adjlist = graphgen.createadj(V, E)
    
    # my naive prims
    t = timeit.timeit(stmt = "primsbad(V, E, weights)".format(V, E, weights),
                       setup = "from primbad import primsbad; from __main__ import V, E, weights", number = iters)
    t = t / iters
    print("badprims:",t)
    with open("primsbad.txt", "a") as myfile:
        myfile.write(str(t) + ',')
    
    # regular prims
    t = timeit.timeit(stmt = "prims(V, E, weights, adjlist)".format(V, E, 
                                                                    weights, 
                                                                    adjlist),
                       setup = "from primbasic import prims; from __main__ import V, E, weights, adjlist", number = iters)
    t = t / iters
    print("reg",t)
    with open("prims.txt", "a") as myfile:
        myfile.write(str(t) + ',')
    
    # prims multithreaded
    t = timeit.timeit(stmt = "primsthread(V, E, weights, adjlist, 2)".format(V,
                                                                              E, weights, adjlist, 2), setup = "from primthreaded import primsthread; from __main__ import V, E, weights, adjlist", number = iters)
    t = t / iters
    print("thread",t)
    with open("primsthread.txt", "a") as myfile:
        myfile.write(str(t) + ',')
    
    with open("primsizes.txt", "a") as myfile:
        myfile.write(size)

with open("primsbad.txt", "a") as myfile:
    myfile.write("]")
with open("prims.txt", "a") as myfile:
    myfile.write("]")
with open("primsthread.txt", "a") as myfile:
    myfile.write("]")
with open("primsizes.txt", "a") as myfile:
    myfile.write("]")  
