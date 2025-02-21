import networkx as nx
import json
from my_utils.utils import resource_path


class RelatedWords:
    SYNONYMS_GRAPH = None
    RELATIONS_GRAPH = None
    eng_to_arb = None
    arb_to_eng = None
    initialized = False
    def __init__(self):
        if not RelatedWords.initialized:
            RelatedWords.SYNONYMS_GRAPH = nx.node_link_graph(json.load(open(resource_path("data/synonyms_graph.json"))), edges='links')
            RelatedWords.RELATIONS_GRAPH = nx.node_link_graph(json.load(open(resource_path("data/relations_graph.json"))), edges='links')
            RelatedWords.eng_to_arb = json.load(open(resource_path('data/eng_to_arb.json')))
            RelatedWords.arb_to_eng = json.load(open(resource_path('data/arb_to_eng.json')))
            RelatedWords.initialized = True

    def get_by_distance(self, query, cutoff):
        if not RelatedWords.initialized:
            raise ReferenceError("Please initialize the class")
        # related_ar = set()
        words_bases_eng = set()
        paths = {}
        for component in nx.connected_components(RelatedWords.SYNONYMS_GRAPH):
            subgraph = RelatedWords.SYNONYMS_GRAPH.subgraph(component)
            for node in subgraph.nodes:
                if query in node:
                    # related_ar.update(subgraph.nodes)
                    # paths[node] = [RelatedWords.arb_to_eng[node]]
                    paths[node] = [node]
                    centers = [RelatedWords.SYNONYMS_GRAPH.nodes[c]['concept_id'] for c in
                               nx.center(RelatedWords.SYNONYMS_GRAPH.subgraph(nx.node_connected_component(RelatedWords.SYNONYMS_GRAPH, node))) if
                               RelatedWords.SYNONYMS_GRAPH.nodes[c].get('concept_id')]
                    words_bases_eng.update(centers)
                    break
        for word_base_eng in words_bases_eng:
            for node, path in nx.single_source_shortest_path(RelatedWords.RELATIONS_GRAPH, word_base_eng, cutoff=cutoff).items():
                if not RelatedWords.RELATIONS_GRAPH.nodes[node].get('info') in ['category', 'root']:
                    synonyms = nx.node_connected_component(RelatedWords.SYNONYMS_GRAPH, RelatedWords.eng_to_arb[node])
                    # related_ar.update(synonyms)
                    for synonym in synonyms:
                        if len(path) == 1and RelatedWords.eng_to_arb[path[0]] != synonym:
                            paths[synonym] = [RelatedWords.eng_to_arb[path[0]]] + [synonym]
                        else:
                            paths[synonym] = [RelatedWords.eng_to_arb[n] for n in path[:-1]] + [synonym]
        # return related_ar, paths
        return paths
