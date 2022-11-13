from DRE import DRE

# THE CHALLENGE ########################################################################################################

# Crack the following ciphertext:
ciphertext = '''?0:?Lm=BIOQb/OAH<P11+X_lk+oe_L-wyreJ845a%dh$~*n>yY1HqLj)5=cH(WHUn.N/uDBKc$s-J"Xg"5^TMEx9)w9d%5uiYa9qML:&S?KGS,aqceg?IUr8se#N/AU4nj*)}B3oduaBbx#DN~/bda-@B+x8^B7VO;l3eG>Hx*;q94)~-Wk14E4D#^N%$7+O)PGH/IdpKWnB8qn1Y*_*aDeyg((lK:8M:KNu^gikT5)1AwD%%@T~pB9VG"V,$Gm-Og)MPVjK;-'YNBNoNacmLzUW@>3i&j,&/T^0p@}+$$z4$CNAW%'i3^MqSWeKXeaL7S:"w<Wz.y=:'sX-DS5Pq9@?Qr(,@5nPcYz(kl5iLmJh%-p>>Had_8#$9eJ'sy9hDh&=o?.h=b>qzPlqq,Y''l)I_LwS'scG='sy=gBPk-qXNJ}LD?8qzGSV/UW(C.OcKQa98scX)+-q<iB@)emEC*'C~"D.dEuHaJdVMrU~aCA5)0a8X&&E"k*T%?,wxOb0Y$Lx9qD-az15QaBcpAG**lTm'AVO.mqMipJh.b^'J4$-y&&O-=m3CQxOQ}-:^Mc,k<D"8lCg-uhS_B4&"Uzo0?*:ohy3Djh-NI4^c(a3SnY^_EdS^?<}C4I(j&4V*pE3-MIm;;e*u:ujsyQA"Ur.s%G&cMS30y_H+Yz/CCSe+IK4TIGsV:9HeP*9H$r^M+,y7}x(}YN$yz;<#olC~E15<lmbAK97SsE@b)j$u~=9yPq>)>_W}ddWj:,:@7*Yz14Xc54A"4&5w%8)57(%8.<5qYB'orY"l0xM:jTO3B.lrGDpYj;Pb:pKj}u^e^X/S9-uy8pgK3:J-.n;C#:):_PH9K*)iY}}rA_'$KUX/3^c./L&VGkw#CuGY9sC>&5d&BQo}/7s1iWV=_4XYcNwj:x^@#-;QgaCX_(NbV3szI~~BHYJc}aiT}~'",5;cK^?Y3"W:V&XJO.Hu4$h-qx%jc4u)De;>5,}o=dXywDU}0/M)4_<_Q%(~oa#eIpM-Kx$j13~r&Y?KrMK4@~=*WedQc'aJq}YaB));XX5zG"SXYT:r_JKdcT)^0p8pO.-p>w$*Su}+p.Tg<3VhNs<z1)8^/x#W)W)VQ=xP15+@OY'q81"d7UB5Te$uGG:4#PV$jSq=7}#QHIQnCK:~PN4^oCC1(5e5;4,b'JiJexxwkYO@zp),qTCjYCH<^'B=p/7S(IjME_*)+M/C4V/*%:oC?(,qp?V4H/1y4@5j,Cg.al""3~mW+?qNpXKw_hH/kQ~@Pxkms9=>C&_+s#ll~T9z+&4)<qV^5:0@PuQAs"<Ls+Y"YO+Tk~"-_rjb-KeB"8D99zyi7//@yPL,y8?qU'OCr&DX-B'''

# I will give you the key just so you can imitate a known-plaintext attack, but obviously a real attacker
# wouldn't know the key:
plaintext_symbols = '''E G)Z@o+."2i5;Q^6c~K}J9zXbIr&Fd4A'n_L,yfC*gx7#kTUDV1$SWhHjuOP%vwNt?-Ra:(><qps{B!m/Yl3M=e08'''
ciphertext_symbols = '''<?pzL%B3W~qUSX;xPhVTH$s&:YMojuDd.7)kJ5IGN=>8n(4-1^g9A#'_@b+irl"ewc*QE0,aC}ym/KO'''
key = (plaintext_symbols, ciphertext_symbols)

# You can use this DRE object to encrypt/decrypt using the given key:
dre = DRE(*key)

# Important notes:
#    1. As an attacker, you don't immediately know what bases are being used; the plaintext is base-90 and the
#       ciphertext is base-79, but do NOT assume you know this beforehand.
#    2. If you encrypt the same plaintext multiple times, you will get multiple different ciphertexts. This is
#       because my implementation has a small element of randomness when encrypting. I don't believe this really adds
#       to the security, it was just a design choice. But it might make your job as an attacker more annoying, so keep
#       that in mind.
########################################################################################################################


# YOUR CODE HERE
