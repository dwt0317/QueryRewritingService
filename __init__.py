# -*- coding:utf-8 -*-
from rewriting.RewritingServiceHandler import *
from rewriting import RewritingService
from rewriting.MyTBinaryProtocol import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.server import TServer
import threading
import sys

if __name__ == '__main__':
    handler = RewritingServiceHandler()
    processor = RewritingService.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = MyTBinaryProtocolFactory()

    try:
        server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
        print 'Rewriting server:ready to start'
        server.serve()
    except KeyboardInterrupt:
        transport.close()
        sys.exit(0)
        # print "Service closed successfully."
    except Exception as e:
        print(repr(e))


