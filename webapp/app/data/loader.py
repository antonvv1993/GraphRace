import pandas as pd
from app.core.config import CSV_PATH

candles_df = pd.read_csv(CSV_PATH, parse_dates=['TRADEDATE'])

def get_all_secids():
    return candles_df['SECID'].unique().tolist()

def get_candles_for_asset(secid):
    return candles_df[candles_df['SECID'] == secid].sort_values('TRADEDATE').reset_index(drop=True)
