

def castom_transform(df):

  df['year**2'] = df['year'].transform(lambda x : x**2)
  df['mileage**2'] = df['mileage'].transform(lambda x : x**2)
  df['1_div_km_driven'] = df['km_driven'].transform(lambda x : 1/x)
  df['engine_bins'] = pd.cut(df['engine'], bins=14, labels=list(range(14)))
  df['max_power_bins'] = pd.cut(df['max_power'], bins=14, labels=list(range(14)))
  df['torque_Nm_bins'] = pd.cut(df['torque_Nm'], bins=14, labels=list(range(14)))

  return df
