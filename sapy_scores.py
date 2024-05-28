import pandas as pd

def create_results_df(desc, rmse, precision, recall, f1_score)
    return pd.DataFrame({
      "Experiment": desc,
      "RMSE": [rmse],
      "Precision": [precision],
      "Recall": [recall],
      "F1_Score": [f1_score]})

def append_to_results_df(tset, df):
   return pd.concat([df, tset], , ignore_index=True))

def sort_and_report_minmax(df, sort_field, asc=False):
  # Sort the dataframe by the specified field in descending order
  sorted_df = df.sort_values(by=sort_field, ascending=asc)

  # Get the first row (which has the max value after sorting)
  max_row = sorted_df.iloc[0]

  # Extract the description and the max value
  description = max_row['Experiment']
  max_value = max_row[sort_field]

  # Report back the description and the max value
  return description, max_value

def iterate_scores_getbest(df):
  fields_to_sort = [col for col in df.columns if col != 'Experiment']

  # Iterate over the fields and call the sort_and_report_max function
  rs = {field: sort_and_report_minmax(df, field, True if field == "RMSE" else False)[0] for field in fields_to_sort if field != 'Experiment'}

  return rs
