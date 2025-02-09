from .data import uncertainty_factors
from .from_string import find_pedigree_matrix
from pprint import pformat
import math


class PedigreeMatrix(object):
    labels = (
        "reliability",
        "completeness",
        "temporal correlation",
        "geographical correlation",
        "further technological correlation",
        "sample size",
    )

    def __init__(self, version=1):
        assert version in (1, 2, *uncertainty_factors), f"Version must be 1, 2 or in {list(uncertainty_factors.keys())}"
        self.version = version
        self.factors = {}

    def from_numbers(self, *args):
        assert len(args) in (5, 6), "Must provide either 5 or 6 factors"
        if len(args) == 5:
            args = args + (1,)
        for index, factor in enumerate(args):
            self.factors[self.labels[index]] = factor

    def from_string(self, string):
        factors = find_pedigree_matrix(string)
        if not factors:
            raise ValueError("Can't find Pedigree Matrix factors")
        for index, factor in enumerate(factors):
            self.factors[self.labels[index]] = factor

    def calculate(self, basic_uncertainty=1.0, as_geometric_sigma=False):
        values = [basic_uncertainty] + self.get_values()
        sigma = math.sqrt(sum([math.log(x) ** 2 for x in values]))
        if as_geometric_sigma:
            return math.exp(sigma)
        else:
            return sigma

    def get_values(self):
        assert self.factors, "Must provide Pedigree Matrix factors"
        data = uncertainty_factors['version_1'] if self.version == 1 \
            else uncertainty_factors['version_2'] if self.version == 2 \
            else uncertainty_factors[self.version]
        return [data[key][index - 1] for key, index in self.factors.items()]

    def __repr__(self):
        if not self.factors:
            return u"Empty Pedigree Matrix"
        else:
            return pformat(self.factors)
