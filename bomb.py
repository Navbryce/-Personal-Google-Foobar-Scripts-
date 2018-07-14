import math
def acceptable_mod(big, small):
    """mods two numbers. returns number of steps and result on the big number"""
    mod = big % small
    resulting_value = mod if mod != 0 else small
    number_of_steps = (big - mod)/small
    if mod == 0:
        number_of_steps -= 1 # if the mod == 0, then we want to the result to be just the small number (presumably the small number is 1 or its impossible). thus, the number of steps is - 1 because we didn't mod all the way down
    return {
        "result": resulting_value,
        "number_of_steps": number_of_steps
    }

def format_answer (answer_string):
    period = answer_string.find(".")
    return answer_string if period < 0 else answer_string[0:period]

def answer(M, F):
    """
    M and F are target ints. You start out with a set of numbers (1, 1) and have to get to (M, F) via (M+F, F) or (M, F+M)
    with the minimum number of additions
    returns a string version of the number of steps
    returns "impossible" if impossible
    """
    step_counter = long(0)
    not_possible = False
    M = long(M)
    F = long(F)
    while (M != 1 or F != 1) and not not_possible: # the smaller number must have been what was added just because (any muber > 1) + number > number. So the smaller number must have always been aded
        if M > F and F >= 1:
            result = acceptable_mod(M, F)  # remove F as many times as possible. a negative number can never happen
            step_counter += result["number_of_steps"]
            M = result["result"]
        elif M < F and M >= 1:
            result = acceptable_mod(F, M)  # remove M as many times as possible. a negative number can never happen
            step_counter += result["number_of_steps"]
            F = result["result"]
        else: # the two numbers can never be equal except at (1, 1). since 1,1 exits the loop, then the two numbers both share a value that is not 1. impossible. they also can never be less than 0
            not_possible = True
    return "impossible" if not_possible else format_answer(str(step_counter))



def test():
    assert(answer("2", "1") == "1")
    assert(answer("62", "3") == "22")
    assert(answer("4", "7") == "4")
    assert(answer("3", "2") == "2")
    assert(answer("5", "5") == "impossible")
    assert(answer("2", "4") == "impossible")



test()
