import pickle
import os
fn = 'decision_tree_regressor.pkl'
print('exists', os.path.exists(fn))
with open(fn, 'rb') as f:
    obj = pickle.load(f)
print(type(obj))
print('n_features', getattr(obj, 'n_features_in_', 'N/A'))
print('feature_names_in', getattr(obj, 'feature_names_in_', 'N/A'))
print('params', obj.get_params())
