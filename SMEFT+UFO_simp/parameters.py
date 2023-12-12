# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Mon 11 Dec 2023 22:19:32



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

csdH = Parameter(name = 'csdH',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\tilde{d},H}',
                 lhablock = 'SMEFT',
                 lhacode = [ 1 ])

cHsd = Parameter(name = 'cHsd',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{H,\\tilde{d}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 2 ])

cHbox = Parameter(name = 'cHbox',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{H,\\text{Box}}',
                  lhablock = 'SMEFT',
                  lhacode = [ 3 ])

cHDD = Parameter(name = 'cHDD',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{H,\\text{DD}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 4 ])

csdbox = Parameter(name = 'csdbox',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\square  \\tilde{d}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 5 ])

csdDD = Parameter(name = 'csdDD',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{D \\tilde{d}}',
                  lhablock = 'SMEFT',
                  lhacode = [ 6 ])

cHsdbox = Parameter(name = 'cHsdbox',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{H \\square  \\tilde{d}}',
                    lhablock = 'SMEFT',
                    lhacode = [ 7 ])

cHsdDD = Parameter(name = 'cHsdDD',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{D H \\tilde{d}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 8 ])

cHG = Parameter(name = 'cHG',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HG}}',
                lhablock = 'SMEFT',
                lhacode = [ 9 ])

csdG = Parameter(name = 'csdG',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{G \\tilde{d}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 10 ])

cdsdH1Re11 = Parameter(name = 'cdsdH1Re11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re11}',
                       lhablock = 'SMEFT',
                       lhacode = [ 11 ])

cdsdH1Re22 = Parameter(name = 'cdsdH1Re22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re22}',
                       lhablock = 'SMEFT',
                       lhacode = [ 12 ])

cdsdH1Re33 = Parameter(name = 'cdsdH1Re33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re33}',
                       lhablock = 'SMEFT',
                       lhacode = [ 13 ])

cdsdH1Re12 = Parameter(name = 'cdsdH1Re12',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re12}',
                       lhablock = 'SMEFT',
                       lhacode = [ 14 ])

cdsdH1Re13 = Parameter(name = 'cdsdH1Re13',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re13}',
                       lhablock = 'SMEFT',
                       lhacode = [ 15 ])

cdsdH1Re23 = Parameter(name = 'cdsdH1Re23',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re23}',
                       lhablock = 'SMEFT',
                       lhacode = [ 16 ])

cdsdH1Re21 = Parameter(name = 'cdsdH1Re21',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re21}',
                       lhablock = 'SMEFT',
                       lhacode = [ 17 ])

cdsdH1Re31 = Parameter(name = 'cdsdH1Re31',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re31}',
                       lhablock = 'SMEFT',
                       lhacode = [ 18 ])

cdsdH1Re32 = Parameter(name = 'cdsdH1Re32',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Re32}',
                       lhablock = 'SMEFT',
                       lhacode = [ 19 ])

cdsdH1Im11 = Parameter(name = 'cdsdH1Im11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im11}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 1 ])

cdsdH1Im22 = Parameter(name = 'cdsdH1Im22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im22}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 2 ])

cdsdH1Im33 = Parameter(name = 'cdsdH1Im33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im33}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 3 ])

cdsdH1Im12 = Parameter(name = 'cdsdH1Im12',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im12}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 4 ])

cdsdH1Im13 = Parameter(name = 'cdsdH1Im13',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im13}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 5 ])

cdsdH1Im23 = Parameter(name = 'cdsdH1Im23',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im23}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 6 ])

cdsdH1Im21 = Parameter(name = 'cdsdH1Im21',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im21}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 7 ])

cdsdH1Im31 = Parameter(name = 'cdsdH1Im31',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im31}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 8 ])

cdsdH1Im32 = Parameter(name = 'cdsdH1Im32',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cdsdH1Im32}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 9 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

