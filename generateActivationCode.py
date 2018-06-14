#-*- coding:utf-8 -*-
import uuid
def generateActivationCode (num):
    codeList = []
    for code in xrange(num):
        code = str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)
    return  codeList

if __name__ == '__main__':
    generateActivationCode(200)