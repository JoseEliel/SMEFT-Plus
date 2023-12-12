# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Mon 11 Dec 2023 22:19:32


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS6, L.SSSS9 ],
             couplings = {(0,0):C.GC_88,(0,2):C.GC_1,(0,1):C.GC_2})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS6, L.SSS7 ],
             couplings = {(0,0):C.GC_173,(0,2):C.GC_126,(0,1):C.GC_127})

V_3 = Vertex(name = 'V_3',
             particles = [ P.g, P.g, P.H, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVSS2 ],
             couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVS2 ],
             couplings = {(0,0):C.GC_128})

V_5 = Vertex(name = 'V_5',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_21})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.H, P.H ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVVSS1 ],
             couplings = {(0,0):C.GC_24})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g, P.H ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVVS1 ],
             couplings = {(0,0):C.GC_134})

V_8 = Vertex(name = 'V_8',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_21})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_180})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS2, L.VVVVSS3 ],
              couplings = {(1,1):C.GC_31,(0,0):C.GC_31,(2,2):C.GC_31})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
              couplings = {(1,1):C.GC_136,(0,0):C.GC_136,(2,2):C.GC_136})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV4, L.VVVV7, L.VVVV8 ],
              couplings = {(1,1):C.GC_30,(0,0):C.GC_30,(2,2):C.GC_30})

V_13 = Vertex(name = 'V_13',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV4, L.VVVV7, L.VVVV8 ],
              couplings = {(1,1):C.GC_181,(0,0):C.GC_181,(2,2):C.GC_181})

V_14 = Vertex(name = 'V_14',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_196})

V_15 = Vertex(name = 'V_15',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_199})

V_16 = Vertex(name = 'V_16',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_194})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_197})

V_18 = Vertex(name = 'V_18',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_198})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_207})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_208})

V_21 = Vertex(name = 'V_21',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_195})

V_22 = Vertex(name = 'V_22',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_206})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.sd__tilde__, P.sd ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_12})

V_24 = Vertex(name = 'V_24',
              particles = [ P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_90,(0,1):C.GC_5,(0,2):C.GC_6})

V_25 = Vertex(name = 'V_25',
              particles = [ P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_178})

V_26 = Vertex(name = 'V_26',
              particles = [ P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_174,(0,1):C.GC_130,(0,2):C.GC_131})

V_27 = Vertex(name = 'V_27',
              particles = [ P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_182})

