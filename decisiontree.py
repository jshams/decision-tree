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
        p = len(true_rows) / (len(false_rows) + len(true_rows))
        left_gini = self.gini_index(true_rows)
        right_gini = self.gini_index(false_rows)
        return uncertainty - p * left_gini - (1 - p) * right_gini

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

    def partition(self, rows, question):
        true_rows, false_rows = [], []
        for row in rows:
            if question.satisfy(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows


class Question:
    def __init__(self, col_index, val, col_name):
        self.col_index = col_index
        self.val = val
        self.col_name = col_name
    
    def is_numeric(self, data):
        '''indicates whether data is a number'''
        return isinstance(data (int, float))

    def satisfy(self, example):
        example_val = example[self.col_index]
        if self.is_numeric(example_val):
            return example_val >= self.val
        else:
            return example_val == self.val
    
    def __repr__(self):
        condition = '>='
        if not self.is_numeric(self.val):
            condition = 'equal to'
        return f'Is {self.col_name} {condition} {self.val}?'

class LeafNode:
    def __init__(self, predictions):
        self.predictions = predictions


class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

