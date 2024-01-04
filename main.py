import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def play_game(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    while dealer_score <= 16:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    return player_score, dealer_score

def simulate_games(total_games):
    results = {}

    for start_value in range(4, 23):
        hit_wins = 0
        hit_losses = 0
        hit_draws = 0
        stand_wins = 0
        stand_losses = 0
        stand_draws = 0

        for _ in range(total_games // 2):
            player_hand_hit = [start_value]
            player_hand_stand = [start_value]
            dealer_hand = [deal_card(), deal_card()]

            player_hand_hit.append(deal_card())
            player_score_hit, dealer_score_hit = play_game(player_hand_hit, dealer_hand)
            if player_score_hit > 21 or (dealer_score_hit <= 21 and dealer_score_hit > player_score_hit):
                hit_losses += 1
            elif player_score_hit == dealer_score_hit:
                hit_draws += 1
            else:
                hit_wins += 1

            _, dealer_score_stand = play_game(player_hand_stand, dealer_hand)
            if dealer_score_stand > 21 or (dealer_score_stand <= 21 and dealer_score_stand < start_value):
                stand_wins += 1
            elif dealer_score_stand == start_value:
                stand_draws += 1
            else:
                stand_losses += 1

        results[start_value] = {
            'hit_wins': hit_wins,
            'hit_losses': hit_losses,
            'hit_draws': hit_draws,
            'stand_wins': stand_wins,
            'stand_losses': stand_losses,
            'stand_draws': stand_draws
        }

    return results

total_games_per_start_value = 100000
results = simulate_games(total_games_per_start_value)

print("Results:")
print("Starting Value | Hit Wins | Hit Losses | Hit Draws | Stand Wins | Stand Losses | Stand Draws")
for start_value in range(4, 23):
    stats = results[start_value]
    print(f"{start_value:14} | {stats['hit_wins']:8} | {stats['hit_losses']:10} | {stats['hit_draws']:9} | {stats['stand_wins']:10} | {stats['stand_losses']:12} | {stats['stand_draws']:10}")
