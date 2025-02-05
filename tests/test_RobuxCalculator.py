import sys
import os
sys.path.append(os.path.abspath(".."))

from src.Model.robuxPrice import robuxPriceWithTax, robuxPriceWithoutTax
from src.Model.robuxCalculator import calculateRobux


def test_calculateRobux():
    priceWithoutTaxOf1000Robux = 1000 * robuxPriceWithoutTax
    priceWithTaxOf1000Robux = 1000/0.7 * robuxPriceWithTax
    
    print(priceWithTaxOf1000Robux)
    
    expectedPriceOf1000Robux = calculateRobux(1000)
    
    assert expectedPriceOf1000Robux[0] == priceWithoutTaxOf1000Robux and expectedPriceOf1000Robux[1] == priceWithTaxOf1000Robux