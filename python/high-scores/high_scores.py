import collections ,heapq
class HighScores(object):
    def __init__(self, scores):
        if scores is None:
            raise ValueError("Empty scores passed")
        
        if not isinstance(scores,collections.abc.Sequence):
            raise ValueError("score is not valid sequence")
        self.scores = scores

    def latest(self):
        return self.scores[-1]
    
    def personal_best(self):
        return max(self.scores)
    
    def personal_top(self):
        n_largest = len(self.scores) if len(self.scores) < 3 else 3
        return heapq.nlargest(n_largest, self.scores)
    
    def report(self):
        latest,best =self.latest(),self.personal_best()
        if latest == best :
            message = "Your latest score was {0}. That's your personal best!".format(latest)
        else:
            message = "Your latest score was {0}. That's {1} short of your personal best!".format(latest,best-latest)
        return message