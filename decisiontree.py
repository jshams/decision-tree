class DecisionTree:
    def __init__(self, data, features):
        self.data = data
        self.target = [row[-1] for row in data]
        self.features = features
        self.root = None

    def find_best_split(self, rows):
        '''finds the best split of data using gini index and information gain'''
        pass

    def info_gain(self, true_rows, false_rows, uncertainty):
        '''returns the information gain of split data'''
        pass

    def gini_index(self, cat):        
        '''this can be better'''
        not_cat_not_tgt = 0
        not_cat_yes_tgt = 0
        yes_cat_not_tgt = 0
        yes_cat_yes_tgt = 0

        for cat_val, tgt in zip(cat, self.target):
            if not cat_val and not tgt:
                not_cat_not_targer += 1
            elif not cat_val and tgt:
                not_cat_yes_tgt += 1
            elif cat_val and not tgt:
                yes_cat_not_tgt += 1
            else: # yes cat_val yes tgt
                yes_cat_yes_tgt += 1

        prob_not_cat = not_cat_yes_tgt / (not_cat_not_tgt + not_cat_yes_tgt)
        prob_yes_cat = yes_cat_yes_tgt / (yes_cat_not_tgt + yes_cat_yes_tgt)
        gini_not = prob_not_cat ** 2 + (1 - prob_not_cat) ** 2
        gini_yes = prob_yes_cat ** 2 + (1 - prob_yes_cat) ** 2
        weighted_gini_index = gini_not * (not_cat_not_tgt + not_cat_yes_tgt) + gini_yes * (yes_cat_not_tgt + yes_cat_yes_tgt)

        return weighted_gini_index


    def entropy(self, cat):
        '''calculates the entropy of a column of data
        the lesser the entropy the better
        entropy = -p*log(p, 2) - q*log(q, 2)'''
        pass

class Question:
    def __init__(self, col_index, val):
        self.col_index = col_index
        self.val = val
    
    def is_numeric(self, data):
        '''indicates whether data is a number'''
        return isinstance(data (int, float))

    def satisfy(self, example):
        example_val = example[self.col_index]
        if self.is_numeric(example_val):
            return example_val >= self.val
        else:
            return example_val == self.val

class LeafNode:
    def __init__(self, predictions):
        self.predictions = predictions


class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

