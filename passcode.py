def answer(l):
    # ensures only unique combinations
    triples = 0

    for index, number in enumerate(l): # only does unique combinations
        divisors = 0
        multiples = 0
        triples_for_number = 0
        for other_index, other_number in enumerate(l):
            if other_index < index and number % other_number == 0:
                divisors += 1
            elif other_index > index and other_number % number == 0:
                multiples += 1
        triples_for_number += divisors * multiples
        triples += triples_for_number
    return triples