msd = Parameter(name = 'msd',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{msd}',
                lhablock = 'MASS',
                lhacode = [ 9000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Wsd = Parameter(name = 'Wsd',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{Wsd}',
                lhablock = 'DECAY',
                lhacode = [ 9000005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

lamsdh = Parameter(name = 'lamsdh',
                   nature = 'internal',
                   type = 'real',
                   value = '1',
                   texname = '\\text{lamsdh}')

lamsd = Parameter(name = 'lamsd',
                  nature = 'internal',
                  type = 'real',
                  value = '1',
                  texname = '\\text{lamsd}')

ysdRdo = Parameter(name = 'ysdRdo',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{ysdRdo}')

ysdRs = Parameter(name = 'ysdRs',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{ysdRs}')

ysdRb = Parameter(name = 'ysdRb',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{ysdRb}')

ysdLdo = Parameter(name = 'ysdLdo',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{ysdLdo}')

ysdLs = Parameter(name = 'ysdLs',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{ysdLs}')

ysdLb = Parameter(name = 'ysdLb',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{ysdLb}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*(cdsdH1Re11 - cdsdH1Im11*complex(0,1)) + CKM2x1*(cdsdH1Re21 - cdsdH1Im21*complex(0,1)) + CKM3x1*(cdsdH1Re31 - cdsdH1Im31*complex(0,1))',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*(cdsdH1Re11 - cdsdH1Im11*complex(0,1)) + CKM2x2*(cdsdH1Re21 - cdsdH1Im21*complex(0,1)) + CKM3x2*(cdsdH1Re31 - cdsdH1Im31*complex(0,1))',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*(cdsdH1Re11 - cdsdH1Im11*complex(0,1)) + CKM2x3*(cdsdH1Re21 - cdsdH1Im21*complex(0,1)) + CKM3x3*(cdsdH1Re31 - cdsdH1Im31*complex(0,1))',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*(cdsdH1Re12 - cdsdH1Im12*complex(0,1)) + CKM2x1*(cdsdH1Re22 - cdsdH1Im22*complex(0,1)) + CKM3x1*(cdsdH1Re32 - cdsdH1Im32*complex(0,1))',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*(cdsdH1Re12 - cdsdH1Im12*complex(0,1)) + CKM2x2*(cdsdH1Re22 - cdsdH1Im22*complex(0,1)) + CKM3x2*(cdsdH1Re32 - cdsdH1Im32*complex(0,1))',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*(cdsdH1Re12 - cdsdH1Im12*complex(0,1)) + CKM2x3*(cdsdH1Re22 - cdsdH1Im22*complex(0,1)) + CKM3x3*(cdsdH1Re32 - cdsdH1Im32*complex(0,1))',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*(cdsdH1Re13 - cdsdH1Im13*complex(0,1)) + CKM2x1*(cdsdH1Re23 - cdsdH1Im23*complex(0,1)) + CKM3x1*(cdsdH1Re33 - cdsdH1Im33*complex(0,1))',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*(cdsdH1Re13 - cdsdH1Im13*complex(0,1)) + CKM2x2*(cdsdH1Re23 - cdsdH1Im23*complex(0,1)) + CKM3x2*(cdsdH1Re33 - cdsdH1Im33*complex(0,1))',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*(cdsdH1Re13 - cdsdH1Im13*complex(0,1)) + CKM2x3*(cdsdH1Re23 - cdsdH1Im23*complex(0,1)) + CKM3x3*(cdsdH1Re33 - cdsdH1Im33*complex(0,1))',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re11 + cdsdH1Im11*complex(0,1))*complexconjugate(CKM1x1) + (cdsdH1Re21 + cdsdH1Im21*complex(0,1))*complexconjugate(CKM2x1) + (cdsdH1Re31 + cdsdH1Im31*complex(0,1))*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re12 + cdsdH1Im12*complex(0,1))*complexconjugate(CKM1x1) + (cdsdH1Re22 + cdsdH1Im22*complex(0,1))*complexconjugate(CKM2x1) + (cdsdH1Re32 + cdsdH1Im32*complex(0,1))*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re13 + cdsdH1Im13*complex(0,1))*complexconjugate(CKM1x1) + (cdsdH1Re23 + cdsdH1Im23*complex(0,1))*complexconjugate(CKM2x1) + (cdsdH1Re33 + cdsdH1Im33*complex(0,1))*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re11 + cdsdH1Im11*complex(0,1))*complexconjugate(CKM1x2) + (cdsdH1Re21 + cdsdH1Im21*complex(0,1))*complexconjugate(CKM2x2) + (cdsdH1Re31 + cdsdH1Im31*complex(0,1))*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re12 + cdsdH1Im12*complex(0,1))*complexconjugate(CKM1x2) + (cdsdH1Re22 + cdsdH1Im22*complex(0,1))*complexconjugate(CKM2x2) + (cdsdH1Re32 + cdsdH1Im32*complex(0,1))*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re13 + cdsdH1Im13*complex(0,1))*complexconjugate(CKM1x2) + (cdsdH1Re23 + cdsdH1Im23*complex(0,1))*complexconjugate(CKM2x2) + (cdsdH1Re33 + cdsdH1Im33*complex(0,1))*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re11 + cdsdH1Im11*complex(0,1))*complexconjugate(CKM1x3) + (cdsdH1Re21 + cdsdH1Im21*complex(0,1))*complexconjugate(CKM2x3) + (cdsdH1Re31 + cdsdH1Im31*complex(0,1))*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re12 + cdsdH1Im12*complex(0,1))*complexconjugate(CKM1x3) + (cdsdH1Re22 + cdsdH1Im22*complex(0,1))*complexconjugate(CKM2x3) + (cdsdH1Re32 + cdsdH1Im32*complex(0,1))*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = '(cdsdH1Re13 + cdsdH1Im13*complex(0,1))*complexconjugate(CKM1x3) + (cdsdH1Re23 + cdsdH1Im23*complex(0,1))*complexconjugate(CKM2x3) + (cdsdH1Re33 + cdsdH1Im33*complex(0,1))*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ysdLdo',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ysdLs',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ysdLb',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ysdLdo',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ysdLs',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ysdLb',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*ysdLdo',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*ysdLs',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*ysdLb',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ysdLdo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ysdLs',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ysdLb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ysdLdo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ysdLs',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ysdLb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*ysdLdo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*ysdLs',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*ysdLb',
                  texname = '\\text{I4a33}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x1)',
                  texname = '\\text{I5a11}')

I5a12 = Parameter(name = 'I5a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x2)',
                  texname = '\\text{I5a12}')

I5a13 = Parameter(name = 'I5a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x3)',
                  texname = '\\text{I5a13}')

I5a21 = Parameter(name = 'I5a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x1)',
                  texname = '\\text{I5a21}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x2)',
                  texname = '\\text{I5a22}')

I5a23 = Parameter(name = 'I5a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x3)',
                  texname = '\\text{I5a23}')

I5a31 = Parameter(name = 'I5a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x1)',
                  texname = '\\text{I5a31}')

I5a32 = Parameter(name = 'I5a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x2)',
                  texname = '\\text{I5a32}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x3)',
                  texname = '\\text{I5a33}')

I6a11 = Parameter(name = 'I6a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x1)',
                  texname = '\\text{I6a11}')

I6a12 = Parameter(name = 'I6a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x2)',
                  texname = '\\text{I6a12}')

I6a13 = Parameter(name = 'I6a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLdo*complexconjugate(CKM1x3)',
                  texname = '\\text{I6a13}')

I6a21 = Parameter(name = 'I6a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x1)',
                  texname = '\\text{I6a21}')

I6a22 = Parameter(name = 'I6a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x2)',
                  texname = '\\text{I6a22}')

I6a23 = Parameter(name = 'I6a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLs*complexconjugate(CKM2x3)',
                  texname = '\\text{I6a23}')

I6a31 = Parameter(name = 'I6a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x1)',
                  texname = '\\text{I6a31}')

I6a32 = Parameter(name = 'I6a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x2)',
                  texname = '\\text{I6a32}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ysdLb*complexconjugate(CKM3x3)',
                  texname = '\\text{I6a33}')

