# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Wed 28 Feb 2024 16:32:32


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
               couplings = {(0,0,0):C.R2GC_83_85,(0,0,1):C.R2GC_83_86,(0,0,2):C.R2GC_83_87,(0,0,3):C.R2GC_83_88,(0,0,4):C.R2GC_83_89,(0,0,5):C.R2GC_83_90})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
               couplings = {(0,0,0):C.R2GC_82_79,(0,0,1):C.R2GC_82_80,(0,0,2):C.R2GC_82_81,(0,0,3):C.R2GC_82_82,(0,0,4):C.R2GC_82_83,(0,0,5):C.R2GC_82_84})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_155_35,(0,0,1):C.R2GC_155_36})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_92_99,(2,1,1):C.R2GC_165_44,(0,1,0):C.R2GC_92_99,(0,1,1):C.R2GC_165_44,(4,1,0):C.R2GC_90_96,(4,1,1):C.R2GC_90_97,(3,1,0):C.R2GC_90_96,(3,1,1):C.R2GC_90_97,(8,1,0):C.R2GC_164_41,(8,1,1):C.R2GC_91_98,(6,1,0):C.R2GC_168_48,(6,1,1):C.R2GC_168_49,(7,1,0):C.R2GC_169_50,(7,1,1):C.R2GC_169_51,(5,1,0):C.R2GC_90_96,(5,1,1):C.R2GC_90_97,(1,1,0):C.R2GC_90_96,(1,1,1):C.R2GC_90_97,(11,0,0):C.R2GC_94_101,(11,0,1):C.R2GC_103_3,(10,0,0):C.R2GC_94_101,(10,0,1):C.R2GC_103_3,(9,0,1):C.R2GC_93_100,(2,2,0):C.R2GC_92_99,(2,2,1):C.R2GC_165_44,(0,2,0):C.R2GC_92_99,(0,2,1):C.R2GC_165_44,(4,2,0):C.R2GC_90_96,(4,2,1):C.R2GC_90_97,(3,2,0):C.R2GC_90_96,(3,2,1):C.R2GC_90_97,(8,2,0):C.R2GC_164_41,(8,2,1):C.R2GC_167_47,(6,2,0):C.R2GC_166_45,(6,2,1):C.R2GC_166_46,(7,2,0):C.R2GC_169_50,(7,2,1):C.R2GC_96_103,(5,2,0):C.R2GC_90_96,(5,2,1):C.R2GC_90_97,(1,2,0):C.R2GC_90_96,(1,2,1):C.R2GC_90_97,(0,3,0):C.R2GC_92_99,(0,3,1):C.R2GC_165_44,(2,3,0):C.R2GC_92_99,(2,3,1):C.R2GC_165_44,(5,3,0):C.R2GC_90_96,(5,3,1):C.R2GC_90_97,(1,3,0):C.R2GC_90_96,(1,3,1):C.R2GC_90_97,(7,3,0):C.R2GC_165_43,(7,3,1):C.R2GC_165_44,(4,3,0):C.R2GC_90_96,(4,3,1):C.R2GC_90_97,(3,3,0):C.R2GC_90_96,(3,3,1):C.R2GC_90_97,(8,3,0):C.R2GC_164_41,(8,3,1):C.R2GC_164_42,(6,3,0):C.R2GC_168_48,(6,3,1):C.R2GC_95_102})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_122_17})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_135_24})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_143_28})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_128_21})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_152_33})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_179_56})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_105_6})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.H, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_110_11})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.a, P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_106_7})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_156_37})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.a, P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_162_38})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.g, P.g, P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sd] ] ],
                couplings = {(2,0,0):C.R2GC_163_39,(2,0,1):C.R2GC_163_40,(1,0,0):C.R2GC_163_39,(1,0,1):C.R2GC_163_40,(0,0,0):C.R2GC_103_3,(0,0,1):C.R2GC_103_4})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_107_8})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_108_9})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_170_52})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_109_10})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_113_12})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_113_12})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_113_12})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_132_23})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_140_27})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_149_32})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_175_54})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_176_55})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_153_34})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_25})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_180_57})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_144_29})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_181_58})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_19,(0,1,0):C.R2GC_127_20})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_126_19,(0,1,0):C.R2GC_127_20})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_19,(0,1,0):C.R2GC_127_20})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_120_15,(0,1,0):C.R2GC_121_16})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_120_15,(0,1,0):C.R2GC_121_16})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_120_15,(0,1,0):C.R2GC_121_16})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_174_53,(0,1,0):C.R2GC_117_13})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_125_18,(0,1,0):C.R2GC_117_13})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_148_31,(0,1,0):C.R2GC_117_13})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_22,(0,1,0):C.R2GC_117_13})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_139_26,(0,1,0):C.R2GC_117_13})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_119_14,(0,1,0):C.R2GC_117_13})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_145_30,(0,1,0):C.R2GC_104_5})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,2,4):C.R2GC_73_59,(0,0,0):C.R2GC_77_65,(0,0,2):C.R2GC_77_66,(0,0,3):C.R2GC_77_67,(0,0,5):C.R2GC_77_68,(0,0,6):C.R2GC_77_69,(0,0,7):C.R2GC_77_70,(0,1,1):C.R2GC_74_60})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_75_61,(0,0,1):C.R2GC_75_62})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_78_71,(0,0,1):C.R2GC_78_72})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_81_77,(0,0,1):C.R2GC_81_78})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_84_91,(0,0,1):C.R2GC_84_92,(0,0,2):C.R2GC_84_93,(0,0,3):C.R2GC_84_94,(0,0,4):C.R2GC_84_95})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_76_63,(0,0,1):C.R2GC_76_64})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_80_75,(1,0,1):C.R2GC_80_76,(0,1,0):C.R2GC_79_73,(0,1,1):C.R2GC_79_74})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_155_71,(0,1,1):C.UVGC_155_72,(0,1,2):C.UVGC_155_73,(0,1,3):C.UVGC_155_74,(0,1,4):C.UVGC_155_75,(0,1,5):C.UVGC_155_76,(0,1,6):C.UVGC_155_77,(0,1,7):C.UVGC_155_78,(0,1,8):C.UVGC_155_79,(0,0,3):C.UVGC_86_195,(0,3,4):C.UVGC_88_197,(0,2,6):C.UVGC_89_198})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.sd], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,1,5):C.UVGC_91_202,(2,1,6):C.UVGC_91_201,(0,1,5):C.UVGC_91_202,(0,1,6):C.UVGC_91_201,(4,1,5):C.UVGC_90_199,(4,1,6):C.UVGC_90_200,(3,1,5):C.UVGC_90_199,(3,1,6):C.UVGC_90_200,(8,1,5):C.UVGC_91_201,(8,1,6):C.UVGC_91_202,(6,1,0):C.UVGC_168_154,(6,1,3):C.UVGC_168_155,(6,1,4):C.UVGC_168_156,(6,1,5):C.UVGC_168_157,(6,1,6):C.UVGC_168_158,(6,1,7):C.UVGC_168_159,(6,1,8):C.UVGC_168_160,(6,1,9):C.UVGC_168_161,(6,1,10):C.UVGC_168_162,(7,1,0):C.UVGC_168_154,(7,1,3):C.UVGC_168_155,(7,1,4):C.UVGC_168_156,(7,1,5):C.UVGC_169_163,(7,1,6):C.UVGC_169_164,(7,1,7):C.UVGC_168_159,(7,1,8):C.UVGC_168_160,(7,1,9):C.UVGC_168_161,(7,1,10):C.UVGC_168_162,(5,1,5):C.UVGC_90_199,(5,1,6):C.UVGC_90_200,(1,1,5):C.UVGC_90_199,(1,1,6):C.UVGC_90_200,(11,0,5):C.UVGC_94_205,(11,0,6):C.UVGC_94_206,(10,0,5):C.UVGC_94_205,(10,0,6):C.UVGC_94_206,(9,0,5):C.UVGC_93_203,(9,0,6):C.UVGC_93_204,(2,2,5):C.UVGC_91_202,(2,2,6):C.UVGC_91_201,(0,2,5):C.UVGC_91_202,(0,2,6):C.UVGC_91_201,(4,2,5):C.UVGC_90_199,(4,2,6):C.UVGC_90_200,(3,2,5):C.UVGC_90_199,(3,2,6):C.UVGC_90_200,(8,2,0):C.UVGC_167_145,(8,2,3):C.UVGC_167_146,(8,2,4):C.UVGC_167_147,(8,2,5):C.UVGC_167_148,(8,2,6):C.UVGC_167_149,(8,2,7):C.UVGC_167_150,(8,2,8):C.UVGC_167_151,(8,2,9):C.UVGC_167_152,(8,2,10):C.UVGC_167_153,(6,2,0):C.UVGC_165_133,(6,2,3):C.UVGC_165_134,(6,2,4):C.UVGC_165_135,(6,2,5):C.UVGC_166_142,(6,2,6):C.UVGC_166_143,(6,2,7):C.UVGC_165_138,(6,2,8):C.UVGC_166_144,(6,2,9):C.UVGC_165_140,(6,2,10):C.UVGC_165_141,(7,2,1):C.UVGC_95_207,(7,2,5):C.UVGC_96_210,(7,2,6):C.UVGC_96_211,(5,2,5):C.UVGC_90_199,(5,2,6):C.UVGC_90_200,(1,2,5):C.UVGC_90_199,(1,2,6):C.UVGC_90_200,(0,3,5):C.UVGC_91_202,(0,3,6):C.UVGC_91_201,(2,3,5):C.UVGC_91_202,(2,3,6):C.UVGC_91_201,(5,3,5):C.UVGC_90_199,(5,3,6):C.UVGC_90_200,(1,3,5):C.UVGC_90_199,(1,3,6):C.UVGC_90_200,(7,3,0):C.UVGC_165_133,(7,3,3):C.UVGC_165_134,(7,3,4):C.UVGC_165_135,(7,3,5):C.UVGC_165_136,(7,3,6):C.UVGC_165_137,(7,3,7):C.UVGC_165_138,(7,3,8):C.UVGC_165_139,(7,3,9):C.UVGC_165_140,(7,3,10):C.UVGC_165_141,(4,3,5):C.UVGC_90_199,(4,3,6):C.UVGC_90_200,(3,3,5):C.UVGC_90_199,(3,3,6):C.UVGC_90_200,(8,3,0):C.UVGC_164_124,(8,3,3):C.UVGC_164_125,(8,3,4):C.UVGC_164_126,(8,3,5):C.UVGC_164_127,(8,3,6):C.UVGC_164_128,(8,3,7):C.UVGC_164_129,(8,3,8):C.UVGC_164_130,(8,3,9):C.UVGC_164_131,(8,3,10):C.UVGC_164_132,(6,3,2):C.UVGC_95_207,(6,3,5):C.UVGC_95_208,(6,3,6):C.UVGC_93_203,(6,3,8):C.UVGC_95_209})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_122_18})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_135_33})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_143_45})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_128_24})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_152_58})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_179_187})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_105_6})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.H, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_110_11})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.a, P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_106_7})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_156_80,(0,0,1):C.UVGC_156_81,(0,0,2):C.UVGC_156_82,(0,0,3):C.UVGC_156_83,(0,0,4):C.UVGC_156_84,(0,0,6):C.UVGC_156_85,(0,0,7):C.UVGC_156_86,(0,0,8):C.UVGC_156_87,(0,0,9):C.UVGC_156_88,(0,0,5):C.UVGC_156_89})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.a, P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_162_104,(0,0,1):C.UVGC_162_105,(0,0,2):C.UVGC_162_106,(0,0,3):C.UVGC_162_107,(0,0,4):C.UVGC_162_108,(0,0,6):C.UVGC_162_109,(0,0,7):C.UVGC_162_110,(0,0,8):C.UVGC_162_111,(0,0,9):C.UVGC_162_112,(0,0,5):C.UVGC_162_113})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.g, P.g, P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,0):C.UVGC_163_114,(2,0,1):C.UVGC_163_115,(2,0,2):C.UVGC_163_116,(2,0,3):C.UVGC_163_117,(2,0,4):C.UVGC_163_118,(2,0,6):C.UVGC_163_119,(2,0,7):C.UVGC_163_120,(2,0,8):C.UVGC_163_121,(2,0,9):C.UVGC_163_122,(2,0,5):C.UVGC_163_123,(1,0,0):C.UVGC_163_114,(1,0,1):C.UVGC_163_115,(1,0,2):C.UVGC_163_116,(1,0,3):C.UVGC_163_117,(1,0,4):C.UVGC_163_118,(1,0,6):C.UVGC_163_119,(1,0,7):C.UVGC_163_120,(1,0,8):C.UVGC_163_121,(1,0,9):C.UVGC_163_122,(1,0,5):C.UVGC_163_123,(0,0,3):C.UVGC_103_3,(0,0,5):C.UVGC_103_4})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_107_8})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_108_9})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_170_165,(0,0,1):C.UVGC_170_166,(0,0,2):C.UVGC_170_167,(0,0,3):C.UVGC_170_168,(0,0,4):C.UVGC_170_169,(0,0,6):C.UVGC_170_170,(0,0,7):C.UVGC_170_171,(0,0,8):C.UVGC_170_172,(0,0,9):C.UVGC_170_173,(0,0,5):C.UVGC_170_174})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_109_10})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_113_12,(0,1,0):C.UVGC_124_20})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_113_12,(0,1,0):C.UVGC_147_51})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_113_12,(0,1,0):C.UVGC_172_176})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2,(0,1,0):C.UVGC_118_14})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2,(0,1,0):C.UVGC_130_26})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_101_2,(0,1,0):C.UVGC_138_38})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,2):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,1):C.UVGC_157_91,(0,1,3):C.UVGC_157_92,(0,1,4):C.UVGC_157_93,(0,1,5):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,2):C.UVGC_158_100})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,1):C.UVGC_157_91,(0,1,2):C.UVGC_157_92,(0,1,3):C.UVGC_157_93,(0,1,4):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,5):C.UVGC_161_103})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,1):C.UVGC_157_91,(0,1,2):C.UVGC_157_92,(0,1,3):C.UVGC_157_93,(0,1,4):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,5):C.UVGC_173_177})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,1):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,2):C.UVGC_157_91,(0,1,3):C.UVGC_157_92,(0,1,4):C.UVGC_157_93,(0,1,5):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,1):C.UVGC_157_99})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,3):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,1):C.UVGC_157_91,(0,1,2):C.UVGC_157_92,(0,1,4):C.UVGC_157_93,(0,1,5):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,3):C.UVGC_159_101})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_100_1,(0,1,0):C.UVGC_157_90,(0,1,1):C.UVGC_157_91,(0,1,2):C.UVGC_157_92,(0,1,3):C.UVGC_157_93,(0,1,4):C.UVGC_157_94,(0,1,6):C.UVGC_157_95,(0,1,7):C.UVGC_157_96,(0,1,8):C.UVGC_157_97,(0,1,9):C.UVGC_157_98,(0,1,5):C.UVGC_160_102})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_132_28,(0,0,2):C.UVGC_132_29,(0,0,0):C.UVGC_132_30})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_140_40,(0,0,2):C.UVGC_140_41,(0,0,1):C.UVGC_140_42})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_149_53,(0,0,2):C.UVGC_149_54,(0,0,1):C.UVGC_149_55})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_175_179,(0,0,2):C.UVGC_175_180,(0,0,1):C.UVGC_175_181})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_176_182,(0,0,2):C.UVGC_176_183,(0,0,1):C.UVGC_176_184})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_153_59,(0,0,2):C.UVGC_153_60,(0,0,1):C.UVGC_153_61})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_136_34,(0,0,2):C.UVGC_136_35,(0,0,0):C.UVGC_136_36})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_180_188,(0,0,2):C.UVGC_180_189,(0,0,1):C.UVGC_180_190})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_144_46,(0,0,2):C.UVGC_144_47,(0,0,1):C.UVGC_144_48})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_181_191,(0,0,2):C.UVGC_181_192,(0,0,1):C.UVGC_181_193})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_126_22,(0,1,0):C.UVGC_127_23})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_150_56,(0,1,0):C.UVGC_151_57})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_177_185,(0,1,0):C.UVGC_178_186})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_120_16,(0,1,0):C.UVGC_121_17})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_133_31,(0,1,0):C.UVGC_134_32})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_141_43,(0,1,0):C.UVGC_142_44})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_174_178,(0,1,0):C.UVGC_171_175})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_125_21,(0,1,0):C.UVGC_123_19})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_148_52,(0,1,0):C.UVGC_146_50})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_131_27,(0,1,0):C.UVGC_129_25})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_139_39,(0,1,0):C.UVGC_137_37})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_119_15,(0,1,0):C.UVGC_117_13})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.sd__tilde__, P.sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sd] ] ],
                 couplings = {(0,0,0):C.UVGC_145_49,(0,1,0):C.UVGC_104_5})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_154_62,(0,0,1):C.UVGC_154_63,(0,0,2):C.UVGC_154_64,(0,0,3):C.UVGC_154_65,(0,0,4):C.UVGC_154_66,(0,0,5):C.UVGC_154_67,(0,0,6):C.UVGC_154_68,(0,0,7):C.UVGC_154_69,(0,0,8):C.UVGC_154_70,(0,1,3):C.UVGC_85_194,(0,2,4):C.UVGC_87_196})

