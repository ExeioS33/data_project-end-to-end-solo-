import os
import yfinance as yf
from datetime import datetime
import pandas as pd
from typing import List

class CAC40HistoricalData:
    """
    Retrieves and saves historical data for a list of CAC 40 stock symbols.

    Attributes:
        tickers_list (List[str]): List of stock symbols to retrieve.
        save_path (str): Path to the directory where CSV files will be saved.
    """

    def __init__(self, tickers_list: List[str], save_path: str = "."):
        """
        Initializes the class with a list of stock symbols and a save path.

        Args:
            tickers_list (List[str]): List of stock symbols to retrieve.
            save_path (str): Path to the directory where CSV files will be saved.
        """
        self.tickers_list = tickers_list
        self.save_path = save_path

    def fetch_data(self, ticker_symbol: str) -> pd.DataFrame:
        """
        Retrieves historical data for a given stock symbol.

        Args:
            ticker_symbol (str): The stock symbol to process.
        
        Returns:
            pd.DataFrame: A DataFrame containing the historical data, sorted by descending date.
        """
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="max")
        data.index = data.index.tz_localize(None)
        # Can reverse the order of rows to have the most recent date first
        return data

    def save_to_csv(self, data: pd.DataFrame, ticker_symbol: str) -> None:
        """
        Saves the data to a CSV file, named after the stock symbol.

        Args:
            data (pd.DataFrame): The data to save.
            ticker_symbol (str): The stock symbol used to name the file.
        """
        filename = f"{ticker_symbol}_Historical_Data.csv"
        filepath = os.path.join(self.save_path, filename)
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['date_modification'] = current_date
        data.to_csv(filepath)
        print(f"Saved historical data for {ticker_symbol} in {filepath}")

    def process_and_save_all(self) -> None:
        """
        Processes and saves historical data for all stock symbols in the list.
        """
        for ticker_symbol in self.tickers_list:
            data = self.fetch_data(ticker_symbol)
            self.save_to_csv(data, ticker_symbol)

