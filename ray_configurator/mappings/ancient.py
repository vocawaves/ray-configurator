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

presets = {
    'Default': defaults,
    'Low': {
        'MAIN_LIGHT_ENABLE': 1,
        'SHADOW_QUALITY': 0,
        'IBL_QUALITY': 0,
        'IBL_SKIN_COLOR_BALANCE': 0,
        'FOG_ENABLE': 0,
        'SSAO_QUALITY': 0,
        'SSR_QUALITY': 0,
        'SSSS_QUALITY': 0,
        'HDR_ENABLE': 1,
        'HDR_BLOOM_MODE': 0,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 0,
        'AA_QUALITY': 0,
        'AA_GBUFFER_FILTER_QUALITY': 0,
        'LIGHTMODEL_BRDF': 0,
    },
    'Medium': {
        'MAIN_LIGHT_ENABLE': 1,
        'SHADOW_QUALITY': 1,
        'IBL_QUALITY': 1,
        'IBL_SKIN_COLOR_BALANCE': 0,
        'FOG_ENABLE': 0,
        'SSAO_QUALITY': 1,
        'SSR_QUALITY': 0,
        'SSSS_QUALITY': 1,
        'HDR_ENABLE': 1,
        'HDR_BLOOM_MODE': 1,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 1,
        'AA_QUALITY': 1,
        'AA_GBUFFER_FILTER_QUALITY': 1,
        'LIGHTMODEL_BRDF': 1,
    },
    'High': {
        'MAIN_LIGHT_ENABLE': 1,
        'SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'IBL_SKIN_COLOR_BALANCE': 0,
        'FOG_ENABLE': 0,
        'SSAO_QUALITY': 5,
        'SSR_QUALITY': 1,
        'SSSS_QUALITY': 1,
        'HDR_ENABLE': 1,
        'HDR_BLOOM_MODE': 2,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 1,
        'AA_QUALITY': 1,
        'AA_GBUFFER_FILTER_QUALITY': 1,
        'LIGHTMODEL_BRDF': 1,
    },
    'Ultra': {
        'MAIN_LIGHT_ENABLE': 1,
        'SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'IBL_SKIN_COLOR_BALANCE': 0,
        'FOG_ENABLE': 0,
        'SSAO_QUALITY': 5,
        'SSR_QUALITY': 1,
        'SSSS_QUALITY': 1,
        'HDR_ENABLE': 1,
        'HDR_BLOOM_MODE': 2,
        'HDR_FLARE_MODE': 1,
        'HDR_STAR_MODE': 1,
        'HDR_TONEMAP_OPERATOR': 1,
        'AA_QUALITY': 1,
        'AA_GBUFFER_FILTER_QUALITY': 1,
        'LIGHTMODEL_BRDF': 1,
    },
    'Extreme': {
        'MAIN_LIGHT_ENABLE': 1,
        'SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'IBL_SKIN_COLOR_BALANCE': 0,
        'FOG_ENABLE': 0,
        'SSAO_QUALITY': 5,
        'SSR_QUALITY': 1,
        'SSSS_QUALITY': 1,
        'HDR_ENABLE': 1,
        'HDR_BLOOM_MODE': 2,
        'HDR_FLARE_MODE': 1,
        'HDR_STAR_MODE': 1,
        'HDR_TONEMAP_OPERATOR': 1,
        'AA_QUALITY': 1,
        'AA_GBUFFER_FILTER_QUALITY': 1,
        'LIGHTMODEL_BRDF': 1,
    },
    'Custom': defaults,
}

# language

import importlib

language = importlib.import_module('mappings.languages.english')

name = language.name_ancient
description = language.description_ancient

def set_language(lang):
    global name
    global description
    language = importlib.import_module('mappings.languages.' + lang)
    name = language.name_ancient
    description = language.description_ancient