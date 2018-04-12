from enum import Enum
import sys


class GlueType(Enum):
    """Enumerates the possible strategies
    that could be used to glue two chains of vertices."""
    HH = 0
    HT = 1
    TH = 2
    TT = 3


def dist(a, b):
    """Gets the distance between two points."""
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5


def shortest_distance(xs, ys):
    """Gets the shortest distance between two chains of vertices
    and a glue strategy to be used during the concatenation."""
    xh, xt = xs[0], xs[-1]
    yh, yt = ys[0], ys[-1]

    hh = dist(xh, yh)
    ht = dist(xh, yt)
    th = dist(xt, yh)
    tt = dist(xt, yt)

    md, gt = min(hh, ht, th, tt), None
    if hh == md:
        gt = GlueType.HH
    elif ht == md:
        gt = GlueType.HT
    elif th == md:
        gt = GlueType.TH
    else:
        gt = GlueType.TT
    return(md, gt)


def shortest_glue(xs, ys, gt):
    """Glues two chains of vertices based on the glue strategy."""
    if gt == GlueType.HH:
        return(list(reversed(xs)) + ys)
    elif gt == GlueType.HT:
        return(ys + xs)
    elif gt == GlueType.TH:
        return(xs + ys)
    else:
        return(xs + list(reversed(ys)))


def closest_pair(xs):
    """Builds the TSP path using the closest pair heuristic."""
    xss = xs[:]
    for i in range(len(xss)):
        xss[i] = [xss[i]]

    while len(xss) > 1:
        ir, jr, gt, md = None, None, None, sys.maxsize
        for i in range(len(xss)-1):
            for j in range(i+1, len(xss)):
                sd, gs = shortest_distance(xss[i], xss[j])
                if sd < md:
                    ir, jr, gt, md = xss[i], xss[j], gs, sd

        xss.remove(ir)
        xss.remove(jr)
        xss.append(shortest_glue(ir, jr, gt))

    return(xss[0])


the_ex = [(0, 0),
          (0, 1),
          (0, -1),
          (0, 3),
          (0, -5),
          (0, 11),
          (0, -21),
          (0, 56),
          (0, -97)]
