from random import randint
from collections import Counter


class GameLogic:

    def calculate_score(roll):
        score = 0
        dice_count = Counter(roll).most_common()

        if not dice_count:
            return score

        # Check for straights
        if len(dice_count) == 6:
            score += 1500
            return score

        # 3, 4, 5, and 6 of a kind
        if (dice_count[0][1]) >= 3:
            if dice_count[0][0] != 1:
                score += dice_count[0][0] * 100 * (dice_count[0][1] - 2)
            else:
                score += 1000 * (dice_count[0][1] - 2)
            dice_count = dice_count[1:]

        # Check's for three pair
        if len(dice_count) == 3:
            if dice_count[2][1] == 2:
                score += 1500
                return score

        # Two 3 of a kinds
        if len(dice_count) == 1 and dice_count[0][1] == 3:
            if dice_count[0][0] != 1:
                score += dice_count[0][0] * 100
            else:
                score += 1000

        # 1's and 5's
        for dice in dice_count:
            if dice[0] == 5:
                score += dice[1] * 50
            if dice[0] == 1:
                score += dice[1] * 100

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))

    @staticmethod
    def validate_keepers(dice_roll, dice_kept):
        dice_roll_counts = Counter(dice_roll)
        dice_kept_counts = Counter(dice_kept)
        for value, count in dice_kept_counts.items():
            if value not in dice_roll_counts or dice_roll_counts[value] < count:
                return False
        return True