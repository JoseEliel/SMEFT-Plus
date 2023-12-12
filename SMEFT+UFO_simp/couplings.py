# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Mon 11 Dec 2023 22:19:32


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-3*cHbox*complex(0,1)',
                order = {'NP':1,'NPcHBox':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '2*csdH*complex(0,1)',
                 order = {'NP':1,'NPsdH':1,'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-0.5*(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cHsdDD*cw*ee*complex(0,1))/(2.*sw)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '-0.16666666666666666*(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-0.3333333333333333*(ee*complex(0,1))',
                 order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-0.3333333333333333*(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cHsdDD*ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-0.3333333333333333*(csdDD*ee*complex(0,1)*sw)/cw',
                  order = {'NP':1,'NPcsdDD':1,'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(-2*ee**2*complex(0,1)*sw)/(9.*cw)',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(-4*csdDD*ee**2*complex(0,1)*sw)/(9.*cw)',
                  order = {'NP':1,'NPcsdDD':1,'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(2*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'QCD':1,'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(2*csdDD*ee*complex(0,1)*G*sw)/(3.*cw)',
                  order = {'NP':1,'NPcsdDD':1,'QCD':1,'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(2*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(4*csdDD*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                  order = {'NP':1,'NPcsdDD':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(cHsdDD*cw*ee**2*complex(0,1))/(6.*sw) + (cHsdDD*ee**2*complex(0,1)*sw)/(6.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.5*(cHsdDD*cw*ee*complex(0,1)*G)/sw - (cHsdDD*ee*complex(0,1)*G*sw)/(2.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QCD':1,'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '6*cHDD*ee**2*complex(0,1) + (3*cHDD*cw**2*ee**2*complex(0,1))/sw**2 + (3*cHDD*ee**2*complex(0,1)*sw**2)/cw**2',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '-0.3333333333333333*(cHsdDD*ee**2*complex(0,1)) - (cHsdDD*ee**2*complex(0,1)*sw**2)/(3.*cw**2)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-3*cHbox*complex(0,1)*vev',
                  order = {'NP':1,'NPcHBox':1,'QED':-1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(cHDD*complex(0,1)*vev)',
                  order = {'NP':1,'NPcHDD':1,'QED':-1})

GC_128 = Coupling(name = 'GC_128',
                  value = '4*cHG*complex(0,1)*vev',
                  order = {'NP':1,'NPcHG':1,'QED':-1})

GC_129 = Coupling(name = 'GC_129',
                  value = '6*cHsd*complex(0,1)*vev',
                  order = {'NP':1,'NPcHsd':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(2*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cHsdbox*complex(0,1)*vev)',
                  order = {'NP':1,'NPcHsdbox':1,'QED':-1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-0.5*(cHsdDD*complex(0,1)*vev)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':-1})

GC_132 = Coupling(name = 'GC_132',
                  value = '2*csdH*complex(0,1)*vev',
                  order = {'NP':1,'NPsdH':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-0.16666666666666666*(cHsdDD*ee*complex(0,1)*vev)',
                  order = {'NP':1,'NPcHsdDD':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '4*cHG*G*vev',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':-1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(cHsdDD*complex(0,1)*G*vev)/2.',
                  order = {'NP':1,'NPcHsdDD':1,'QCD':1,'QED':-1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-4*cHG*complex(0,1)*G**2*vev',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':-1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((complex(0,1)*I1a11*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(complex(0,1)*I1a11*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((complex(0,1)*I1a12*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(ee*complex(0,1))',
                 order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(complex(0,1)*I1a12*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((complex(0,1)*I1a13*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(complex(0,1)*I1a13*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((complex(0,1)*I1a21*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(complex(0,1)*I1a21*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((complex(0,1)*I1a22*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(complex(0,1)*I1a22*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*I1a23*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(complex(0,1)*I1a23*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((complex(0,1)*I1a31*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'ee*complex(0,1)',
                 order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(complex(0,1)*I1a31*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((complex(0,1)*I1a32*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(complex(0,1)*I1a32*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*I1a33*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(complex(0,1)*I1a33*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((complex(0,1)*I2a11*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(complex(0,1)*I2a11*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((complex(0,1)*I2a12*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(complex(0,1)*I2a12*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((complex(0,1)*I2a13*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-0.16666666666666666*(cHsdDD*ee*complex(0,1))',
                 order = {'NP':1,'NPcHsdDD':1,'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(complex(0,1)*I2a13*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((complex(0,1)*I2a21*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(complex(0,1)*I2a21*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*I2a22*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(complex(0,1)*I2a22*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((complex(0,1)*I2a23*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(complex(0,1)*I2a23*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*I2a31*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(complex(0,1)*I2a31*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*I2a32*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(csdDD*ee*complex(0,1))/3.',
                 order = {'NP':1,'NPcsdDD':1,'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(complex(0,1)*I2a32*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((complex(0,1)*I2a33*vev)/cmath.sqrt(2))',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(complex(0,1)*I2a33*vev)/cmath.sqrt(2)',
                  order = {'NP':1,'NPcdsdH1':1,'QED':-1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = 'complex(0,1)*lamsdh*vev',
                  order = {'QCD':2,'QED':-1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(cHsdDD*cw*ee*complex(0,1)*vev)/(2.*sw)',
                  order = {'NP':1,'NPcHsdDD':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(cHsdDD*ee*complex(0,1)*sw*vev)/(6.*cw)',
                  order = {'NP':1,'NPcHsdDD':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '3*cHsd*complex(0,1)*vev**2',
                  order = {'NP':1,'NPcHsd':1,'QED':-1})

GC_179 = Coupling(name = 'GC_179',
                  value = 'csdH*complex(0,1)*vev**2',
                  order = {'NP':1,'NPsdH':1,'QED':-1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(2*ee**2*complex(0,1))/9.',
                 order = {'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '2*cHG*G*vev**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':-2})

GC_181 = Coupling(name = 'GC_181',
                  value = '-2*cHG*complex(0,1)*G**2*vev**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':-2})

GC_182 = Coupling(name = 'GC_182',
                  value = 'cHsd*complex(0,1)*vev**3',
                  order = {'NP':1,'NPcHsd':1,'QED':-2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(cHsdDD*cw*ee**2*complex(0,1)*vev)/(6.*sw) + (cHsdDD*ee**2*complex(0,1)*sw*vev)/(6.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-0.5*(cHsdDD*cw*ee*complex(0,1)*G*vev)/sw - (cHsdDD*ee*complex(0,1)*G*sw*vev)/(2.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QCD':1})

GC_185 = Coupling(name = 'GC_185',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '6*cHDD*ee**2*complex(0,1)*vev + (3*cHDD*cw**2*ee**2*complex(0,1)*vev)/sw**2 + (3*cHDD*ee**2*complex(0,1)*sw**2*vev)/cw**2',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-0.3333333333333333*(cHsdDD*ee**2*complex(0,1)*vev) - (cHsdDD*ee**2*complex(0,1)*sw**2*vev)/(3.*cw**2)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(cHsdDD*cw*ee*complex(0,1)*vev**2)/(4.*sw) + (cHsdDD*ee*complex(0,1)*sw*vev**2)/(4.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QED':-1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cHsdDD*cw*ee**2*complex(0,1)*vev**2)/(12.*sw) + (cHsdDD*ee**2*complex(0,1)*sw*vev**2)/(12.*cw)',
                  order = {'NP':1,'NPcHsdDD':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'ee**2*complex(0,1)',
                 order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '-0.25*(cHsdDD*cw*ee*complex(0,1)*G*vev**2)/sw - (cHsdDD*ee*complex(0,1)*G*sw*vev**2)/(4.*cw)',
                  order = {'NP':1,'NPcHsdDD':1,'QCD':1,'QED':-1})

GC_191 = Coupling(name = 'GC_191',
                  value = '3*cHDD*ee**2*complex(0,1)*vev**2 + (3*cHDD*cw**2*ee**2*complex(0,1)*vev**2)/(2.*sw**2) + (3*cHDD*ee**2*complex(0,1)*sw**2*vev**2)/(2.*cw**2)',
                  order = {'NP':1,'NPcHDD':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-0.16666666666666666*(cHsdDD*ee**2*complex(0,1)*vev**2) - (cHsdDD*ee**2*complex(0,1)*sw**2*vev**2)/(6.*cw**2)',
                  order = {'NP':1,'NPcHsdDD':1})

GC_193 = Coupling(name = 'GC_193',
                  value = 'cHDD*ee**2*complex(0,1)*vev**3 + (cHDD*cw**2*ee**2*complex(0,1)*vev**3)/(2.*sw**2) + (cHDD*ee**2*complex(0,1)*sw**2*vev**3)/(2.*cw**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':-1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '-(cHDD*complex(0,1))',
                order = {'NP':1,'NPcHDD':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(4*csdDD*ee**2*complex(0,1))/9.',
                 order = {'NP':1,'NPcsdDD':1,'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '-(complex(0,1)*ysdRb)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'complex(0,1)*ysdRb',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(complex(0,1)*ysdRdo)',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = 'complex(0,1)*ysdRdo',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(complex(0,1)*ysdRs)',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = 'complex(0,1)*ysdRs',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-G',
                 order = {'QCD':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '4*cHG*G',
                 order = {'NP':1,'NPcHG':1,'QCD':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cHsdDD*complex(0,1)*G)/2.',
                 order = {'NP':1,'NPcHsdDD':1,'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(csdDD*complex(0,1)*G)',
                 order = {'NP':1,'NPcsdDD':1,'QCD':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '4*csdG*G',
                 order = {'NP':1,'NPcsdG':1,'QCD':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-2*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-2*csdDD*ee*complex(0,1)*G)/3.',
                 order = {'NP':1,'NPcsdDD':1,'QCD':1,'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '4*cHG*complex(0,1)',
                order = {'NP':1,'NPcHG':1})

GC_30 = Coupling(name = 'GC_30',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-4*cHG*complex(0,1)*G**2',
                 order = {'NP':1,'NPcHG':1,'QCD':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '2*csdDD*complex(0,1)*G**2',
                 order = {'NP':1,'NPcsdDD':1,'QCD':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-4*csdG*complex(0,1)*G**2',
                 order = {'NP':1,'NPcsdG':1,'QCD':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((complex(0,1)*I1a11)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(complex(0,1)*I1a11)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((complex(0,1)*I1a12)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(complex(0,1)*I1a12)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((complex(0,1)*I1a13)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(complex(0,1)*I1a13)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_4 = Coupling(name = 'GC_4',
                value = '6*cHsd*complex(0,1)',
                order = {'NP':1,'NPcHsd':1,'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((complex(0,1)*I1a21)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(complex(0,1)*I1a21)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*I1a22)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(complex(0,1)*I1a22)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((complex(0,1)*I1a23)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(complex(0,1)*I1a23)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((complex(0,1)*I1a31)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(complex(0,1)*I1a31)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((complex(0,1)*I1a32)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(complex(0,1)*I1a32)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(cHsdbox*complex(0,1))',
                order = {'NP':1,'NPcHsdbox':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((complex(0,1)*I1a33)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(complex(0,1)*I1a33)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((complex(0,1)*I2a11)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(complex(0,1)*I2a11)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((complex(0,1)*I2a12)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(complex(0,1)*I2a12)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((complex(0,1)*I2a13)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(complex(0,1)*I2a13)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*I2a21)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(complex(0,1)*I2a21)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_6 = Coupling(name = 'GC_6',
                value = '-0.5*(cHsdDD*complex(0,1))',
                order = {'NP':1,'NPcHsdDD':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*I2a22)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(complex(0,1)*I2a22)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*I2a23)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(complex(0,1)*I2a23)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((complex(0,1)*I2a31)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(complex(0,1)*I2a31)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((complex(0,1)*I2a32)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(complex(0,1)*I2a32)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((complex(0,1)*I2a33)/cmath.sqrt(2))',
                 order = {'NP':1,'NPcdsdH1':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(complex(0,1)*I2a33)/cmath.sqrt(2)',
                 order = {'NP':1,'NPcdsdH1':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(csdbox*complex(0,1))',
                order = {'NP':1,'NPcsdbox':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(complex(0,1)*I3a11) - complex(0,1)*I4a11',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(complex(0,1)*I3a12) - complex(0,1)*I4a12',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(complex(0,1)*I3a13) - complex(0,1)*I4a13',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(complex(0,1)*I3a21) - complex(0,1)*I4a21',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(complex(0,1)*I3a22) - complex(0,1)*I4a22',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(complex(0,1)*I3a23) - complex(0,1)*I4a23',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(complex(0,1)*I3a31) - complex(0,1)*I4a31',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(complex(0,1)*I3a32) - complex(0,1)*I4a32',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(complex(0,1)*I3a33) - complex(0,1)*I4a33',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = 'complex(0,1)*I5a11 + complex(0,1)*I6a11',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-(csdDD*complex(0,1))',
                order = {'NP':1,'NPcsdDD':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'complex(0,1)*I5a12 + complex(0,1)*I6a12',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'complex(0,1)*I5a13 + complex(0,1)*I6a13',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'complex(0,1)*I5a21 + complex(0,1)*I6a21',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'complex(0,1)*I5a22 + complex(0,1)*I6a22',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'complex(0,1)*I5a23 + complex(0,1)*I6a23',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = 'complex(0,1)*I5a31 + complex(0,1)*I6a31',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'complex(0,1)*I5a32 + complex(0,1)*I6a32',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = 'complex(0,1)*I5a33 + complex(0,1)*I6a33',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '2*complex(0,1)*lamsd',
                 order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '4*csdG*complex(0,1)',
                order = {'NP':1,'NPcsdG':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'complex(0,1)*lamsdh',
                 order = {'QCD':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

