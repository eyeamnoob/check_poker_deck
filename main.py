ORDER = {str(i): i for i in range(1, 11)}
ORDER['J'] = 11
ORDER['Q'] = 12
ORDER['K'] = 13
ORDER['A'] = 14

custom_order = lambda x: ORDER[x]


def pocker_hand_ranking(deck):
    card_value = [None] * 5
    card_suit = [None] * 5
    for i in range(len(deck)):
        card_value[i] = deck[i][0:-1]
        card_suit[i] = deck[i][-1]
    
    sorted_card_value = sorted(card_value, key=custom_order)

    full_house1 = 0
    full_house2 = 0

    flag1 = False
    flag2 = False
    for i in range(len(sorted_card_value) - 1):
        if sorted_card_value[i] == sorted_card_value[i + 1]:
            if not flag1 and not flag2:
                full_house1 += 1
            else:
                full_house2 += 1            
        elif not flag1 and not flag2:
            flag1 = True
        elif flag1 and not flag2:
            flag2 = True

    if len(set(card_suit)) == 1 and set(card_value).issuperset({'10', 'J', 'Q', 'A', 'K'}):
        return 'Royal Flush'
    elif len(set(card_suit)) == 1 and max(card_value, key=custom_order) - min(card_value, key=custom_order) == 4 and len(set(card_value)) == 5:
        return 'Straight Flush'
    elif sorted_card_value[1] == sorted_card_value[2] == sorted_card_value[3] and sorted_card_value[1] in [sorted_card_value[0], sorted_card_value[4]]:
        return 'Four of a Kind'
    elif full_house1 + full_house2 == 3:
        return 'Full House'
    elif len(set(card_suit)) == 1:
        return 'Flush'
    elif custom_order(max(card_value, key=custom_order)) - custom_order(min(card_value, key=custom_order)) == 4 and len(set(card_value)) == 5:
        return 'Straight'
    elif 2 in [full_house1, full_house2]:
        return 'Three of a Kind'
    elif full_house1 == full_house2 == 1:
        return 'Two Pair'
    elif len(set(card_value)) == 4:
        return 'Pair'
    else:
        return 'High Card'


print(pocker_hand_ranking(['10h', 'Jh', 'Qh', 'Ah', 'Kh']))
print(pocker_hand_ranking(['3h', '5h', 'Qs', '9h', 'Ad']))
print(pocker_hand_ranking(['10s', '10c', '8d', '10d', '10h']))
