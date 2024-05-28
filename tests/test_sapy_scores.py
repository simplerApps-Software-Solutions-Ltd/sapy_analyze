
import pandas as pd

from .sapy_scores import create_results_df, append_to_results_df, iterate_scores_getbest

results_set = create_results_df("User-User",	1.024957,	0.860,	0.783,	0.820)
results_set = append_to_results_df(create_results_df("User-User Optimized",	0.962958,	0.850,	0.809,	0.829),results_set)
results_set = append_to_results_df(create_results_df("Item-Item",	1.023244,	0.835,	0.758,	0.795), results_set)

# display results_set data frame to compare experiments
results_set

# analyze results_set data frame
iterate_scores_getbest(results_set)