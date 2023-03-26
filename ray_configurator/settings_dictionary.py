def map_config_values(config_values):
    mapping = {
        'SUN_SHADOW_SAMPLE_QUALITY': {
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Low w/ PCSS",
            5: "Medium w/ PCSS",
            6: "High w/ PCSS"
        },
        'MULTI_SHADOW_MAP_QUALITY': {
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Ultra"
        },
        'MULTI_SHADOW_SAMPLE_QUALITY': {
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Low w/ PCSS",
            5: "Medium w/ PCSS",
            6: "High w/ PCSS"
        },
        'MULTI_VOLUMETRIC_LIGHT_QUALITY': {
            0: "Disabled",
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Ultra"
        },
        'MULTI_VOLUMETIC_SHADOW_QUALITY': {
            0: "Disabled",
            1: "Low",
            2: "Medium",
            3: "High",
            4: "Ultra"
        },
        'IBL_QUALITY': {
            0: "Disabled",
            1: "Enabled",
            2: "Enabled w/ UV flip"
        },
        'OUTLINE_QUALITY': {
            0: "Disabled",
            1: "Enabled",
            2: "Enabled + SSAA"
        },
        'TOON_ENABLE': {
            0: "Disabled",
            1: "Enabled",
            2: "Enabled w/ Diffusion"
        },
        'SSDO_QUALITY': {
            0: "Disabled",
            1: "16 samples",
            2: "24 samples",
            3: "32 samples",
            4: "48 samples",
            5: "64 samples",
            6: "80 samples",
        },
        'SSR_QUALITY': {
            0: "Disabled",
            1: "32 samples",
            2: "64 samples",
            3: "128 samples",
        },
        'SSGI_QUALITY': {
            0: "Disabled",
            1: "16 samples",
            2: "24 samples",
            3: "32 samples",
            4: "48 samples",
            5: "64 samples",
            6: "80 samples",
        },
        'BOKEH_MODE': {
            0: "Disabled",
            1: "Cinematic",
            2: "Hexagonal",
        },
        'EYE_ADAPTATION': {
            0: "Disabled",
            1: "ISO 100",
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
            2: "John-Hable",
            3: "Neutral",
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

    setting_strings = mapping[config_values]
    setting_strings = list(setting_strings.values())

    return {
        'values': list(mapping[config_values].keys()),
        'names': setting_strings
    }
