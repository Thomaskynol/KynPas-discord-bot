import crcmod
import qrcode

class pixPayload():
    def __init__(self, name, key, city, value, txtId, message):
        self.name = name
        self.key = key
        self.city = city
        self.value = value
        self.txtId = txtId
        self.message = message
        
        self.nameLen = len(self.name)
        self.keyLen = len(self.key) 
        self.cityLen = len(self.city)
        self.valueLen = len(str(self.value))
        self.txtIdLen = len(self.txtId)
        self.messageLen = len(self.message)
        
        #00 id | 14 len | BR.GOV.BCB.PIX value ++ 01 id | keyLen len | key value
        self.merchantAcountInfo = f'0014BR.GOV.BCB.PIX01{self.keyLen}{self.key}'
        self.merchantAcountLen = len(self.merchantAcountInfo)
        
        self.transactionAmountLen = len(str(self.value))
        if self.transactionAmountLen < 10:
            self.transactionAmountLen = f'0{self.transactionAmountLen}'
        
        self.txtIdLen = len(self.txtId)
        if self.txtIdLen < 10:
            self.txtIdLen = f'0{self.txtIdLen}'
            
        #62 id | len -> | id | len | txtId
        self.txtIdInfo = f'05{self.txtIdLen}{self.txtId}'
        self.txtIdInfoLen = len(self.txtIdInfo)
        if self.txtIdInfoLen < 10:
            self.txtIdInfoLen = f'0{self.txtIdInfoLen}'
        
        
        #62 id | len -> | id | len | message
        self.messageInfo = f'04{self.messageLen}{self.message}'  # ID 04 | len | message
        self.messageInfoLen = len(self.messageInfo)
        if self.messageInfoLen < 10:
            self.messageInfoLen = f'0{self.messageInfoLen}'
        
        # id | len | value
        self.payloadFormat = '000201' # ID 00 | len 02 | value 01
        self.merchantAcount = f'26{self.merchantAcountLen}{self.merchantAcountInfo}' # ID 26 | merchantAcountLen | merchantAcountInfo
        self.merchantCategoryCode = '52040000' # ID 52 | len 04 | value 0000
        self.transactionCurrency = '5303986' # ID 53 | len 03 | value 986 (BRL)
        self.transactionAmount = f'54{self.transactionAmountLen}{self.value}' # ID 54 | transactionAmountLen | value
        self.countryCode = '5802BR' # ID 58 | len 02 | value BR
        self.merchantName = f'59{self.nameLen}{self.name}' # ID 59 | nameLen | name
        self.merchantCity = f'60{self.cityLen}{self.city}' # ID 60 | cityLen | city
        self.addDataField = f'62{self.txtIdInfoLen}{self.txtIdInfo}' # ID 62 | txtIdInfoLen | txtIdInfo --> | id | len | txtId
        self.addMessageField = f'62{self.messageInfoLen}{self.messageInfo}'
        self.crc16 = '6304' # ID 63 | len 04 | value CRC16
        
    def generatePayLoadCode(self):
        payloadInfos = f'{self.payloadFormat}{self.merchantAcount}{self.merchantCategoryCode}{self.transactionCurrency}{self.transactionAmount}{self.countryCode}{self.merchantName}{self.merchantCity}{self.addDataField}{self.crc16}'
        
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        crc16Code = hex(crc16(str(payloadInfos).encode('utf-8'))).replace('0x', '').upper()
        
        return f'{payloadInfos}{crc16Code}'
        
        #print(f'Pix Copy and Paste::\n{self.payloadCode}')
        #self.generateQrCode(self.payloadCode)
        
    def generateQrCode(self, code):
        return qrcode.make(code)
        #self.qrcode.save("pix_qr_code.png")
        #print("QR Code generated and saved as 'pix_qr_code.png")