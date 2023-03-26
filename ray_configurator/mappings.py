setting = {
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
    }
}

name = {
    'SUN_SHADOW_SAMPLE_QUALITY': "Sun Shadow Sample Quality",
    'MULTI_SHADOW_MAP_QUALITY': "Multi Shadow Map Quality"
}

category = {
    'Graphics': ['SUN_SHADOW_SAMPLE_QUALITY', 'MULTI_SHADOW_MAP_QUALITY'],
    'Other': ['SUN_SHADOW_SAMPLE_QUALITY']
}

inputs = {
    'SUN_SHADOW_SAMPLE_QUALITY': 'dropdown',
    'MULTI_SHADOW_MAP_QUALITY': 'dropdown'
}