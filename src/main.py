
from .Service.LoadInput import  LoadInput
from  .Service.ConversationTree import ConversationTree
from .Service.ConversationForest import ConversationForest
from .Service.InteractionNetwork import InteractionNetwork

filePath=""
topic=None
loadInput=LoadInput(filePath)
loadInput.loadDataFromAllSheets()
forest=ConversationForest(loadInput)
forest.buildConversationTrees()
trees=forest.getAllConversationTrees()
interactionNetworks={}   # topicName(key) InteractionNetworkClass(value)
for topic in trees.keys():
    tree=trees[topic]
    tempInteractionNetwork=InteractionNetwork(tree)
    interactionNetworks[topic]=tempInteractionNetwork



for topic in trees.keys():
    tree=trees[topic]
    graph=interactionNetworks[topic]
    tree.showConversationTree()
    graph.showInteractionNetwork()







