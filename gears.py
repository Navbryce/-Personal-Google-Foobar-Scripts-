from fractions import Fraction


#  NOTE: Work for equations done by hand in a notebook. If you want to see the work, please e-mail me

def fraction_array_decorator(function):
    """ function must output a Fraction object"""
    def wrapper(gear_list):
        return fraction_to_array(function(gear_list))
    return wrapper

def fraction_to_array(fraction):
    return [fraction.numerator, fraction.denominator]

@fraction_array_decorator # i realize that this function and the function below (odd gear_number) can be simplified a lot to smaller code
def even_gear_number(gear_list):
    result = None

    first_value = (gear_list[len(gear_list) - 1] - gear_list[0])
    result = Fraction(first_value * 2, 3) # see equation for the scalars

    summation = 0

    if len(gear_list) >= 4:
        gears_to_sum = range(1, len(gear_list) - 1)
        factor = 1
        for gear_index in gears_to_sum:
            summation += factor * gear_list[gear_index]
            factor = factor * -1 #  alternation summation
        summation_fraction = Fraction(4 * summation, 3) # see equation for the scalars
        result += summation_fraction
    return result


@fraction_array_decorator
def odd_gear_number(gear_list):
    result = None

    first_value = (-gear_list[len(gear_list) - 1] - gear_list[0])
    result = Fraction(first_value * 2, 1) # see equation for the scalars

    summation = 0

    if len(gear_list) >= 3:
        gears_to_sum = range(1, len(gear_list) - 1)
        factor = 1
        for gear_index in gears_to_sum:
            summation += factor * gear_list[gear_index]
            factor = factor * -1 #  alternation summation
        summation_fraction = Fraction(4 * summation, 1) # see equation for the scalars
        result += summation_fraction
    return result


def answer_meets_constraints(answer, gear_list):
    valid = True

    previous_gear_size = None
    previous_gear = None
    gear_sizes_array = []
    for gear in gear_list:
        if previous_gear_size is None: # it's the first gear
            gear_size = answer[0] / answer[1]
        else:
            gear_size = gear - previous_gear - previous_gear_size
        if gear_size < 1:
            valid = False
            break
        else:
            gear_sizes_array.append(gear_size)
        previous_gear = gear
        previous_gear_size = gear_size
    return valid



def answer(pegs):
    answer = None
    if len(pegs) >= 2:
        if len(pegs) % 2 == 0:
            answer = even_gear_number(pegs)
        else:
            answer = odd_gear_number(pegs)
        answer = answer if answer_meets_constraints(answer, pegs) else [-1, -1]
    else:
        answer = [-1, -1]
    return answer



gear_list = [4, 30, 40, 50]
print(answer(gear_list))
