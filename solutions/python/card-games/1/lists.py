"""Functions for tracking poker hands and assorted card tasks."""



def get_rounds(number):
    return [number,number+1,number+2]
    
    
    


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    


def list_contains_round(rounds, number):
    return number in rounds
    



def card_average(hand):
    return sum(hand)/len(hand)
   


def approx_average_is_average(hand):
    actual_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    median = sorted(hand)[len(hand) // 2]

    return actual_average == first_last_average or actual_average == median 
    
   


def average_even_is_average_odd(hand):
    even_avg = sum(hand[::2]) / len(hand[::2])
    odd_avg = sum(hand[1::2]) / len(hand[1::2])
    return even_avg == odd_avg
 


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
    