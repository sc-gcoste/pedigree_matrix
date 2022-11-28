uncertainty_factors = {
    'version_1': {
        "reliability": (1.0, 1.05, 1.1, 1.2, 1.5),
        "completeness": (1.0, 1.02, 1.05, 1.1, 1.2),
        "temporal correlation": (1.0, 1.03, 1.1, 1.2, 1.5),
        "geographical correlation": (1.0, 1.01, 1.02, 1.02, 1.1),
        "further technological correlation": (1.0, 1.0, 1.2, 1.5, 2),
        "sample size": (1.0, 1.02, 1.05, 1.1, 1.2),
    },

    'version_2': {
        "reliability": (1.0, 1.54, 1.61, 1.69, 1.69),
        "completeness": (1.0, 1.03, 1.04, 1.08, 1.08),
        "temporal correlation": (1.0, 1.03, 1.1, 1.19, 1.29),
        "geographical correlation": (1.0, 1.04, 1.08, 1.11, 1.11),
        "further technological correlation": (1.0, 1.18, 1.65, 2.08, 2.8),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Version 3 is the generic PM from Muller et al. 2016
    'version_3': {
        "reliability": (1.0, 1.01, 1.21, 1.25, 2.36),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.08, 1.55, 2.22, 2.49),
        # The factor for score 5 is 2.30, but we use the same as score 4 for more consistency
        "geographical correlation": (1.0, 1.14, 1.23, 2.36, 2.36),
        "further technological correlation": (1.0, 1.19, 1.52, 1.95, 2.23),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Agriculture specific PM from Muller et al. 2016
    'version_3_agriculture': {
        "reliability": (1.0, 1.00, 1.05, 1.07, 1.6),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.03, 1.13, 1.8, 4.07),
        # The factor for score 5 is 1.55, but we use the same as score 4 for more consistency
        "geographical correlation": (1.0, 1.0, 1.10, 1.57, 1.57),
        "further technological correlation": (1.0, 1.0, 1.32, 1.59, 2.03),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Combustion specific PM from Muller et al. 2016
    'version_3_combustion': {
        "reliability": (1.0, 1.06, 1.12, 1.18, 1.69),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.08, 1.27, 1.72, 1.75),
        # The factor for score 5 is 1.65, but we use the same as score 4 for more consistency
        "geographical correlation": (1.0, 1.08, 1.11, 1.66, 1.66),
        "further technological correlation": (1.0, 1.04, 1.04, 1.5, 1.89),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Utilities specific PM from Muller et al. 2016
    'version_3_utilities': {
        "reliability": (1.0, 1.01, 1.21, 1.25, 2.36),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.0, 1.22, 1.87, 2.52),
        "geographical correlation": (1.0, 1.14, 1.23, 2.36, 2.36),
        "further technological correlation": (1.0, 1.0, 1.29, 1.62, 2.0),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Manufacturing specific PM from Muller et al. 2016
    'version_3_manufacturing': {
        "reliability": (1.0, 1.0, 1.2, 1.25, 2.6),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.05, 1.38, 2.12, 2.47),
        # The factor for score 5 is 2.92, but we use the same as score 4 for more consistency
        "geographical correlation": (1.0, 1.09, 1.16, 1.98, 1.98),
        "further technological correlation": (1.0, 1.19, 1.52, 1.95, 2.23),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Chemicals specific PM from Muller et al. 2016
    'version_3_chemicals': {
        "reliability": (1.0, 1.01, 1.21, 1.25, 2.36),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.08, 1.55, 2.22, 2.49),
        "geographical correlation": (1.0, 1.14, 1.23, 2.36, 2.36),
        "further technological correlation": (1.0, 1.16, 1.44, 2.04, 2.21),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Metal specific PM from Muller et al. 2016
    'version_3_metal': {
        "reliability": (1.0, 1.0, 1.0, 1.21, 1.51),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.07, 1.22, 1.32, 1.49),
        "geographical correlation": (1.0, 1.14, 1.23, 2.36, 2.36),
        "further technological correlation": (1.0, 1.19, 1.52, 1.95, 2.23),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    },

    # Transport specific PM from Muller et al. 2016
    'version_3_transport': {
        "reliability": (1.0, 1.01, 1.21, 1.25, 2.36),
        "completeness": (1.0, 1.02, 1.05, 1.10, 1.63),
        "temporal correlation": (1.0, 1.08, 1.55, 2.22, 2.49),
        # The factor for score 5 is 1.15, but we use the same as score 4 for more consistency
        "geographical correlation": (1.0, 1.16, 1.26, 1.26, 1.26),
        "further technological correlation": (1.0, 1.19, 1.52, 1.95, 2.23),
        "sample size": (1.0, 1.0, 1.0, 1.0, 1.0),
    }
}

# from collections import defaultdict

# basic_uncertainty = {
#     "demand": {
#         "thermal energy, electricity, semi-finished products, working material, waste treatment services":
#             defaultdict(lambda: 1.05),
#         "transport services (tkm)":
#             defaultdict(lambda: 2),
#         "Infrastructure":
#             defaultdict(lambda: 3)
#         },
#     "resources": {
#         "primary energy carriers, metals, salts":
#             defaultdict(lambda: 1.05),
#         "land use, occupation": {
#             "combustion": 1.5,
#             "process": 1.5,
#             "agricultural": 1.1
#             },
#         "land use, transformation": {
#             "combustion": 2,
#             "process": 2,
#             "agricultural": 1.2
#             }
#         },
#     "water": {
#         "BOD, COD, DOC, TOC, inorganic compounds": {
#             "process": 1.5
#             },
#         "individual hydrocarbons, PAH": {
#             "process": 3
#             },
#         "heavy metals": {
#             "process": 1.5,
#             "agricultural": 1.5
#             },
#         "NO3, PO4": {
#             "agricultural": 1.2
#             }
#         },
#     "soil": {
#         "oil, hydrocarbon total": {
#             "process": 1.5
#             },
#         "heavy metals": {
#             "process": 1.5,
#             "agricultural": 1.5
#             },
#         "pesticides": {
#             "agricultural": 1.2
#             }
#         },
#     "air": {
#         "CO2": {
#             "combustion": 1.05,
#             "process": 1.05
#             },
#         "SO2": {
#             "combustion": 1.05
#             },
#         "NMVOC total": {
#             "combustion": 1.5
#             },
#         "NOx, N2O": {
#             "combustion": 1.5,
#             "agricultural": 1.4
#             },
#         "CH4, NH3": {
#             "combustion": 1.5,
#             "agricultural": 1.2
#             },
#         "individual hydrocarbons": {
#             "combustion": 1.5,
#             "process": 2
#             },
#         "PM>10": {
#             "combustion": 1.5,
#             "process": 1.5
#             },
#         "PM10": {
#             "combustion": 2,
#             "process": 2
#             },
#         "PM2.5": {
#             "combustion": 3,
#             "process": 3
#             },
#         "polycyclic aromatic hydrocarbons (PAH)": {
#             "combustion": 3
#             },
#         "CO, heavy metals": {
#             "combustion": 5
#             },
#         "inorganic emissions, others": {
#             "process": 1.5
#             },
#         "radionuclides (e.g., Radon-222)": {
#             "process": 3
#             }
#         }
#     }
