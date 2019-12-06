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

class DecisionTree:
    def __init__(self, data, features):
        self.data = data
        self.target = [row[-1] for row in data]
        self.features = features
        self.root = self.build_tree(self.data)

    def build_tree(self, rows, parent=None):
        gain, best_question = self.find_best_split(rows)
        if gain == 0:
            return LeafNode(self.label_counts(rows))
        true_rows, false_rows = self.partition(rows, best_question)
        true_branch = self.build_tree(true_rows)
        false_branch = self.build_tree(false_rows)
        return DecisionNode(best_question, true_branch, false_branch)

    def traverse_dfs(self, visit,node=None, depth=0):
        if node is None:
            node = self.root
        visit(node, depth)
        # print(node)
        if not isinstance(node, LeafNode):
            # visit(node.true_branch, depth)
            self.traverse_dfs(visit, node.true_branch, depth + 1)
            # visit(node.false_branch, depth)
            self.traverse_dfs(visit, node.false_branch, depth + 1)

    def find_best_split(self, rows):
        '''finds the best split of data using gini index and information gain'''
        max_gain = 0
        best_question = None

        current_uncertainty = self.gini_index(rows)

        for col_index in range(len(rows[0]) - 1):
            values = set([row[col_index] for row in rows])
            
            for val in values:
                q = Question(col_index, val, self.features[col_index])
                true_rows, false_rows = self.partition(rows, q)
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue
                else:
                    gain = self.info_gain(true_rows, false_rows, current_uncertainty)
                if gain >= max_gain:
                    max_gain = gain
                    best_question = q

        return max_gain, best_question

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

    def classify(self, row, node=None):
        if node == None:
            node = self.root
        if isinstance(node, LeafNode):
            return node.probabilities
        if node.question.satisfy(row):
            return self.classify(row, node.true_branch)
        else:
            return self.classify(row, node.false_branch)


