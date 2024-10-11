def accum(st):
    count = []
    for i, char in enumerate(st):
        part = char.upper() + char.lower()*i
        count.append(part)
    return '-'.join(count)
       

print(accum("ZpglnRxqenU")), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
print(accum("NyffsGeyylB")), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
print(accum("MjtkuBovqrU")), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
