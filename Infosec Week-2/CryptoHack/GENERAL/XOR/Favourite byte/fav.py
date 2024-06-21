from pwn import *

str="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte=bytes.fromhex(str)        # Converts from hexadecimal to bytes

# XORS the output with numbers from 0 to desired range.
for i in range(20):
    print(i,"->",xor(byte,i))

# Our flag is the string on number 16. It means that the output when xored with 16 gives the flag.
'''
Output :
0 -> b"sbi`d\x7fk h! O!%O}iOv$f eb!'#Ori'um"
1 -> b'rchae~j!i !N $N|hNw%g!dc &"Nsh&tl'
2 -> b'q`kbf}i"j#"M#\'M\x7fkMt&d"g`#%!Mpk%wo'
3 -> b'pajcg|h#k"#L"&L~jLu\'e#fa"$ Lqj$vn'
4 -> b"wfmd`{o$l%$K%!KymKr b$af%#'Kvm#qi"
5 -> b'vgleazn%m$%J$ JxlJs!c%`g$"&Jwl"ph'
6 -> b'udofbym&n\'&I\'#I{oIp"`&cd\'!%Ito!sk'
7 -> b'tengcxl\'o&\'H&"HznHq#a\'be& $Hun rj'
8 -> b'{jahlwc(`)(G)-GuaG~,n(mj)/+Gza/}e'
9 -> b'zk`imvb)a()F(,Ft`F\x7f-o)lk(.*F{`.|d'
10 -> b'yhcjnua*b+*E+/EwcE|.l*oh+-)Exc-\x7fg'
11 -> b'xibkot`+c*+D*.DvbD}/m+ni*,(Dyb,~f'
12 -> b'\x7fnelhsg,d-,C-)CqeCz(j,in-+/C~e+ya'
13 -> b'~odmirf-e,-B,(BpdB{)k-ho,*.B\x7fd*x`'
14 -> b'}lgnjqe.f/.A/+AsgAx*h.kl/)-A|g){c'
15 -> b'|mfokpd/g./@.*@rf@y+i/jm.(,@}f(zb'
16 -> b'crypto{0x10_15_my_f4v0ur173_by7e}'
17 -> b'bsxqunz1y01^04^lx^g5w1ts062^cx6d|'
18 -> b'ap{rvmy2z32]37]o{]d6t2wp351]`{5g\x7f'
19 -> b'`qzswlx3{23\\26\\nz\\e7u3vq240\\az4f~'
'''
