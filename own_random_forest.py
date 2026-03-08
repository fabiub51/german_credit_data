import numpy as np

class Node: 
    def __init__(self, feature_index, threshold, left, right, value):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self):
        pass 

    def _gini(y):
        return 1 - np.sum(np.pi**2)

    def _best_split(X,y):
        """find optimal feature and treshold: 
        - loops over all features 
        - computes weighted Gini of left/right splits
        - returns split with lowest weighted Gini 
        MODIFY: sample max features, consider random sub-sample 
        """
        pass

    def _build(X,y,depth): 
        """
        grows a tree recursively: 
            - if stopping criteria are met, return a leaf (max depth, min samples, pure node)
            - otherwise find best split and recurse on left/right subsets
        """
        pass

    def _bootstrap(X,y):
        """ Draw n samples with replacement, return sampled X and y"""
        pass

    def fit(X,y):
        """Kick off _build from the root"""
        pass

    def predict(X): 
        """Traverse the tree for each sample to reach a leaf value"""
        pass
        