V_28 = Vertex(name = 'V_28',
              particles = [ P.H, P.H, P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(5,6)' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_4})

V_29 = Vertex(name = 'V_29',
              particles = [ P.H, P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(4,5)' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_129})

V_30 = Vertex(name = 'V_30',
              particles = [ P.a, P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(4,5)' ],
              lorentz = [ L.VSSSS1 ],
              couplings = {(0,0):C.GC_16})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VSSS1 ],
              couplings = {(0,0):C.GC_133})

V_32 = Vertex(name = 'V_32',
              particles = [ P.g, P.g, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_9,(2,0):C.GC_30,(1,0):C.GC_30})

V_33 = Vertex(name = 'V_33',
              particles = [ P.g, P.g, P.g, P.sd__tilde__, P.sd ],
              color = [ 'f(1,2,3)*Identity(4,5)' ],
              lorentz = [ L.VVVSS1 ],
              couplings = {(0,0):C.GC_27})

V_34 = Vertex(name = 'V_34',
              particles = [ P.g, P.g, P.g, P.g, P.sd__tilde__, P.sd ],
              color = [ 'f(-1,1,2)*f(3,4,-1)*Identity(5,6)', 'f(-1,1,3)*f(2,4,-1)*Identity(5,6)', 'f(-1,1,4)*f(2,3,-1)*Identity(5,6)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS2, L.VVVVSS3 ],
              couplings = {(1,1):C.GC_33,(0,0):C.GC_33,(2,2):C.GC_33})

V_35 = Vertex(name = 'V_35',
              particles = [ P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.SSSS1, L.SSSS4, L.SSSS5, L.SSSS7, L.SSSS8 ],
              couplings = {(1,0):C.GC_89,(0,0):C.GC_89,(1,3):C.GC_7,(0,4):C.GC_7,(1,2):C.GC_8,(0,1):C.GC_8})

V_36 = Vertex(name = 'V_36',
              particles = [ P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(1,0):C.GC_179,(0,0):C.GC_179})

V_37 = Vertex(name = 'V_37',
              particles = [ P.d__tilde__, P.d, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_34,(0,0):C.GC_35,(1,1):C.GC_52,(0,1):C.GC_53})

V_38 = Vertex(name = 'V_38',
              particles = [ P.s__tilde__, P.d, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_36,(0,0):C.GC_37,(1,1):C.GC_54,(0,1):C.GC_55})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.d, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_38,(0,0):C.GC_39,(1,1):C.GC_56,(0,1):C.GC_57})

V_40 = Vertex(name = 'V_40',
              particles = [ P.d__tilde__, P.s, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_40,(0,0):C.GC_41,(1,1):C.GC_58,(0,1):C.GC_59})

V_41 = Vertex(name = 'V_41',
              particles = [ P.s__tilde__, P.s, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_42,(0,0):C.GC_43,(1,1):C.GC_60,(0,1):C.GC_61})

V_42 = Vertex(name = 'V_42',
              particles = [ P.b__tilde__, P.s, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_44,(0,0):C.GC_45,(1,1):C.GC_62,(0,1):C.GC_63})

V_43 = Vertex(name = 'V_43',
              particles = [ P.d__tilde__, P.b, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_46,(0,0):C.GC_47,(1,1):C.GC_64,(0,1):C.GC_65})

V_44 = Vertex(name = 'V_44',
              particles = [ P.s__tilde__, P.b, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_48,(0,0):C.GC_49,(1,1):C.GC_66,(0,1):C.GC_67})

V_45 = Vertex(name = 'V_45',
              particles = [ P.b__tilde__, P.b, P.H, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(4,5)', 'Identity(1,5)*Identity(2,4)' ],
              lorentz = [ L.FFSSS1, L.FFSSS2 ],
              couplings = {(1,0):C.GC_50,(0,0):C.GC_51,(1,1):C.GC_68,(0,1):C.GC_69})

V_46 = Vertex(name = 'V_46',
              particles = [ P.d__tilde__, P.d, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_137,(0,0):C.GC_138,(1,1):C.GC_155,(0,1):C.GC_156})

V_47 = Vertex(name = 'V_47',
              particles = [ P.s__tilde__, P.d, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_139,(0,0):C.GC_140,(1,1):C.GC_157,(0,1):C.GC_158})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.d, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_141,(0,0):C.GC_142,(1,1):C.GC_159,(0,1):C.GC_160})

V_49 = Vertex(name = 'V_49',
              particles = [ P.d__tilde__, P.s, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_143,(0,0):C.GC_144,(1,1):C.GC_161,(0,1):C.GC_162})

V_50 = Vertex(name = 'V_50',
              particles = [ P.s__tilde__, P.s, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_145,(0,0):C.GC_146,(1,1):C.GC_163,(0,1):C.GC_164})

V_51 = Vertex(name = 'V_51',
              particles = [ P.b__tilde__, P.s, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_147,(0,0):C.GC_148,(1,1):C.GC_165,(0,1):C.GC_166})

V_52 = Vertex(name = 'V_52',
              particles = [ P.d__tilde__, P.b, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_149,(0,0):C.GC_150,(1,1):C.GC_167,(0,1):C.GC_168})

V_53 = Vertex(name = 'V_53',
              particles = [ P.s__tilde__, P.b, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_151,(0,0):C.GC_152,(1,1):C.GC_169,(0,1):C.GC_170})

V_54 = Vertex(name = 'V_54',
              particles = [ P.b__tilde__, P.b, P.sd__tilde__, P.sd ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(1,0):C.GC_153,(0,0):C.GC_154,(1,1):C.GC_171,(0,1):C.GC_172})

V_55 = Vertex(name = 'V_55',
              particles = [ P.a, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(2,4)*Identity(3,5)', 'Identity(2,5)*Identity(3,4)' ],
              lorentz = [ L.VSSSS8 ],
              couplings = {(1,0):C.GC_17,(0,0):C.GC_17})

V_56 = Vertex(name = 'V_56',
              particles = [ P.H, P.H, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(3,5)*Identity(4,6)', 'Identity(3,6)*Identity(4,5)' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(1,0):C.GC_10,(0,0):C.GC_10})

V_57 = Vertex(name = 'V_57',
              particles = [ P.H, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(2,4)*Identity(3,5)', 'Identity(2,5)*Identity(3,4)' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(1,0):C.GC_132,(0,0):C.GC_132})

V_58 = Vertex(name = 'V_58',
              particles = [ P.a, P.a, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(3,5)*Identity(4,6)', 'Identity(3,6)*Identity(4,5)' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_59 = Vertex(name = 'V_59',
              particles = [ P.a, P.a, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18})

V_60 = Vertex(name = 'V_60',
              particles = [ P.g, P.sd__tilde__, P.sd ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_22})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.g, P.sd__tilde__, P.sd ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_28})

V_62 = Vertex(name = 'V_62',
              particles = [ P.g, P.H, P.H, P.sd__tilde__, P.sd ],
              color = [ 'T(1,5,4)' ],
              lorentz = [ L.VSSSS1 ],
              couplings = {(0,0):C.GC_25})

V_63 = Vertex(name = 'V_63',
              particles = [ P.g, P.H, P.sd__tilde__, P.sd ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VSSS1 ],
              couplings = {(0,0):C.GC_135})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.g, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(3,5)*T(2,6,4)', 'Identity(3,6)*T(2,5,4)', 'Identity(4,5)*T(2,6,3)', 'Identity(4,6)*T(2,5,3)' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(3,0):C.GC_29,(1,0):C.GC_29,(2,0):C.GC_29,(0,0):C.GC_29})

V_65 = Vertex(name = 'V_65',
              particles = [ P.g, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'Identity(2,4)*T(1,5,3)', 'Identity(2,5)*T(1,4,3)', 'Identity(3,4)*T(1,5,2)', 'Identity(3,5)*T(1,4,2)' ],
              lorentz = [ L.VSSSS2, L.VSSSS3, L.VSSSS6, L.VSSSS7 ],
              couplings = {(1,2):C.GC_26,(0,0):C.GC_26,(3,3):C.GC_26,(2,1):C.GC_26})

V_66 = Vertex(name = 'V_66',
              particles = [ P.g, P.g, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
              color = [ 'T(1,5,3)*T(2,6,4)', 'T(1,5,4)*T(2,6,3)', 'T(1,6,3)*T(2,5,4)', 'T(1,6,4)*T(2,5,3)' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(3,0):C.GC_32,(2,0):C.GC_32,(1,0):C.GC_32,(0,0):C.GC_32})

V_67 = Vertex(name = 'V_67',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_15})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_91})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_175})

V_70 = Vertex(name = 'V_70',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_19})

