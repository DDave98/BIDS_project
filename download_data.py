#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author: David Michalica

import yfinance as yf
import numpy as np

class DataDownloader:

    def __init__(self, url="yahoo", folder="data", cache_filename="data_{}.csv"):
        """
        Params:
        :param str url: odkaz od kud se mají data stahovat
        :param str folder: nazev slozky kde budou data stazena
        :param str cache_filename: jmeno souboru ve specifikovane slozce
        """

        # ulozeni parametru
        self.url = url
        self.cache_filename = cache_filename
        self.path_folder = "./"+ folder


    #############################################
    def download_data(self, symbol, start_date, end_date):
        """
        metoda stahne do slozky folder vsechny soubory s daty z url
        """
        try:
            # Download historical data
            self.data = yf.download(symbol, start=start_date, end=end_date)

            # Display the data
            print(self.data.head())
            print(f'Data downloaded')
            
        except Exception as e:
            print(f'An error occurred: {e}')


    #############################################
    def save_data(self, filename):
        """
        ulozi stazene data do .csv souboru
        
        Params:
        :param filename: nazev souboru, do ktereho data chceme ulozit
        """
        
        try:
            path = self.path_folder + self.cache_filename.replace("{}",filename)
            self.data.to_csv(f'{path}')
            print(f'Data saved to {path}')

        except Exception as e:
            print(f'An error occurred: {e}')


    #############################################
    def get_dict(self, symbols, start, end, save=False):
        """
        vraci zpracovana data pro vybrane prvky, 
        pripadne data ulozi

        Params:
        :param symbols: umoznuje specifikovat pro, pro ktere chceme vysledek
        """
        
        all_dict = dict((key, np.array()) for key in symbols)
        for symbol in symbols:
            self.download_data(symbol, start, end)
            if save == True:
                self.save_data(symbol)

#############################################
if __name__ == "__main__":
    downloder = DataDownloader()
