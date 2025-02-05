from .pixPayload import pixPayload
from .pixInfo import pixInfo
def generatePix(price: float, robuxAmount: int):
    
    if not isinstance(price, float):
        return "Valor inválido"
    
    message = f"Pagamento de {robuxAmount} robux"
    
    payload = pixPayload(pixInfo['name'], pixInfo['key'], pixInfo['city'], price, pixInfo['txtId'], message)
    pixCopyPaste = payload.generatePayLoadCode()
    pixQrCode = payload.generateQrCode(pixCopyPaste)
    return pixCopyPaste, pixQrCode