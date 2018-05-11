import networkx as nx
import matplotlib.pyplot as plt


def chain_glue(db, rf_chain, rf_signal):
    for key in rf_chain:
        rf_signal.apply_gain(db[key]['G'])
        rf_signal.convert_frequency(local_oscillator_freq=db[key]['LO'])
        rf_signal.append_trace(source=key)


db = {
    'LNA1': {'G': 41, 'LO': 0},
    'filter2': {'G': -10, 'LO': 0},
    'CNV3': {'G': 30, 'LO': -200},
    'SWC1': {'G': -5, 'LO': 0},
    'CNV2': {'G': -10, 'LO': -150},
    'SWC2': {'G': -3, 'LO': -200}
}


G = nx.Graph()
# G.add_edge('LNA1', 'filter2')
# G.add_edge('filter2', 'CNV3')
# G.add_edge('CNV3', 'SWC1')
# G.add_edge('SWC1', 'CNV2')
# G.add_edge('SWC1', 'SWC2')
# G.add_edge('SWC2', 'CNV2')
G.add_edge('WSC1/3', 'WSC1/2')
G.add_edge('WSC1/4', 'WSC1/1')
G.add_edge('WSC2/1', 'WSC2/2')
G.add_edge('WSC2/4', 'WSC2/3')
G.add_edge('WSC3/1', 'WSC3/2')
G.add_edge('WSC3/4', 'WSC3/3')
G.add_edge('WSC4/1', 'WSC4/2')
G.add_edge('WSC4/4', 'WSC4/3')

G.add_edge('WSC1/3', 'WSC1/4')
G.add_edge('WSC1/2', 'WSC1/1')
G.add_edge('WSC2/2', 'WSC2/3')
G.add_edge('WSC2/1', 'WSC2/4')
G.add_edge('WSC3/2', 'WSC3/3')
G.add_edge('WSC3/1', 'WSC3/4')
G.add_edge('WSC4/2', 'WSC4/3')
G.add_edge('WSC4/1', 'WSC4/4')

G.add_edge('WLNA2/1','WLNA2/2')
G.add_edge('WLNA1/1','WLNA1/2')
G.add_edge('WCNV1/1','WCNV1/2')
G.add_edge('WCNV2/1','WCNV2/2')
G.add_edge('WCNV3/1','WCNV3/2')
G.add_edge('WCNV4/1','WCNV4/2')
G.add_edge('VT1/1','VT1/2')
G.add_edge('VT1/3','VT1/2')




G.add_edge('WSC1/3','WLNA2/2', weight=100)
G.add_edge('WSC1/2','WCNV4/1', weight=50)
G.add_edge('WSC2/3','WLNA1/2', weight=2)
G.add_edge('WSC2/2','WCNV3/1', weight=5)
G.add_edge('WSC2/4','WCNV1/1', weight=2)
G.add_edge('WSC1/1','WSC2/1', weight=6)
G.add_edge('WSC1/4','WCNV2/1', weight=2)
G.add_edge('WCNV4/2','WSC3/2', weight=7)
G.add_edge('WSC3/1','VT1/3', weight=1)
G.add_edge('WSC4/1','VT1/1', weight=9)
G.add_edge('WSC4/4','WCNV1/2', weight=5)
G.add_edge('WSC4/2','WCNV3/2', weight=2)
G.add_edge('WCNV2/2','WSC3/4', weight=1)
G.add_edge('WSC3/3','WSC4/3', weight=4)
G.add_edge('VT1/3', 'out', weight=2)

ans = nx.all_simple_paths(G, 'WLNA1/1', 'out')
print(list(ans))

pos = nx.spring_layout(G, k=3, pos=None, fixed=None, iterations=50, weight='weight',
                       scale=10, center=None, dim=2)
nx.draw(G, with_labels=True, font_size=4, pos=pos)
plt.show()
