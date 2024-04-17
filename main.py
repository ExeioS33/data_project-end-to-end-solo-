from financial_package.cac40_historical_data import CAC40HistoricalData
from financial_package.stock_historical_data import StockHistoricalData
import os

def setup_directory(path : str):
    """Crée un répertoire s'il n'existe pas déjà."""
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    # Définir le répertoire de sauvegarde

    save_directory_unique = "./financial_data_excel"
    save_directory_lake = "./financial_data_lake"
    setup_directory(save_directory_unique)
    setup_directory(save_directory_lake)
    
    tickers = ['AI.PA','AIR.PA','ALO.PA','MT.AS','CS.PA','BNP.PA','EN.PA','CAP.PA','CA.PA','ACA.PA',
               'BN.PA','DSY.PA','EDEN.PA','ENGI.PA','EL.PA','ERF.PA','RMS.PA','KER.PA','OR.PA','LR.PA',
               'MC.PA','ML.PA','ORA.PA','RI.PA','PUB.PA','RNO.PA','SAF.PA','SGO.PA',
               'SAN.PA', 'SU.PA', 'GLE.PA', 'STLAP.PA', 'STMPA.PA', 'TEP.PA', 'HO.PA', 'TTE.PA', 'URW.PA', 'VIE.PA',
               'DG.PA', 'WLN.PA'
               ] 

    # Création d'une instance de StockHistoricalData
    stock_data = StockHistoricalData(tickers_list=tickers, save_path=save_directory_unique)
    stock_data.save_to_excel()

    # Création d'une instance de CAC40HistoricalData
    cac40_data = CAC40HistoricalData(tickers_list=tickers, save_path=save_directory_lake)
    cac40_data.process_and_save_all()

if __name__ == "__main__":
    main()
