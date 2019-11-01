import sys
import base64

try:
    print(sys.argv[2] + "ing")
except:
    print('Please specify if you want to Endoce or Decode. Use the Format: "python 64endocoder.py filename encode/decode"')
    sys.exit()

#ENCODE
if sys.argv[2] == "encode":
    edata = ""
    efile = open(sys.argv[1], "r")
    for x in efile:
         edata = edata + x
    efile.close()

    #Encoding
    encodedBytes = base64.b64encode(edata.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    #Writing
    file = open(sys.argv[1], "w")
    file.write(encodedStr)
elif sys.argv[2] == "decode":
#DECODE
    ddata = ""
    dfile = open(sys.argv[1], "r")
    for x in dfile:
         ddata = ddata + x
    dfile.close()

    #Encoding
    decodedBytes = base64.b64decode(ddata.encode("utf-8"))
    decodedStr = str(decodedBytes, "utf-8")

    #Writing
    file = open(sys.argv[1], "w")
    file.write(decodedStr)



