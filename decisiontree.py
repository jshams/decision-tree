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

    def gini_index(self, rows):        
        '''this can be better'''
        counts = self.label_counts(rows)
        impurity = 1
        for count in counts.values():
            p_label = count / len(rows)
            impurity -= p_label**2
        return impurity
    
    def label_counts(self, rows):
        label_hist = {}
        for row in rows:
            label = row[-1]
            if label not in label_hist:
                label_hist[label] = 1
            else:
                label_hist[label] += 1
        return label_hist


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

