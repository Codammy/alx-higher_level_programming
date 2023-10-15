#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    bestScoreIndex = 0
    bestScore = 0
    for k, v in a_dictionary.items():
        if v > bestScore:
            bestScore = v
            bestScoreIndex = k
    return bestScoreIndex
