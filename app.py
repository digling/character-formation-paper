from lingpy import *
from sinopy import *
from collections import defaultdict
import networkx as nx
from classify import *
from tabulate import tabulate


def load_data(path):

    data = csv2list(path, strip_lines=False)
    return {line[0]: dict(zip([h.lower() for h in data[0]], line)) for line in
            data[1:]}

# make a network of all series
def make_graph(data):
    G = nx.DiGraph()
    for char, vals in data.items():
        if vals['xiesheng'] and vals['xiesheng'] != '?':
            if vals['xiesheng'] in G:
                G.node[vals['xiesheng']]['frequency'] += 1
            else:
                G.add_node(vals['xiesheng'], series=vals['karlgren'],
                        frequency=1)

            if char in G:
                G.node[char]['frequency'] += 1
            else:
                G.add_node(char, series=vals['karlgren'], frequency=1)

            if char in G[vals['xiesheng']]:
                G[vals['xiesheng']]['frequency'] += 1
            else:
                G.add_edge(vals['xiesheng'], char, frequency=1)
    return G


if __name__ == '__main__':
    from sys import argv
    
    if 'sandeng' in argv:
        condition1 = sandeng
        condition2 = lambda x: False if sandeng(x) else True
        cname = 'sandeng'
        header = ['GROUP', 'MCH',  'B', 'A', 'none', 'MIXED']
        condition = lambda x: '1' in x and '2' in x

    if 'uvulars' in argv:
        condition1 = velars
        condition2 = glottals
        cname = 'uvulars'
        header = ['group', 'mch', 'velars', 'glottals', 'none', 'mixed']
        condition = lambda x: '1' in x or '2' in x

    if 'kl' in argv:
        condition1 = velars
        condition2 = lateral
        cname = 'kl'
        header = ['group', 'mch', 'velars', 'laterals', 'none', 'mixed']

    if 'qu' in argv:
        condition1 = qutone
        condition2 = lambda x: False if qutone(x) else True
        cname = 'qu'
        header = ['group', 'mch', 'qu-tone', 'other', 'none', 'mixed']
        condition = lambda x: '1' in x and '2' in x

    if 'pt' in argv:
        condition1 = tcoda
        condition2 = pcoda
        cname = 'pt'
        header = ['group', 'mch', 't-coda', 'p-coda', 'other', 'mixed']
        condition = lambda x: '1' in x and '2' in x

    data = load_data('data/data.tsv')
    G = make_graph(data)
    D = defaultdict(lambda : defaultdict(list))
    text = '<html><head><meta charset="utf-8"/><style>td {border: 1pt solid black};</style> </head><body>'



    # make initial test with the data to share it
    found = 1

    # get karlgren nodes
    karlgren = sorted(set(v['karlgren'] for v in data.values()))

    # iterate over all karlgren items
    for group in karlgren:
        # assemble xiesheng series
        chars = [(x['character'], x['mch'], x['xiesheng']) for x in \
                        data.values() if x['karlgren'] == group and x['xiesheng'].strip('?')
                        ]
        for char, mch, xiesheng in chars:
            D[group][xiesheng] += [(char, mch)]

        if chars:
            is_condition = []
            for char, mch, xiesheng in chars:
                if condition1(mch):
                    is_condition += ['1']
                elif condition2(mch):
                    is_condition += ['2']
                else:
                    is_condition += ['0']

            table = []
            for xiesheng in D[group].keys():
                row = [xiesheng, data.get(char, {"mch": ''})['mch'], [], [], [], '']
                for char, mch in D[group][xiesheng]:
                    if condition1(mch):
                        row[2] += [char]
                    elif condition2(mch):
                        row[3] += [char]
                    else:
                        row[4] += [char]

                if row[2] and not row[3]:
                    row[5] = '++'
                if row[3] and not row[2]:
                    row[5] = '--'
                row[2] = ' '.join(row[2])
                row[3] = ' '.join(row[3])
                row[4] = ' '.join(row[4])

                table += [row]

            if condition(is_condition):
                if '--verbose' in argv or '-v' in argv:
                    print(group)
                    print('')
                    print(tabulate(table, headers=header))
                    print('')
                if len(D[group]) > 1:
                    text += '<p>'+'('+str(found)+') '
                    text += group+' [{0}]'.format(len(D[group]))+'</br>'
                    text += tabulate(table, headers=header,
                            tablefmt='html').replace(
                                    '<td>', 
                                    '<td style="width:70px; border: 1px solid black">'
                                    ).replace(
                                            '<table>',
                                            '<table style="width:500px;">'
                                            )
                    text += '</p>'
                    found += 1
    with open('output/'+cname+'.html', 'w') as f:
        f.write(text+'</body></html>')


            
