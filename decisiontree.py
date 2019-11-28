class DecisionTree(object):
    def __init__(self, data=None, target=None):
        self.data = data
        self.target = target

    def gini_index(self, cat):        
        
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