# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Wed 28 Feb 2024 16:32:32


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '4*cHG*complex(0,1)',
                order = {'NP':1,'NPcHG':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '4*cHG*G',
                 order = {'NP':1,'NPcHG':1,'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(-2*ee*complex(0,1)*G)/3.',
                 order = {'QCD':1,'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-4*cHG*complex(0,1)*G**2',
                 order = {'NP':1,'NPcHG':1,'QCD':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '2*complex(0,1)*lamsd',
                 order = {'QED':1, 'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*lamsdh',
                 order = {'QED':1, 'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-0.3333333333333333*(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-2*ee**2*complex(0,1)*sw)/(9.*cw)',
                 order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(2*ee*complex(0,1)*G*sw)/(3.*cw)',
                 order = {'QCD':1,'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(2*ee**2*complex(0,1)*sw**2)/(9.*cw**2)',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '4*cHG*complex(0,1)*vev',
                 order = {'NP':1,'NPcHG':1,'QED':-1})

GC_47 = Coupling(name = 'GC_47',
                 value = '4*cHG*G*vev',
                 order = {'NP':1,'NPcHG':1,'QCD':1,'QED':-1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-4*cHG*complex(0,1)*G**2*vev',
                 order = {'NP':1,'NPcHG':1,'QCD':2,'QED':-1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'HHH':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'complex(0,1)*lamsdh*vev',
                 order = {'QED':1, 'NP':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '2*cHG*G*vev**2',
                 order = {'NP':1,'NPcHG':1,'QCD':1,'QED':-2})

GC_53 = Coupling(name = 'GC_53',
                 value = '-2*cHG*complex(0,1)*G**2*vev**2',
                 order = {'NP':1,'NPcHG':1,'QCD':2,'QED':-2})

GC_54 = Coupling(name = 'GC_54',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'HTT':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'YUK':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '(2*ee**2*complex(0,1))/9.',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-G',
                order = {'QCD':1})

