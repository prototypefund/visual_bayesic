from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor
from xai_components.xai_plotting.probabilistic_plot import ArvizObject, VisualizeModelGraph, PlotPrior
from xai_components.xai_probabilistic_models.probabilistic_models_I import PyroModel
from xai_components.xai_probability_distributions.probabilistic_distributions import NormalSampler
from xai_components.xai_pyro.probabilistic_node import FullInference

def main(args):
    ctx = {}
    ctx['args'] = args
    c_0 = NormalSampler()
    c_1 = NormalSampler()
    c_2 = VisualizeModelGraph()
    c_3 = PyroModel()
    c_4 = FullInference()
    c_5 = ArvizObject()
    c_6 = PlotPrior()
    c_0.name.value = 'Likelihood\n'
    c_0.mean = c_1.sample
    c_0.std.value = 0.9
    c_0.obs.value = [2.12, 2.06, 2.08, 2.05]
    c_1.name.value = 'Likelihood mean\n'
    c_1.mean.value = 2.07
    c_1.std.value = 0.08
    c_2.model_function = c_3.model
    c_3.arg1 = c_0.sample
    c_4.model = c_3.model
    c_4.num_samples.value = 100
    c_4.num_chains.value = 1
    c_5.prior_predictive_values = c_4.posterior_predictive
    c_5.prior_predictive_values = c_4.prior_predictive
    c_5.posterior_predictive_values = c_4.posterior_samples
    c_6.az_data = c_5.az_data
    c_0.next = c_3
    c_1.next = c_0
    c_2.next = c_4
    c_3.next = c_2
    c_4.next = c_5
    c_5.next = c_6
    c_6.next = None
    next_component = c_1
    while next_component:
        next_component = next_component.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    main(parser.parse_args())
    print('\nFinished Executing')