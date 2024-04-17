import os
import pandas as pd
import random
from datetime import datetime
import yfinance as yf
from typing import Tuple
from typing import List
from .cac40_historical_data import CAC40HistoricalData

class StockHistoricalData(CAC40HistoricalData):
    """
    Derived class from CAC40HistoricalData to retrieve and save historical data 
    for a specific stock into an Excel file.
    """
    def __init__(self, tickers_list: List[str], save_path: str = ".") -> None:
        super().__init__(tickers_list, save_path)  # Initializes with the list of tickers

    def fetch_random_data(self) -> Tuple[pd.DataFrame, str]:
        """
        Selects a random ticker from the list and retrieves its historical data.
        
        Returns:
            Tuple[pd.DataFrame, str]: A tuple containing the historical data and the selected ticker symbol.
        """
        random_ticker = random.choice(self.tickers_list)  # Selects a random ticker
        return self.fetch_data(random_ticker), random_ticker

    def save_to_excel(self, filename: str = None) -> None:
        """
        Saves the historical data for a randomly selected ticker to an Excel file.
        
        Args:
            filename (str, optional): The filename for the Excel file. If not provided, a name is generated.
        """
        data, ticker = self.fetch_random_data()
        if filename is None:
            filename = f"{ticker}_Historical_Data.xlsx"
        data.index = data.index.strftime("%Y-%m-%d")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['date_modification'] = current_date
        full_path = os.path.join(self.save_path, filename)
        data.to_excel(full_path)
        print(f"Saved historical data for {ticker} at {full_path}.")

