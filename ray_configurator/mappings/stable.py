setting = {
    'SUN_LIGHT_ENABLE': {
        0: "None",
        1: "Default",
        2: "Sun radience via solar zenith angle"
    },
    'SUN_SHADOW_QUALITY': {
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
    'FOG_ENABLE': {
        0: "Disabled",
        1: "Enabled"
    },
    'MULTI_LIGHT_ENABLE': {
        0: "Enabled",
        1: "Disabled"
    },
    'OUTLINE_QUALITY': {
        0: "Disabled",
        1: "Enabled",
        2: "Enabled + SMAA",
        3: "Enabled + SSAA",
    },
    'TOON_ENABLE': {
        0: "Disabled",
        1: "Enabled",
        2: "Enabled w/ Diffusion"
    },
    'SSDO_QUALITY': {
        0: "Disabled",
        1: "8 samples",
        2: "12 samples",
        3: "16 samples",
        4: "20 samples",
        5: "24 samples",
        6: "28 samples",
    },
    'SSR_QUALITY': {
        0: "Disabled",
        1: "32 samples",
        2: "64 samples",
        3: "128 samples",
    },
    'SSSS_QUALITY': {
        0: "Disabled",
        1: "Enabled",
    },
    'BOKEH_QUALITY': {
        0: "Disabled",
        1: "Enabled",
    },
    'HDR_EYE_ADAPTATION': {
        0: "Disabled",
        1: "ISO 100 (12.7%)",
        2: "ISO 100 (18%)",
    },
    'HDR_BLOOM_MODE': {
        0: "None",
        1: "Inf",
        2: "Saturate",
        3: "Luminance & Exposure",
        4: "Saturate & Exposure",
    },
    'HDR_FLARE_MODE': {
        0: "None",
        1: "Blue",
        2: "Orange",
        3: "Auto",
    },
    'HDR_STAR_MODE': {
        0: "Disabled",
        1: "Anamorphic Lens Flares (Blue)",
        2: "Anamorphic Lens Flares (Auto)",
        3: "Glare Star (Orange)",
        4: "Glare Star (Auto)",
    },
    'HDR_TONEMAP_OPERATOR': {
        0: "Linear",
        1: "Reinhard",
        2: "Hable",
        3: "Uncharted 2",
        4: "Hejl2015",
        5: "ACES",
        6: "Naughty Dog",
    },
    'AA_QUALITY': {
        0: "Disabled",
        1: "FXAA",
        2: "SMAAx1 (Medium)",
        3: "SMAAx1 (High)",
        4: "SMAAx2 (Medium)",
        5: "SMAAx2 (High)",
    },
    'POST_DISPERSION_MODE': {
        0: "Disabled",
        1: "Colour Shift",
        2: "Chromatic Aberration",
    }
}

category = {
    'Lighting': ['SUN_LIGHT_ENABLE', 'SUN_SHADOW_QUALITY', 'IBL_QUALITY', 'FOG_ENABLE', 'MULTI_LIGHT_ENABLE'],
    'Post Processing': ['OUTLINE_QUALITY', 'TOON_ENABLE', 'SSDO_QUALITY', 'SSR_QUALITY', 'SSSS_QUALITY', 'BOKEH_QUALITY', 'HDR_EYE_ADAPTATION', 'HDR_BLOOM_MODE', 'HDR_FLARE_MODE', 'HDR_STAR_MODE', 'HDR_TONEMAP_OPERATOR', 'AA_QUALITY', 'POST_DISPERSION_MODE'],
}

inputs = {
    'SUN_LIGHT_ENABLE': 'dropdown',
    'SUN_SHADOW_QUALITY': 'dropdown',
    'IBL_QUALITY': 'dropdown',
    'FOG_ENABLE': 'checkbox',
    'MULTI_LIGHT_ENABLE': 'checkbox',
    'OUTLINE_QUALITY': 'dropdown',
    'TOON_ENABLE': 'dropdown',
    'SSDO_QUALITY': 'dropdown',
    'SSR_QUALITY': 'dropdown',
    'SSSS_QUALITY': 'checkbox',
    'BOKEH_QUALITY': 'checkbox',
    'HDR_EYE_ADAPTATION': 'dropdown',
    'HDR_BLOOM_MODE': 'dropdown',
    'HDR_FLARE_MODE': 'dropdown',
    'HDR_STAR_MODE': 'dropdown',
    'HDR_TONEMAP_OPERATOR': 'dropdown',
    'AA_QUALITY': 'dropdown',
    'POST_DISPERSION_MODE': 'dropdown',
}

defaults = {
    'SUN_LIGHT_ENABLE': 1,
    'SUN_SHADOW_QUALITY': 3,
    'IBL_QUALITY': 1,
    'FOG_ENABLE': 1,
    'MULTI_LIGHT_ENABLE': 1,
    'OUTLINE_QUALITY': 0,
    'TOON_ENABLE': 0,
    'SSDO_QUALITY': 2,
    'SSR_QUALITY': 0,
    'SSSS_QUALITY': 1,
    'BOKEH_QUALITY': 0,
    'HDR_EYE_ADAPTATION': 0,
    'HDR_BLOOM_MODE': 4,
    'HDR_FLARE_MODE': 0,
    'HDR_STAR_MODE': 0,
    'HDR_TONEMAP_OPERATOR': 4,
    'AA_QUALITY': 1,
    'POST_DISPERSION_MODE': 1,
}

presets = {
    'Default': defaults,
    'Low': {
        'SUN_LIGHT_ENABLE': 1,
        'SUN_SHADOW_QUALITY': 0,
        'IBL_QUALITY': 0,
        'FOG_ENABLE': 1,
        'MULTI_LIGHT_ENABLE': 1,
        'OUTLINE_QUALITY': 0,
        'TOON_ENABLE': 0,
        'SSDO_QUALITY': 0,
        'SSR_QUALITY': 0,
        'SSSS_QUALITY': 0,
        'BOKEH_QUALITY': 0,
        'HDR_EYE_ADAPTATION': 0,
        'HDR_BLOOM_MODE': 0,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 0,
        'AA_QUALITY': 0,
        'POST_DISPERSION_MODE': 0,
    },
    'Medium': {
        'SUN_LIGHT_ENABLE': 1,
        'SUN_SHADOW_QUALITY': 1,
        'IBL_QUALITY': 0,
        'FOG_ENABLE': 1,
        'MULTI_LIGHT_ENABLE': 1,
        'OUTLINE_QUALITY': 0,
        'TOON_ENABLE': 0,
        'SSDO_QUALITY': 1,
        'SSR_QUALITY': 0,
        'SSSS_QUALITY': 0,
        'BOKEH_QUALITY': 0,
        'HDR_EYE_ADAPTATION': 0,
        'HDR_BLOOM_MODE': 1,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 1,
        'AA_QUALITY': 1,
        'POST_DISPERSION_MODE': 0,
    },
    'High': {
        'SUN_LIGHT_ENABLE': 1,
        'SUN_SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'FOG_ENABLE': 1,
        'MULTI_LIGHT_ENABLE': 1,
        'OUTLINE_QUALITY': 0,
        'TOON_ENABLE': 0,
        'SSDO_QUALITY': 2,
        'SSR_QUALITY': 0,
        'SSSS_QUALITY': 1,
        'BOKEH_QUALITY': 0,
        'HDR_EYE_ADAPTATION': 0,
        'HDR_BLOOM_MODE': 4,
        'HDR_FLARE_MODE': 0,
        'HDR_STAR_MODE': 0,
        'HDR_TONEMAP_OPERATOR': 4,
        'AA_QUALITY': 1,
        'POST_DISPERSION_MODE': 1,
    },
    'Ultra': {
        'SUN_LIGHT_ENABLE': 1,
        'SUN_SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'FOG_ENABLE': 1,
        'MULTI_LIGHT_ENABLE': 1,
        'OUTLINE_QUALITY': 0,
        'TOON_ENABLE': 0,
        'SSDO_QUALITY': 3,
        'SSR_QUALITY': 1,
        'SSSS_QUALITY': 1,
        'BOKEH_QUALITY': 1,
        'HDR_EYE_ADAPTATION': 1,
        'HDR_BLOOM_MODE': 4,
        'HDR_FLARE_MODE': 1,
        'HDR_STAR_MODE': 1,
        'HDR_TONEMAP_OPERATOR': 4,
        'AA_QUALITY': 2,
        'POST_DISPERSION_MODE': 1,
    },
    'Extreme': {
        'SUN_LIGHT_ENABLE': 1,
        'SUN_SHADOW_QUALITY': 3,
        'IBL_QUALITY': 1,
        'FOG_ENABLE': 1,
        'MULTI_LIGHT_ENABLE': 1,
        'OUTLINE_QUALITY': 0,
        'TOON_ENABLE': 0,
        'SSDO_QUALITY': 3,
        'SSR_QUALITY': 1,
        'SSSS_QUALITY': 1,
        'BOKEH_QUALITY': 1,
        'HDR_EYE_ADAPTATION': 1,
        'HDR_BLOOM_MODE': 4,
        'HDR_FLARE_MODE': 1,
        'HDR_STAR_MODE': 1,
        'HDR_TONEMAP_OPERATOR': 4,
        'AA_QUALITY': 2,
        'POST_DISPERSION_MODE': 1,
    },
    'Custom': defaults
}

# language

import importlib

language = importlib.import_module('mappings.languages.english')

name = language.name_stable
description = language.description_stable

def set_language(lang):
    global name
    global description
    language = importlib.import_module('mappings.languages.' + lang)
    name = language.name_stable
    description = language.description_stable