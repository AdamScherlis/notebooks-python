def count_binairo(k):
    cnt = 0
    for i in range(2**k):
        if jnp.sum(i >> jnp.arange(k) & 1) != k/2:
            continue
        trips = (i >> jnp.arange(k - 2)) & 7
        if jnp.all(trips != 0) and jnp.all(trips != 7):
            cnt += 1

    return cnt

for halfk in range(1, 10):
    print(2*halfk, count_binairo(2*halfk))
10 ** (300/700)
(3+jnp.sqrt(5))/2