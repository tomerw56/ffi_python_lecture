from time import time
def time_function(title, function,**kwargs):
    start = time()
    for i in range(1_000):
        function(**kwargs)
    elapsed = (time() - start) / 1_000
    print(f"Time per call, {title}: {elapsed * 1000:.2} ms")

