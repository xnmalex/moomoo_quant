def calculate_score(row):
    score = 0

    # # Momentum
    # if row['change_rate'] > 5:
    #     score += 2

    # Volume spike
    # if row['volume'] > 2 * row['volume_5d_avg']:
    #     score += 3

    # # Price strength
    # if row['last_price'] > row['open_price']:
    #     score += 1

    return score

def premarket_scan(data):
    candidates = []
    for _, row in data.iterrows():
        candidates.append((row['code'], row['pre_change_rate']))
    return sorted(candidates, key=lambda x: x[1], reverse=True)

def rank_stocks(data):
    candidates = []

    for _, row in data.iterrows():
        score = calculate_score(row)
        candidates.append((row['code'], row['last_price']))

    return sorted(candidates, key=lambda x: x[1], reverse=True)