#Default ecological community transition function
import numpy as np

def eco_transition_function(n, N, params):
    return params['r0'] * n - params['d0'] * n**2 * N/(params['Nc'])

eco_params = {'r0':0.2, 'd0':0.010011, 'S':10, 'Nc':95}

def pandemic_transition_function(n, I, params):
    m_effective = (params['m_(t-tau)'] - params['c1'] * params['tau'] * params['d_0'] * n)
    
    return (params['c0'] * params['h'] * n * np.exp(- 1 * I / params['K'])) * (m_effective - n) - (params['d_0'] * n)

pandemic_params = {
    'm_0': 100,
    'S': 100, # analogous to G
    'K': 400,
    'd_0': 0.1,
    'c0': 0.00137, # analogous to r_0
    'c1': 0,
    'c2': 0,
    'tau': 0.05,
    '<n>_(t-tau)': 0,
    'm_(t-tau)': 100, # should be set to the same value as m_0
}

#TODO: Add remaining 2 functions from paper