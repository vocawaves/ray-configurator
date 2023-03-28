setting = {
    'MAIN_LIGHT_ENABLE': {
        0: "None",
        1: "Default",
        2: "Sun radience via solar zenith angle"
    },
    'SHADOW_QUALITY': {
        0: "Disabled",
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Ultra",
        5: "Extreme"
    },
    'IBL_QUALITY': {
        1: "Enabled",
        2: "Enabled w/ UV flip"
    },
    "IBL_SKIN_COLOR_BALANCE": {
        0: "Disabled",
        1: "Enabled",
    },
    'FOG_ENABLE': {
        0: "Disabled",
        1: "Enabled"
    },
    'SSAO_QUALITY': {
        0: "Disabled",
        1: "8 samples",
        2: "12 samples",
        3: "16 samples",
        4: "8 samples (SSDO)",
        5: "12 samples (SSDO)",
        6: "16 samples (SSDO)",
    },
    'SSR_QUALITY': {
        0: "Disabled",
        1: "32 samples",
        2: "64 samples",
        3: "128 samples",
    },
    'SSSS_QUALITY': {
        0: "Disabled",
        1: "MMD",
        2: "Human",
    },
    'HDR_ENABLE': {
        0: "Disabled",
        1: "Enabled",
    },
    'HDR_BLOOM_MODE': {
        0: "None",
        1: "Inf",
        2: "Saturate",
        3: "Luminance",
    },
    'HDR_FLARE_MODE': {
        0: "None",
        1: "Blue",
        2: "Orange"
    },
    'HDR_STAR_MODE': {
        0: "Disabled",
        1: "Anamorphic Lens Flares",
        2: "Glare Star"
    },
    'HDR_TONEMAP_OPERATOR': {
        0: "Linear",
        1: "ACES-sRGB",
        2: "ACES-Rec709",
        3: "ACES-Rec2020",
        4: "Uncharted2",
        5: "Filmic"
    },
    'AA_QUALITY': {
        0: "Disabled",
        1: "FXAA",
        2: "SMAAx1 (Medium)",
        3: "SMAAx1 (High)",
        4: "SMAAx2 (Medium)",
        5: "SMAAx2 (High)",
    },
    "AA_GBUFFER_FILTER_QUALITY": {
        0: "Disabled",
        1: "Enabled",
    },
    'LIGHTMODEL_BRDF': {
        0: "BurleyBDRF + GGX BRDF",
        1: "BurleyBDRF + GGX BRDF + ShadingMaterialID"
    }
}

name = {
    'MAIN_LIGHT_ENABLE': 'Main Light',
    'SHADOW_QUALITY': 'Shadow Quality',
    'IBL_QUALITY': 'IBL Quality',
    'IBL_SKIN_COLOR_BALANCE': 'Skin Balance',
    'FOG_ENABLE': 'Fog',
    'SSAO_QUALITY': 'SSAO Quality',
    'SSR_QUALITY': 'SSR Quality',
    'SSSS_QUALITY': 'SSSS Quality',
    'HDR_ENABLE': 'HDR',
    'HDR_BLOOM_MODE': 'HDR Bloom Mode',
    'HDR_FLARE_MODE': 'HDR Flare Mode',
    'HDR_STAR_MODE': 'HDR Star Mode',
    'HDR_TONEMAP_OPERATOR': 'HDR Tonemap Operator',
    'AA_QUALITY': 'Anti-Aliasing',
    'AA_GBUFFER_FILTER_QUALITY': 'GBuffer Filter',
    'LIGHTMODEL_BRDF': 'Lightmodel BRDF',
}

category = {
    'Lighting': ['MAIN_LIGHT_ENABLE', 'IBL_QUALITY', 'IBL_SKIN_COLOR_BALANCE', 'FOG_ENABLE'],
    'Shadows': ['SHADOW_QUALITY'],
    'Ambient Occlusion': ['SSAO_QUALITY'],
    'Screen Space Reflection': ['SSR_QUALITY'],
    'Screen Space Subsurface Scattering': ['SSSS_QUALITY'],
    'HDR': ['HDR_ENABLE', 'HDR_BLOOM_MODE', 'HDR_FLARE_MODE', 'HDR_STAR_MODE', 'HDR_TONEMAP_OPERATOR'],
    'Anti-Aliasing': ['AA_QUALITY', 'AA_GBUFFER_FILTER_QUALITY'],
    'Lightmodel': ['LIGHTMODEL_BRDF'],
}

inputs = {
    'MAIN_LIGHT_ENABLE': 'checkbox',
    'SHADOW_QUALITY': 'dropdown',
    'IBL_QUALITY': 'dropdown',
    'IBL_SKIN_COLOR_BALANCE': 'checkbox',
    'FOG_ENABLE': 'checkbox',
    'SSAO_QUALITY': 'dropdown',
    'SSR_QUALITY': 'dropdown',
    'SSSS_QUALITY': 'dropdown',
    'HDR_ENABLE': 'checkbox',
    'HDR_BLOOM_MODE': 'dropdown',
    'HDR_FLARE_MODE': 'dropdown',
    'HDR_STAR_MODE': 'dropdown',
    'HDR_TONEMAP_OPERATOR': 'dropdown',
    'AA_QUALITY': 'dropdown',
    'AA_GBUFFER_FILTER_QUALITY': 'checkbox',
    'LIGHTMODEL_BRDF': 'dropdown',
}

defaults = {
    'MAIN_LIGHT_ENABLE': 1,
    'SHADOW_QUALITY': 3,
    'IBL_QUALITY': 1,
    'IBL_SKIN_COLOR_BALANCE': 0,
    'FOG_ENABLE': 0,
    'SSAO_QUALITY': 5,
    'SSR_QUALITY': 0,
    'SSSS_QUALITY': 1,
    'HDR_ENABLE': 1,
    'HDR_BLOOM_MODE': 2,
    'HDR_FLARE_MODE': 0,
    'HDR_STAR_MODE': 0,
    'HDR_TONEMAP_OPERATOR': 1,
    'AA_QUALITY': 1,
    'AA_GBUFFER_FILTER_QUALITY': 1,
    'LIGHTMODEL_BRDF': 1,
}

description = {
    'MAIN_LIGHT_ENABLE': 'Enable main light',
    'SHADOW_QUALITY': 'Shadow quality',
    'IBL_QUALITY': 'IBL quality',
    'IBL_SKIN_COLOR_BALANCE': 'Skin color balance',
    'FOG_ENABLE': 'Enable fog',
    'SSAO_QUALITY': 'SSAO quality',
    'SSR_QUALITY': 'SSR quality',
    'SSSS_QUALITY': 'SSSS quality',
    'HDR_ENABLE': 'Enable HDR',
    'HDR_BLOOM_MODE': 'HDR bloom mode',
    'HDR_FLARE_MODE': 'HDR flare mode',
    'HDR_STAR_MODE': 'HDR star mode',
    'HDR_TONEMAP_OPERATOR': 'HDR tonemap operator',
    'AA_QUALITY': 'Anti-aliasing quality',
    'AA_GBUFFER_FILTER_QUALITY': 'GBuffer filter',
    'LIGHTMODEL_BRDF': 'Lightmodel BRDF',
}
