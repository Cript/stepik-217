from rcviz import callgraph, viz

fib_ = [0, 1]

@viz
def fib(n):
    if n > len(fib_) - 1:
        fib_.append(fib(n-2) + fib(n-1))

    return fib_[n]

print(fib(10))

callgraph.render('fib_1_2.png')