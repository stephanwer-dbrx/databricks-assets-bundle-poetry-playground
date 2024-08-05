def filter_taxis(df):
  return df.filter("fare_amount > 5.0")