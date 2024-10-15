def contamination(text, char):
    if not text or not char:
        return ""
    
    print(char * len(text))

contamination("abc","z"), "zzz"
contamination("","z"), ""
contamination("abc",""), ""
contamination("_3ebzgh4","&"), "&&&&&&&&"
contamination("//case"," "), "      "