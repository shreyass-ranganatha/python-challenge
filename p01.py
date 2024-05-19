# http://www.pythonchallenge.com/pc/def/map.html
# http://www.pythonchallenge.com/pc/def/ocr.html

st = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

transtable = str.maketrans({
    ord(_): (ord(_)+2 if ord(_)+2 <= ord('z') else ord('a')-1 + ((ord(_)+2) - ord('z')))
    for _ in "abcdefghijklmnopqrstuvwxyz"
})

print(st.translate(transtable))
print("map".translate(transtable))