V_71 = Vertex(name = 'V_71',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_106})

V_72 = Vertex(name = 'V_72',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_92})

V_73 = Vertex(name = 'V_73',
              particles = [ P.u__tilde__, P.d__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_70,(0,1):C.GC_203})

V_74 = Vertex(name = 'V_74',
              particles = [ P.c__tilde__, P.d__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_71})

V_75 = Vertex(name = 'V_75',
              particles = [ P.t__tilde__, P.d__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_72})

V_76 = Vertex(name = 'V_76',
              particles = [ P.u__tilde__, P.s__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_73})

V_77 = Vertex(name = 'V_77',
              particles = [ P.c__tilde__, P.s__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_74,(0,1):C.GC_205})

V_78 = Vertex(name = 'V_78',
              particles = [ P.t__tilde__, P.s__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_75})

V_79 = Vertex(name = 'V_79',
              particles = [ P.u__tilde__, P.b__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_76})

V_80 = Vertex(name = 'V_80',
              particles = [ P.c__tilde__, P.b__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_77})

V_81 = Vertex(name = 'V_81',
              particles = [ P.t__tilde__, P.b__tilde__, P.sd__tilde__ ],
              color = [ 'EpsilonBar(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_78,(0,1):C.GC_201})

V_82 = Vertex(name = 'V_82',
              particles = [ P.d, P.u, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_202,(0,1):C.GC_79})

V_83 = Vertex(name = 'V_83',
              particles = [ P.s, P.u, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_80})

V_84 = Vertex(name = 'V_84',
              particles = [ P.b, P.u, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_81})

V_85 = Vertex(name = 'V_85',
              particles = [ P.d, P.c, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_82})

V_86 = Vertex(name = 'V_86',
              particles = [ P.s, P.c, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_204,(0,1):C.GC_83})

V_87 = Vertex(name = 'V_87',
              particles = [ P.b, P.c, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_84})

V_88 = Vertex(name = 'V_88',
              particles = [ P.d, P.t, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_85})

V_89 = Vertex(name = 'V_89',
              particles = [ P.s, P.t, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_86})

V_90 = Vertex(name = 'V_90',
              particles = [ P.b, P.t, P.sd ],
              color = [ 'Epsilon(1,2,3)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_200,(0,1):C.GC_87})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Z, P.sd__tilde__, P.sd ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1, L.VSS2 ],
              couplings = {(0,1):C.GC_110,(0,0):C.GC_188})

V_92 = Vertex(name = 'V_92',
              particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_114})

V_93 = Vertex(name = 'V_93',
              particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_189})

V_94 = Vertex(name = 'V_94',
              particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_116})

