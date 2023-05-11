from src.Service.LoadInput import LoadInput
from src.Service.ConversationForest import ConversationForest
from src.Service.InteractionNetwork import InteractionNetwork
from src.Service.TwoCoreReduction import TwoCoreReduction
from src.Service.SDP import SDP
import networkx as nx
import matplotlib.pyplot as plt

filePath = "/home/br/Desktop/projectPhase2/MajorProject/input/createdebate_released_no_parse.xlsx"


def showGraph(graph):
    nx.draw(graph, with_labels=True, width=[graph[u][v]['weight'] for u, v in graph.edges()])
    plt.show()


loadInput = LoadInput(filePath)
loadInput.loadDataFromAllSheets()
conversationForest = ConversationForest(loadInput)
conversationForest.buildConversationTrees()
trees = conversationForest.getAllConversationTrees()

for key in trees.keys():
    tree = trees[key]
    # tree.showConversationTree()
    iNetwork = InteractionNetwork(tree, [])
    # iNetwork.showInteractionNetwork()
    graph = TwoCoreReduction(iNetwork.graph).run2CoreReduction()
    showGraph(graph)
    sdpObj=SDP(graph)
    sdpObj.runSDP()
    break


