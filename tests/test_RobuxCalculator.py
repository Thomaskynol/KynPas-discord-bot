import sys
import os
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("src"))

from Model.robuxPrice import robuxPrice
from Model.robuxCalculator import calculateRobux

def test_calculateRobux():
    priceOf1000Robux = 1000 * robuxPrice
    priceWithTaxOf1000Robux = priceOf1000Robux / 0.7
    
    print(priceWithTaxOf1000Robux)
    
    expectedPriceOf1000Robux = calculateRobux(1000)
    
    assert expectedPriceOf1000Robux[0] == priceOf1000Robux and expectedPriceOf1000Robux[1] == priceWithTaxOf1000Robux