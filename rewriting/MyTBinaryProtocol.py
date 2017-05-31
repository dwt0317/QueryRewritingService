# -*- coding:utf-8 -*-
from thrift.protocol import TBinaryProtocol


class MyTBinaryProtocol(TBinaryProtocol.TBinaryProtocol):
    def __init__(self, trans, strictRead=False, strictWrite=True):
        TBinaryProtocol.TBinaryProtocol.__init__(self, trans, strictRead, strictWrite)

    def writeString(self, str):
        if type(str) is unicode:
            str = str.encode('utf-8')
        self.writeI32(len(str))
        self.trans.write(str)


class MyTBinaryProtocolFactory(TBinaryProtocol.TBinaryProtocolFactory):
    def __init__(self, strictRead=False, strictWrite=True):
        TBinaryProtocol.TBinaryProtocolFactory.__init__(self, strictRead, strictWrite)

    def getProtocol(self, trans):
        prot = MyTBinaryProtocol(trans, self.strictRead, self.strictWrite)
        return prot