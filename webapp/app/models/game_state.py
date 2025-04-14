import random
from app.data.loader import get_all_secids, get_candles_for_asset

class GameSession:
    def __init__(self):
        self.asset = random.choice(get_all_secids())
        self.candles = get_candles_for_asset(self.asset)
        self.start_index = random.randint(0, len(self.candles) - 36)

    def get_game_data(self):
        sample = self.candles.iloc[self.start_index:self.start_index + 30]
        return sample.to_dict(orient="records")

    def get_target_direction(self):
        current_close = self.candles.iloc[self.start_index + 29]['CLOSE']
        future_close = self.candles.iloc[self.start_index + 34]['CLOSE']
        return 'up' if future_close > current_close else 'down'
