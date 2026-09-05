"""Functions to help play and score a game of blackjack.
How to play blackjack: https://bicyclecards.com/how-to-play/blackjack/
Standard playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.
    """
    if card in ("J", "Q", "K"):
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): The first card.
        card_two (str): The second card.

    Returns:
        str or tuple: The higher card, or both if they are equal.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Determine the value of an ace."""
    if card_one == "A" or card_two == "A":
        return 1

    hand_value = value_of_card(card_one) + value_of_card(card_two)
    if hand_value + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is blackjack.

    Parameters:
        card_one (str): The first card.
        card_two (str): The second card.

    Returns:
        bool: True if the hand is blackjack, otherwise False.
    """
    return (card_one == "A" and value_of_card(card_two) == 10) or (
        card_two == "A" and value_of_card(card_one) == 10
    )


def can_split_pairs(card_one, card_two):
    """Determine if the hand can be split into two pairs.

    Parameters:
        card_one (str): The first card.
        card_two (str): The second card.

    Returns:
        bool: True if the cards have the same value, otherwise False.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if the hand can be doubled down.

    Parameters:
        card_one (str): The first card.
        card_two (str): The second card.

    Returns:
        bool: True if the hand total is 9, 10, or 11.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)