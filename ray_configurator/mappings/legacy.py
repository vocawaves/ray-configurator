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
    'FOG_ENABLE': {
        0: "Disabled",
        1: "Enabled"
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
    'HDR_ENABLE': {
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
        5: "ACES"
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
    'POST_DISPERSION_MODE': {
        0: "Disabled",
        1: "Colour Shift",
        2: "Chromatic Aberration",
    }
}

name = {
    'MAIN_LIGHT_ENABLE': "Main light",
    'SHADOW_QUALITY': "Shadow quality",
    'IBL_QUALITY': "IBL quality",
    'FOG_ENABLE': "Fog",
    'SSDO_QUALITY': "SSDO quality",
    'SSR_QUALITY': "SSR quality",
    'HDR_ENABLE': "HDR",
    'HDR_EYE_ADAPTATION': "HDR eye adaptation",
    'HDR_BLOOM_MODE': "HDR bloom mode",
    'HDR_FLARE_MODE': "HDR flare mode",
    'HDR_STAR_MODE': "HDR star mode",
    'HDR_TONEMAP_OPERATOR': "HDR tonemap operator",
    'AA_QUALITY': "Anti-aliasing",
    "AA_GBUFFER_FILTER_QUALITY": "GBuffer filter",
    'POST_DISPERSION_MODE': "Post dispersion mode",
}

category = {
    'Lighting': ['MAIN_LIGHT_ENABLE', 'SHADOW_QUALITY', 'IBL_QUALITY', 'FOG_ENABLE'],
    'SSR': ['SSR_QUALITY'],
    'SSDO': ['SSDO_QUALITY'],
    'HDR': ['HDR_ENABLE', 'HDR_EYE_ADAPTATION', 'HDR_BLOOM_MODE', 'HDR_FLARE_MODE', 'HDR_STAR_MODE', 'HDR_TONEMAP_OPERATOR'],
    'AA': ['AA_QUALITY', 'AA_GBUFFER_FILTER_QUALITY'],
    'Post': ['POST_DISPERSION_MODE'],
}

inputs = {
    'MAIN_LIGHT_ENABLE': 'dropdown',
    'SHADOW_QUALITY': 'dropdown',
    'IBL_QUALITY': 'dropdown',
    'FOG_ENABLE': 'checkbox',
    'SSDO_QUALITY': 'dropdown',
    'SSR_QUALITY': 'dropdown',
    'SSSS_QUALITY': 'checkbox',
    'HDR_ENABLE': 'checkbox',
    'HDR_EYE_ADAPTATION': 'dropdown',
    'HDR_BLOOM_MODE': 'dropdown',
    'HDR_FLARE_MODE': 'dropdown',
    'HDR_STAR_MODE': 'dropdown',
    'HDR_TONEMAP_OPERATOR': 'dropdown',
    'AA_QUALITY': 'dropdown',
    "AA_GBUFFER_FILTER_QUALITY": 'checkbox',
    'POST_DISPERSION_MODE': 'dropdown',
}

defaults = {
    'MAIN_LIGHT_ENABLE': 1,
    'SHADOW_QUALITY': 3,
    'IBL_QUALITY': 1,
    'FOG_ENABLE': 1,
    'SSDO_QUALITY': 2,
    'SSR_QUALITY': 0,
    'SSSS_QUALITY': 1,
    'HDR_ENABLE': 1,
    'HDR_EYE_ADAPTATION': 0,
    'HDR_BLOOM_MODE': 4,
    'HDR_FLARE_MODE': 0,
    'HDR_STAR_MODE': 0,
    'HDR_TONEMAP_OPERATOR': 4,
    'AA_QUALITY': 1,
    "AA_GBUFFER_FILTER_QUALITY": 0,
    'POST_DISPERSION_MODE': 1,
}

description = {
    'MAIN_LIGHT_ENABLE': "Enable/disable the main light.",
    'SHADOW_QUALITY': "Set the shadow quality.",
    'IBL_QUALITY': "Set the IBL quality.",
    'FOG_ENABLE': "Enable/disable fog.",
    'SSDO_QUALITY': "Set the SSDO quality.",
    'SSR_QUALITY': "Set the SSR quality.",
    'SSSS_QUALITY': "Enable/disable SSSS.",
    'HDR_ENABLE': "Enable/disable HDR.",
    'HDR_EYE_ADAPTATION': "Set the HDR eye adaptation.",
    'HDR_BLOOM_MODE': "Set the HDR bloom mode.",
    'HDR_FLARE_MODE': "Set the HDR flare mode.",
    'HDR_STAR_MODE': "Set the HDR star mode.",
    'HDR_TONEMAP_OPERATOR': "Set the HDR tonemap operator.",
    'AA_QUALITY': "Set the anti-aliasing quality.",
    "AA_GBUFFER_FILTER_QUALITY": "Enable/disable the GBuffer filter.",
    'POST_DISPERSION_MODE': "Set the post dispersion mode.",
}
