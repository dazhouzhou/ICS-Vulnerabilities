# -*- coding: utf-8 -*-
from kitty.model import *
from kitty.interfaces import WebInterface
from kitty.fuzzers import ServerFuzzer
from controller import WinAppDbgController
from target import TcpTarget
import struct

web_port = 26000
target_ip = '127.0.0.1'
target_port = 81


#step1 fuzz get
data = Template(name='HTTP_GET', fields=[
    String('GET', name='method', fuzzable=False),   
    Delimiter(' ', name='space1', fuzzable=False), 
    String('/getcaminfo.asp', name='path'),          
    Delimiter('?', name='question mark'),
    String('VWID', name='parameter'),
    Delimiter('=', name='equals sign'),
    String('1', name='value'),
    Delimiter(' ', name='space2'),                  
    String('HTTP', name='protocol name'),           
    Delimiter('/', name='fws1'),                    
    Dword(1, name='major version',                  
          encoder=ENC_INT_DEC),                    
    Delimiter('.', name='dot1'),                    
    Dword(1, name='minor version',     
          encoder=ENC_INT_DEC),                    
    Static('\r\n\r\n', name='eom')
])



#define target
target = TcpTarget(name='test_target', host=target_ip, port=target_port, timeout=2)
target.set_expect_response(True)

#define controller
controller = WinAppDbgController(name='test_controller', process_path='C:\\ProgramData\\SOFTCMS\\AspWebServer.exe')
target.set_controller(controller)

#define model
model = GraphModel()
model.connect(data)

#define fuzzer
fuzzer = ServerFuzzer()

fuzzer.set_interface(WebInterface(host='0.0.0.0', port=web_port))
fuzzer.set_model(model)
fuzzer.set_target(target)
fuzzer.set_delay_between_tests(0.5)
fuzzer.start()




