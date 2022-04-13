from collections import defaultdict


def solution(genres, plays):
    answer = []
    iters = sorted([(-n, gp[0], gp[1])
                   for n, gp in enumerate(zip(genres, plays))], key=lambda x: (x[-1], x[0]))
    G = defaultdict(list)
    genre_sum = defaultdict(int)
    for n, g, p in iters:
        G[g].append((p, n))
        genre_sum[g] += p
    for g, s in sorted(genre_sum.items(), key=lambda x: x[1], reverse=True):
        n = 0
        while n < 2 and len(G[g]):
            p_ind, n_ind = G[g].pop()
            answer.append(-n_ind)
            n += 1
    return answer

genres, plays = ["classic", "pop", "classic","classic", "pop"], [500, 600, 800, 800, 2500]
