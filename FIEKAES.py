class FIEKAES():
    import base64
    import hashlib
    from Crypto import Random
    from Crypto.Cipher import AES
    #Blendi
    def __init__(self): 
        self.bs = 16
        self.qelesi = self.qelesi()
        
    def qelesi(self):
        import random
        qelesi  = ''.join(chr(random.randint(0,0xFF)) for i in range(16))
        return hashlib.sha256(qelesi.encode()).digest()
    
    def vektoriInicializues(self):
        return Random.new().read(AES.block_size)
    
    def kontrollo(self, text, tekstiDekriptuar):
        if text == tekstiDekriptuar:
            print("Dekriptimi eshte kryer me sukses")
        else:
            print("Gabim gjate dekriptimit")
            
    #Arianiti
    def enkripto(self, teksti):
        teksti = self._pad(teksti)
        iv = self.vektoriInicializues()
        cipher = AES.new(self.qelesi, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(teksti))
    
    #Fjolla
    def dekripto(self, tekstiEnkriptuar):
        tekstiEnkriptuar = base64.b64decode(tekstiEnkriptuar)
        iv = tekstiEnkriptuar[:AES.block_size]
        cipher = AES.new(self.qelesi, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(tekstiEnkriptuar[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
    
