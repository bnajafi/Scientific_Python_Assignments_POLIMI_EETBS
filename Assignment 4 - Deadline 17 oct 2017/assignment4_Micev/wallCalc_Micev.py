def wallCalc_withParallel(layers_in_series,layers_in_paralel,fraction):
    Materials_library={"glassfiber_90mm":2.52,"stucco_25mm":0.037,"facebrick_100mm":0.075,"wood_25mm":0.22,
"woodstud_90mm":0.63,"woodstud_140mm":0.98,"plywood_13mm":0.11,"gypsum_13mm":0.079,"fiberboard_13mm":0.23,
"outsideSurface_winter":0.03,"outsideSurface_summer":0.044,"insideSurface":0.12,"wood_bevel":0.14,"common_brick_100mm":0.12,"roof":4.0}
    convection_resistances=["insideSurface","outsideSurface_winter"]
    layers1=layers_in_series+convection_resistances+["glassfiber_90mm"]
    layers2=layers_in_series+convection_resistances+["woodstud_90mm"]
    Rtot=0
    for anyLayer in layers1:
        RValue_layer=Materials_library[anyLayer]
        Rtot=Rtot+RValue_layer
    Rtot1=0
    for anyLayer in layers2:
        RValue_layer=Materials_library[anyLayer]
        Rtot1=Rtot1+RValue_layer   
    Utot=fraction/Rtot+(1-fraction)/Rtot1
    Rsum=1/Utot
    all_resistances=layers_in_series+layers_in_paralel+convection_resistances
    material=[]
    resistances=[]
    for anyLayer in all_resistances:
        material.append(Materials_library[anyLayer])
        resistances.append(anyLayer)
    library=dict(zip(resistances,material))
    return library, Rsum, Utot
   
def wallCalc_onlyinSeries(layers_series):
    Materials_library={"glassfiber_90mm":2.52,"stucco_25mm":0.037,"facebrick_100mm":0.075,"wood_50mm":0.44,
"woodstud_90mm":0.63,"woodstud_140mm":0.98,"plywood_13mm":0.11,"gypsum_13mm":0.079,"fiberboard_13mm":0.23,
"outsideSurface_winter":0.03,"outsideSurface_summer":0.044,"insideSurface":0.12,"wood_bevel":0.14,"common_brick_100mm":0.12,
"roof":4.0}
    Rtot=0
    for anyLayer in layers_series:
        RValue_layer=Materials_library[anyLayer]
        Rtot=Rtot+RValue_layer
    U=1/Rtot
    return U

