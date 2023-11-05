#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author: David Michalica

import os
import yfinance as yf
import numpy as np
from abc import ABC, abstractmethod
from config import EventDataUrl
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Abstract class - Interface
class DataDownloader(ABC):

    def __init__(self, folder="data"):
        self.cache_filename = "data_{}.csv"
        self.path_folder = "./"+ folder + "/"

    @abstractmethod
    def download_data(self, symbol, start_date, end_date):
        """
        metoda stahne do slozky folder vsechny soubory s daty z url
        """
        pass

    def createFolder(self):
        # Check if the folder exists
        if not os.path.exists(self.path_folder):
            # If it doesn't exist, create the folder
            os.makedirs(self.path_folder)

    def save_data(self, filename, data):
        """
        ulozi stazene data do .csv souboru
        
        Params:
        :param filename: nazev souboru, do ktereho data chceme ulozit
        """
        #create folder if not exist
        self.createFolder()

        try:
            path = self.path_folder + self.cache_filename.replace("{}",filename)
            data.to_csv(f'{path}')
            print(f'Data saved to {path}')

        except Exception as e:
            print(f'An error occurred: {e}')

    @abstractmethod
    def get_dict(self, symbols, start, end):
        """
        vraci zpracovana data pro vybrane prvky, 
        pripadne data ulozi

        Params:
        :param symbols: umoznuje specifikovat pro, pro ktere chceme vysledek
        """
        pass

# Finance Data Downloader
class FinanceDownloader(DataDownloader):

    def __init__(self, folder="data", save=False):
        super().__init__(folder)
        self.saveData = save

    #############################################
    def download_data(self, symbol, startDate, endDate):
        try:
            self.data = yf.download(symbol, start=startDate, end=endDate)
            print("Finance Data dowloaded successfully")
            
        except Exception as e:
            print(f'An error occurred while Finance Data download process: {e}')

    #############################################
    def get_dict(self, symbols, startDate, endDate):        
        all_dict = {key: np.array([]) for key in symbols}
        for symbol in symbols:
            self.download_data(symbol, startDate, endDate)
            if self.saveData == True:
                self.save_data(symbol, self.data)
        return all_dict


# Historical Data Downloader
class EventDowloader(DataDownloader):

    def __init__(self, folder="data", save=False):
        super().__init__(folder)
        self.saveData = save
        self.api = KaggleApi()
        self.api.authenticate()

    def download_data(self, symbol):
        try:
            self.createFolder()
            self.api.dataset_download_files(dataset=symbol, path="./data", unzip=True)
            self.data = ""
            
        except Exception as e:
            print(f'An error occurred while Event Data download process: {e}')

    def get_dict(self, symbols):
        for symbol in symbols:
            self.download_data(symbol)

#############################################
if __name__ == "__main__":
    fd = FinanceDownloader(save=True)
    fd.get_dict(["MSFT"], "1990-01-01", "2000-01-01")

    ed = EventDowloader(save=True)
    source = [member.value for member in EventDataUrl]
    #ed.download_data(EventDataUrl.BBC, "1990-01-01", "2000-01-01")
    ed.get_dict(source)