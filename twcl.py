#!/usr/bin/python
# -*- coding: utf-8 -*-

import igraph


def clustering(file, size=200):
    users, friends = [], {}
    for line in file:
        line = line.strip().split()
        users.append(line[0])
        friends[line[0]] = set(line[1:])
    user2id = dict((u,i) for (i,u) in enumerate(users))
    edges = []
    for i, u in enumerate(users):
        for f in friends[u]:
            if f not in friends:
                continue
            fi = user2id[f]
            if i < fi and u in friends.get(f, set()):
                edges.append((i, fi))
    G = igraph.Graph(edges)
    G.vs['label'] = users
    # igraph.plot(G.community_fastgreedy())
    C = G.community_fastgreedy().as_clustering(size)
    cluster = []
    for i in range(len(C)):
        l = len(C.subgraph(i).vs['label'])
        if l > 3:
            cluster.append(set(C.subgraph(i).vs['label']))
    return cluster


if __name__ == '__main__':
    import sys
    cluster = clustering(sys.stdin)
    for i, c in enumerate(cluster):
        print "cluster %d: %s" % (i, ', '.join(c))
