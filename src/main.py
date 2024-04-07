from src.Service.LoadInput import LoadInput
from src.Service.ConversationForest import ConversationForest
from src.Service.InteractionNetwork import InteractionNetwork
from src.Service.TwoCoreReduction import TwoCoreReduction
from src.Service.SDP import SDP
import networkx as nx
import matplotlib.pyplot as plt



filePath = "../input/createdebate_released_no_parse.xlsx"



def showGraph(graph, bestCut,topic):
    pos = nx.spring_layout(graph, seed=3113794652)
    users = sorted(list(graph.nodes))
    postiveStance = []
    negativeStance = []
    for user in bestCut.cut:
        value=user.stance
        key=user.userId
        if value < float(0):
            negativeStance.append(key)
        else:
            postiveStance.append(key)

    usersLabels = {}
    for i in range(len(users)):
        usersLabels[users[i]] = users[i]
    options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
    nx.draw_networkx_nodes(graph, pos, nodelist=negativeStance, node_color="tab:blue", **options)
    nx.draw_networkx_nodes(graph, pos, nodelist=postiveStance, node_color="tab:green", **options)
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, usersLabels, font_size=11, font_color="black")
    plt.title(topic)
    plt.tight_layout()
    plt.axis("off")
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
    graphAfter2CoreReduction = TwoCoreReduction(iNetwork.graph).run2CoreReduction()
    try:
        activeUsers = sorted(graphAfter2CoreReduction.nodes)
        sdpObj = SDP(graphAfter2CoreReduction)
        sdpObj.runSDP()
        bestCut = sdpObj.getBestCut()
        showGraph(graphAfter2CoreReduction, bestCut,tree.discussionTitle)
    except Exception as e:
        print("error occured : ", e)
