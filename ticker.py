import yfinance as yf
import pandas as pd

class Ticker:

  def __init__(self, stock_ticker: str):
    self.stock_ticker = stock_ticker
    self.ticker = yf.Ticker(stock_ticker)
    self.quarterly_is = self.ticker.quarterly_income_stmt
    self.annual_is = self.ticker.income_stmt
    self.market_cap = self.ticker.info['marketCap']
    self.enterprise_value = self.ticker.info['enterpriseValue']

  def get_prior_metric(self, freq: str = 'Y', metric: str = 'revenue') -> float:
    """
    Returns the value for the metric from the previous year

    Args:
      freq: either "Y" or "Q"
      metric: "revenue", "cogs", "gross profit", "opex", "ebitda"

    Returns:
      The metric in millions
    """
    