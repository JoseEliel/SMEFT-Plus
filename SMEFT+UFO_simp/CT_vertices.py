# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Mon 11 Dec 2023 22:19:33


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
               couplings = {(0,0,0):C.R2GC_228_27,(0,0,1):C.R2GC_228_28,(0,0,2):C.R2GC_228_29,(0,0,3):C.R2GC_228_30,(0,0,4):C.R2GC_228_31,(0,0,5):C.R2GC_228_32})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
               couplings = {(0,0,0):C.R2GC_227_21,(0,0,1):C.R2GC_227_22,(0,0,2):C.R2GC_227_23,(0,0,3):C.R2GC_227_24,(0,0,4):C.R2GC_227_25,(0,0,5):C.R2GC_227_26})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_302_85,(0,0,1):C.R2GC_302_86})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_237_42,(2,1,1):C.R2GC_237_43,(0,1,0):C.R2GC_237_42,(0,1,1):C.R2GC_237_43,(4,1,0):C.R2GC_235_38,(4,1,1):C.R2GC_235_39,(3,1,0):C.R2GC_235_38,(3,1,1):C.R2GC_235_39,(8,1,0):C.R2GC_236_40,(8,1,1):C.R2GC_236_41,(6,1,0):C.R2GC_240_47,(6,1,1):C.R2GC_315_96,(7,1,0):C.R2GC_241_49,(7,1,1):C.R2GC_316_97,(5,1,0):C.R2GC_235_38,(5,1,1):C.R2GC_235_39,(1,1,0):C.R2GC_235_38,(1,1,1):C.R2GC_235_39,(11,0,0):C.R2GC_239_45,(11,0,1):C.R2GC_239_46,(10,0,0):C.R2GC_239_45,(10,0,1):C.R2GC_239_46,(9,0,1):C.R2GC_238_44,(2,2,0):C.R2GC_237_42,(2,2,1):C.R2GC_237_43,(0,2,0):C.R2GC_237_42,(0,2,1):C.R2GC_237_43,(4,2,0):C.R2GC_235_38,(4,2,1):C.R2GC_235_39,(3,2,0):C.R2GC_235_38,(3,2,1):C.R2GC_235_39,(8,2,0):C.R2GC_236_40,(8,2,1):C.R2GC_314_95,(6,2,0):C.R2GC_313_93,(6,2,1):C.R2GC_313_94,(7,2,0):C.R2GC_241_49,(7,2,1):C.R2GC_241_50,(5,2,0):C.R2GC_235_38,(5,2,1):C.R2GC_235_39,(1,2,0):C.R2GC_235_38,(1,2,1):C.R2GC_235_39,(0,3,0):C.R2GC_237_42,(0,3,1):C.R2GC_237_43,(2,3,0):C.R2GC_237_42,(2,3,1):C.R2GC_237_43,(5,3,0):C.R2GC_235_38,(5,3,1):C.R2GC_235_39,(1,3,0):C.R2GC_235_38,(1,3,1):C.R2GC_235_39,(7,3,0):C.R2GC_312_92,(7,3,1):C.R2GC_237_43,(4,3,0):C.R2GC_235_38,(4,3,1):C.R2GC_235_39,(3,3,0):C.R2GC_235_38,(3,3,1):C.R2GC_235_39,(8,3,0):C.R2GC_236_40,(8,3,1):C.R2GC_311_91,(6,3,0):C.R2GC_240_47,(6,3,1):C.R2GC_240_48})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_282_74})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_290_78})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_269_68})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_326_102})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_275_71})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_299_83})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_250_56})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.H, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1, L.SSS4, L.SSS5 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_257_63,(0,1,0):C.R2GC_256_62,(0,2,0):C.R2GC_255_61})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.g, P.g, P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sd] ] ],
                couplings = {(2,0,0):C.R2GC_310_89,(2,0,1):C.R2GC_310_90,(1,0,0):C.R2GC_310_89,(1,0,1):C.R2GC_310_90,(0,0,0):C.R2GC_239_46,(0,0,1):C.R2GC_248_54})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.a, P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_251_57})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_303_87})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.a, P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_309_88})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_252_58})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_253_59})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_317_98})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_254_60})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_244_53})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_244_53})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_244_53})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_242_51})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_242_51})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_242_51})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_243_52})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_322_100})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_323_101})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_279_73})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_287_77})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_296_82})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_327_103})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_283_75})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_328_104})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_291_79})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_300_84})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_273_70,(0,1,0):C.R2GC_268_67})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_273_70,(0,1,0):C.R2GC_268_67})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_273_70,(0,1,0):C.R2GC_268_67})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_66,(0,1,0):C.R2GC_268_67})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_267_66,(0,1,0):C.R2GC_268_67})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_66,(0,1,0):C.R2GC_268_67})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_321_99,(0,1,0):C.R2GC_264_64})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_272_69,(0,1,0):C.R2GC_264_64})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_295_81,(0,1,0):C.R2GC_264_64})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_278_72,(0,1,0):C.R2GC_264_64})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_286_76,(0,1,0):C.R2GC_264_64})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_266_65,(0,1,0):C.R2GC_264_64})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.R2GC_292_80,(0,1,0):C.R2GC_249_55})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,2,4):C.R2GC_218_1,(0,0,0):C.R2GC_222_7,(0,0,2):C.R2GC_222_8,(0,0,3):C.R2GC_222_9,(0,0,5):C.R2GC_222_10,(0,0,6):C.R2GC_222_11,(0,0,7):C.R2GC_222_12,(0,1,1):C.R2GC_219_2})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_220_3,(0,0,1):C.R2GC_220_4})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_223_13,(0,0,1):C.R2GC_223_14})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_226_19,(0,0,1):C.R2GC_226_20})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_229_33,(0,0,1):C.R2GC_229_34,(0,0,2):C.R2GC_229_35,(0,0,3):C.R2GC_229_36,(0,0,4):C.R2GC_229_37})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_221_5,(0,0,1):C.R2GC_221_6})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_225_17,(1,0,1):C.R2GC_225_18,(0,1,0):C.R2GC_224_15,(0,1,1):C.R2GC_224_16})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_302_91,(0,1,1):C.UVGC_302_92,(0,1,2):C.UVGC_302_93,(0,1,3):C.UVGC_302_94,(0,1,4):C.UVGC_302_95,(0,1,5):C.UVGC_302_96,(0,1,6):C.UVGC_302_97,(0,1,7):C.UVGC_302_98,(0,1,8):C.UVGC_302_99,(0,0,3):C.UVGC_231_2,(0,3,4):C.UVGC_233_4,(0,2,6):C.UVGC_234_5})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.sd], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,1,5):C.UVGC_236_9,(2,1,6):C.UVGC_236_8,(0,1,5):C.UVGC_236_9,(0,1,6):C.UVGC_236_8,(4,1,5):C.UVGC_235_6,(4,1,6):C.UVGC_235_7,(3,1,5):C.UVGC_235_6,(3,1,6):C.UVGC_235_7,(8,1,5):C.UVGC_236_8,(8,1,6):C.UVGC_236_9,(6,1,0):C.UVGC_315_174,(6,1,3):C.UVGC_315_175,(6,1,4):C.UVGC_315_176,(6,1,5):C.UVGC_315_177,(6,1,6):C.UVGC_315_178,(6,1,7):C.UVGC_315_179,(6,1,8):C.UVGC_315_180,(6,1,9):C.UVGC_315_181,(6,1,10):C.UVGC_315_182,(7,1,0):C.UVGC_315_174,(7,1,3):C.UVGC_315_175,(7,1,4):C.UVGC_315_176,(7,1,5):C.UVGC_316_183,(7,1,6):C.UVGC_316_184,(7,1,7):C.UVGC_315_179,(7,1,8):C.UVGC_315_180,(7,1,9):C.UVGC_315_181,(7,1,10):C.UVGC_315_182,(5,1,5):C.UVGC_235_6,(5,1,6):C.UVGC_235_7,(1,1,5):C.UVGC_235_6,(1,1,6):C.UVGC_235_7,(11,0,5):C.UVGC_239_12,(11,0,6):C.UVGC_239_13,(10,0,5):C.UVGC_239_12,(10,0,6):C.UVGC_239_13,(9,0,5):C.UVGC_238_10,(9,0,6):C.UVGC_238_11,(2,2,5):C.UVGC_236_9,(2,2,6):C.UVGC_236_8,(0,2,5):C.UVGC_236_9,(0,2,6):C.UVGC_236_8,(4,2,5):C.UVGC_235_6,(4,2,6):C.UVGC_235_7,(3,2,5):C.UVGC_235_6,(3,2,6):C.UVGC_235_7,(8,2,0):C.UVGC_314_165,(8,2,3):C.UVGC_314_166,(8,2,4):C.UVGC_314_167,(8,2,5):C.UVGC_314_168,(8,2,6):C.UVGC_314_169,(8,2,7):C.UVGC_314_170,(8,2,8):C.UVGC_314_171,(8,2,9):C.UVGC_314_172,(8,2,10):C.UVGC_314_173,(6,2,0):C.UVGC_312_153,(6,2,3):C.UVGC_312_154,(6,2,4):C.UVGC_312_155,(6,2,5):C.UVGC_313_162,(6,2,6):C.UVGC_313_163,(6,2,7):C.UVGC_312_158,(6,2,8):C.UVGC_313_164,(6,2,9):C.UVGC_312_160,(6,2,10):C.UVGC_312_161,(7,2,1):C.UVGC_240_14,(7,2,5):C.UVGC_241_17,(7,2,6):C.UVGC_241_18,(5,2,5):C.UVGC_235_6,(5,2,6):C.UVGC_235_7,(1,2,5):C.UVGC_235_6,(1,2,6):C.UVGC_235_7,(0,3,5):C.UVGC_236_9,(0,3,6):C.UVGC_236_8,(2,3,5):C.UVGC_236_9,(2,3,6):C.UVGC_236_8,(5,3,5):C.UVGC_235_6,(5,3,6):C.UVGC_235_7,(1,3,5):C.UVGC_235_6,(1,3,6):C.UVGC_235_7,(7,3,0):C.UVGC_312_153,(7,3,3):C.UVGC_312_154,(7,3,4):C.UVGC_312_155,(7,3,5):C.UVGC_312_156,(7,3,6):C.UVGC_312_157,(7,3,7):C.UVGC_312_158,(7,3,8):C.UVGC_312_159,(7,3,9):C.UVGC_312_160,(7,3,10):C.UVGC_312_161,(4,3,5):C.UVGC_235_6,(4,3,6):C.UVGC_235_7,(3,3,5):C.UVGC_235_6,(3,3,6):C.UVGC_235_7,(8,3,0):C.UVGC_311_144,(8,3,3):C.UVGC_311_145,(8,3,4):C.UVGC_311_146,(8,3,5):C.UVGC_311_147,(8,3,6):C.UVGC_311_148,(8,3,7):C.UVGC_311_149,(8,3,8):C.UVGC_311_150,(8,3,9):C.UVGC_311_151,(8,3,10):C.UVGC_311_152,(6,3,2):C.UVGC_240_14,(6,3,5):C.UVGC_240_15,(6,3,6):C.UVGC_238_10,(6,3,8):C.UVGC_240_16})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_282_53})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_290_65})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_269_38})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_326_207})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_275_44})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_299_78})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_250_25})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.H, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1, L.SSS4, L.SSS5 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_257_32,(0,1,0):C.UVGC_256_31,(0,2,0):C.UVGC_255_30})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.g, P.g, P.sd__tilde__, P.sd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,0):C.UVGC_310_134,(2,0,1):C.UVGC_310_135,(2,0,2):C.UVGC_310_136,(2,0,3):C.UVGC_310_137,(2,0,4):C.UVGC_310_138,(2,0,6):C.UVGC_310_139,(2,0,7):C.UVGC_310_140,(2,0,8):C.UVGC_310_141,(2,0,9):C.UVGC_310_142,(2,0,5):C.UVGC_310_143,(1,0,0):C.UVGC_310_134,(1,0,1):C.UVGC_310_135,(1,0,2):C.UVGC_310_136,(1,0,3):C.UVGC_310_137,(1,0,4):C.UVGC_310_138,(1,0,6):C.UVGC_310_139,(1,0,7):C.UVGC_310_140,(1,0,8):C.UVGC_310_141,(1,0,9):C.UVGC_310_142,(1,0,5):C.UVGC_310_143,(0,0,3):C.UVGC_248_22,(0,0,5):C.UVGC_248_23})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.a, P.a, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_251_26})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_303_100,(0,0,1):C.UVGC_303_101,(0,0,2):C.UVGC_303_102,(0,0,3):C.UVGC_303_103,(0,0,4):C.UVGC_303_104,(0,0,6):C.UVGC_303_105,(0,0,7):C.UVGC_303_106,(0,0,8):C.UVGC_303_107,(0,0,9):C.UVGC_303_108,(0,0,5):C.UVGC_303_109})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.a, P.g, P.sd__tilde__, P.sd ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_309_124,(0,0,1):C.UVGC_309_125,(0,0,2):C.UVGC_309_126,(0,0,3):C.UVGC_309_127,(0,0,4):C.UVGC_309_128,(0,0,6):C.UVGC_309_129,(0,0,7):C.UVGC_309_130,(0,0,8):C.UVGC_309_131,(0,0,9):C.UVGC_309_132,(0,0,5):C.UVGC_309_133})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_252_27})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.a, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_253_28})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.g, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sd] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_317_185,(0,0,1):C.UVGC_317_186,(0,0,2):C.UVGC_317_187,(0,0,3):C.UVGC_317_188,(0,0,4):C.UVGC_317_189,(0,0,6):C.UVGC_317_190,(0,0,7):C.UVGC_317_191,(0,0,8):C.UVGC_317_192,(0,0,9):C.UVGC_317_193,(0,0,5):C.UVGC_317_194})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.Z, P.Z, P.sd__tilde__, P.sd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.sd] ] ],
                couplings = {(0,0,0):C.UVGC_254_29})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_244_21,(0,1,0):C.UVGC_319_196})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_244_21,(0,1,0):C.UVGC_271_40})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_244_21,(0,1,0):C.UVGC_294_71})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_242_19,(0,1,0):C.UVGC_277_46})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_242_19,(0,1,0):C.UVGC_285_58})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_242_19,(0,1,0):C.UVGC_265_34})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,1):C.UVGC_304_111,(0,1,2):C.UVGC_304_112,(0,1,3):C.UVGC_304_113,(0,1,4):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,5):C.UVGC_320_197})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,2):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,1):C.UVGC_304_111,(0,1,3):C.UVGC_304_112,(0,1,4):C.UVGC_304_113,(0,1,5):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,2):C.UVGC_305_120})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,1):C.UVGC_304_111,(0,1,2):C.UVGC_304_112,(0,1,3):C.UVGC_304_113,(0,1,4):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,5):C.UVGC_308_123})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,3):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,1):C.UVGC_304_111,(0,1,2):C.UVGC_304_112,(0,1,4):C.UVGC_304_113,(0,1,5):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,3):C.UVGC_306_121})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,5):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,1):C.UVGC_304_111,(0,1,2):C.UVGC_304_112,(0,1,3):C.UVGC_304_113,(0,1,4):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,5):C.UVGC_307_122})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,1):C.UVGC_243_20,(0,1,0):C.UVGC_304_110,(0,1,2):C.UVGC_304_111,(0,1,3):C.UVGC_304_112,(0,1,4):C.UVGC_304_113,(0,1,5):C.UVGC_304_114,(0,1,6):C.UVGC_304_115,(0,1,7):C.UVGC_304_116,(0,1,8):C.UVGC_304_117,(0,1,9):C.UVGC_304_118,(0,1,1):C.UVGC_304_119})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_322_199,(0,0,2):C.UVGC_322_200,(0,0,1):C.UVGC_322_201})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_323_202,(0,0,2):C.UVGC_323_203,(0,0,1):C.UVGC_323_204})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_279_48,(0,0,2):C.UVGC_279_49,(0,0,0):C.UVGC_279_50})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_287_60,(0,0,2):C.UVGC_287_61,(0,0,1):C.UVGC_287_62})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_296_73,(0,0,2):C.UVGC_296_74,(0,0,1):C.UVGC_296_75})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_327_208,(0,0,2):C.UVGC_327_209,(0,0,1):C.UVGC_327_210})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_283_54,(0,0,2):C.UVGC_283_55,(0,0,0):C.UVGC_283_56})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_328_211,(0,0,2):C.UVGC_328_212,(0,0,1):C.UVGC_328_213})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_291_66,(0,0,2):C.UVGC_291_67,(0,0,1):C.UVGC_291_68})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_300_79,(0,0,2):C.UVGC_300_80,(0,0,1):C.UVGC_300_81})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_324_205,(0,1,0):C.UVGC_325_206})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_273_42,(0,1,0):C.UVGC_274_43})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_297_76,(0,1,0):C.UVGC_298_77})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_280_51,(0,1,0):C.UVGC_281_52})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_288_63,(0,1,0):C.UVGC_289_64})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_267_36,(0,1,0):C.UVGC_268_37})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_321_198,(0,1,0):C.UVGC_318_195})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_41,(0,1,0):C.UVGC_270_39})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_295_72,(0,1,0):C.UVGC_293_70})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_278_47,(0,1,0):C.UVGC_276_45})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_286_59,(0,1,0):C.UVGC_284_57})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_266_35,(0,1,0):C.UVGC_264_33})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.sd__tilde__, P.sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sd] ] ],
                 couplings = {(0,0,0):C.UVGC_292_69,(0,1,0):C.UVGC_249_24})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.sd] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_301_82,(0,0,1):C.UVGC_301_83,(0,0,2):C.UVGC_301_84,(0,0,3):C.UVGC_301_85,(0,0,4):C.UVGC_301_86,(0,0,5):C.UVGC_301_87,(0,0,6):C.UVGC_301_88,(0,0,7):C.UVGC_301_89,(0,0,8):C.UVGC_301_90,(0,1,3):C.UVGC_230_1,(0,2,4):C.UVGC_232_3})

