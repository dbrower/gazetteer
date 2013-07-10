#!/usr/bin/env python

import fiona
import shapely
import shapely.ops 
import shapely.geometry
import pprint


def each_level(place, prefix):
    prop = place['properties']
    try:
        level = 0
        while True:
            yield prop['%s_%d' % (prefix, level)]
            level += 1
    except:
        pass

def get_all_levels(place, prefix):
    return [x for x in each_level(place, prefix)]

def tree_number(place):
    return ".".join(map(str, get_all_levels(place, "ID")))

def is_morespecific(tree_a, tree_b):
    return tree_b.startswith(tree_a)

# return
# 0 if same
# 1 if tree_b is morespecific than tree_a
# -1 if tree_a is morespecific than tree_b
# 2 if non-compariable
def compare_pair(tree_a, tree_b):
    if tree_a == tree_b:
        return 0
    if is_morespecific(tree_a, tree_b):
        return 1
    elif is_morespecific(tree_b, tree_a):
        return -1
    else:
        return 2

def remove_morespecifics(ts):
    result = []
    for t in ts:
        c = [compare_pair(r, t) for r in result]
        if 0 in c or 1 in c:
            pass
        elif -1 in c:
            del result[c.index(-1)]
        else:
            result.append(t)
    return result

def place_name(place):
    result = "(unknown)"
    for n in each_level(place, "NAME"):
        result = n
    return result

places = []
for i in [0,1,2,3,4,5]:
    with fiona.open("shapefiles/KEN_adm%d.shp" % i) as c:
        for place in c:
            places.append(place)

places_by_name = {}
for p in places:
    n = place_name(p)
    try:
        places_by_name[n].append(p)
    except KeyError:
        places_by_name[n] = [p]

tree_numbers = {}

for n,ps in places_by_name.items():
    tnr = map(tree_number, ps)
    if len(tnr) > 1:
        tnr = remove_morespecifics(tnr)
    tree_numbers[n] = (tnr, shapely.ops.cascaded_union([shapely.geometry.shape(p['geometry']) for p in ps]))

for n,(ps,shp) in tree_numbers.items():
    print n,ps,str(shp.centroid)

