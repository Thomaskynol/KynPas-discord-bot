from .robuxPrice import robuxPriceWithoutTax, robuxPriceWithTax

def calculateRobux(robuxAmount: int):
    return robuxAmount * robuxPriceWithoutTax, robuxAmount/0.7 * robuxPriceWithTax