V_95 = Vertex(name = 'V_95',
              particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_190})

V_96 = Vertex(name = 'V_96',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV9 ],
              couplings = {(0,0):C.GC_108})

V_97 = Vertex(name = 'V_97',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_123})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_191})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_185})

V_100 = Vertex(name = 'V_100',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_193})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_192})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_93})

V_104 = Vertex(name = 'V_104',
               particles = [ P.Z, P.H, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(4,5)' ],
               lorentz = [ L.VSSSS4, L.VSSSS5 ],
               couplings = {(0,1):C.GC_112,(0,0):C.GC_107})

V_105 = Vertex(name = 'V_105',
               particles = [ P.Z, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VSSS2, L.VSSS3 ],
               couplings = {(0,1):C.GC_177,(0,0):C.GC_176})

V_106 = Vertex(name = 'V_106',
               particles = [ P.a, P.Z, P.H, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(5,6)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_121})

V_107 = Vertex(name = 'V_107',
               particles = [ P.a, P.Z, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(4,5)' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_183})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
               color = [ 'Identity(2,4)*Identity(3,5)', 'Identity(2,5)*Identity(3,4)' ],
               lorentz = [ L.VSSSS8 ],
               couplings = {(1,0):C.GC_113,(0,0):C.GC_113})

V_109 = Vertex(name = 'V_109',
               particles = [ P.a, P.Z, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
               color = [ 'Identity(3,5)*Identity(4,6)', 'Identity(3,6)*Identity(4,5)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(1,0):C.GC_115,(0,0):C.GC_115})

V_110 = Vertex(name = 'V_110',
               particles = [ P.g, P.Z, P.H, P.H, P.sd__tilde__, P.sd ],
               color = [ 'T(1,6,5)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_122})

V_111 = Vertex(name = 'V_111',
               particles = [ P.g, P.Z, P.H, P.sd__tilde__, P.sd ],
               color = [ 'T(1,5,4)' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_184})

V_112 = Vertex(name = 'V_112',
               particles = [ P.g, P.Z, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
               color = [ 'Identity(3,5)*T(1,6,4)', 'Identity(3,6)*T(1,5,4)', 'Identity(4,5)*T(1,6,3)', 'Identity(4,6)*T(1,5,3)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(3,0):C.GC_117,(1,0):C.GC_117,(2,0):C.GC_117,(0,0):C.GC_117})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_124})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_186})

V_115 = Vertex(name = 'V_115',
               particles = [ P.Z, P.Z, P.H, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(5,6)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_125})

V_116 = Vertex(name = 'V_116',
               particles = [ P.Z, P.Z, P.H, P.sd__tilde__, P.sd ],
               color = [ 'Identity(4,5)' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_187})

V_117 = Vertex(name = 'V_117',
               particles = [ P.Z, P.Z, P.sd__tilde__, P.sd__tilde__, P.sd, P.sd ],
               color = [ 'Identity(3,5)*Identity(4,6)', 'Identity(3,6)*Identity(4,5)' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(1,0):C.GC_119,(0,0):C.GC_119})

V_118 = Vertex(name = 'V_118',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_119 = Vertex(name = 'V_119',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_120 = Vertex(name = 'V_120',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_121 = Vertex(name = 'V_121',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_122 = Vertex(name = 'V_122',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_123 = Vertex(name = 'V_123',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_124 = Vertex(name = 'V_124',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_125 = Vertex(name = 'V_125',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_126 = Vertex(name = 'V_126',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_127 = Vertex(name = 'V_127',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_128 = Vertex(name = 'V_128',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_129 = Vertex(name = 'V_129',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_130 = Vertex(name = 'V_130',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_131 = Vertex(name = 'V_131',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_132 = Vertex(name = 'V_132',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_133 = Vertex(name = 'V_133',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_95})

V_134 = Vertex(name = 'V_134',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_96})

V_135 = Vertex(name = 'V_135',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_97})

V_136 = Vertex(name = 'V_136',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_98})

V_137 = Vertex(name = 'V_137',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_99})

V_138 = Vertex(name = 'V_138',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_100})

V_139 = Vertex(name = 'V_139',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_101})

V_140 = Vertex(name = 'V_140',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_102})

V_141 = Vertex(name = 'V_141',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_103})

V_142 = Vertex(name = 'V_142',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_209})

V_143 = Vertex(name = 'V_143',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_212})

V_144 = Vertex(name = 'V_144',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_215})

V_145 = Vertex(name = 'V_145',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_210})

V_146 = Vertex(name = 'V_146',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_213})

V_147 = Vertex(name = 'V_147',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_216})

V_148 = Vertex(name = 'V_148',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_211})

V_149 = Vertex(name = 'V_149',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_214})

V_150 = Vertex(name = 'V_150',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_217})

V_151 = Vertex(name = 'V_151',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_152 = Vertex(name = 'V_152',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_155 = Vertex(name = 'V_155',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_156 = Vertex(name = 'V_156',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_94})

V_157 = Vertex(name = 'V_157',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109})

V_158 = Vertex(name = 'V_158',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109})

V_159 = Vertex(name = 'V_159',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109})

V_160 = Vertex(name = 'V_160',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_109})

V_161 = Vertex(name = 'V_161',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_109})

V_162 = Vertex(name = 'V_162',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_109})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_120})

V_164 = Vertex(name = 'V_164',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_120})

V_165 = Vertex(name = 'V_165',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_120})

V_166 = Vertex(name = 'V_166',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_111})

V_167 = Vertex(name = 'V_167',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_111})

V_168 = Vertex(name = 'V_168',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_111})

