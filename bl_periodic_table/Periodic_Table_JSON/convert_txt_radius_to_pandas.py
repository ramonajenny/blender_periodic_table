from pprint import pprint
import pandas
import numpy as np

txt = '/home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_radius.csv'
out_whitespaces = txt.strip()
radius_tables = pandas.read_csv(txt, sep=',', names=['atomic_number', 'symbol', 'name', 'atomic_radius_empirical',
                                                     'atomic_radius_calculated', 'van_der_waals_radius',
                                                     'covalent_radius_single_bond', 'covalent_radius_triple_bond',
                                                     'metallic_radius'])
pprint(radius_tables)

#col = radius_tables.iloc[3, 5]
#[index, column]
#pprint(col)

#df_radius = radius_tables.loc[radius_tables['atomic_number'] == 18]
#pprint(df_radius['symbol'].values[0])

#radius_tables['atomic_radius_empirical'] = pandas.to_numeric(radius_tables['atomic_radius_empirical'])
#radius_tables['van_der_waals_radius'] = pandas.to_numeric(radius_tables['van_der_waals_radius'])
#radius_tables['covalent_radius_single_bond'] = pandas.to_numeric(radius_tables['covalent_radius_single_bond'])

#radius_tables['atomic_radius_empirical'] = radius_tables['atomic_radius_empirical'].astype(int)
#radius_tables['van_der_waals_radius'] = radius_tables['van_der_waals_radius'].astype(int)
#radius_tables['covalent_radius_single_bond'] = radius_tables['covalent_radius_single_bond'].astype(int)


radius_tables = radius_tables.replace(r'^\s*$', -1, regex=True)
radius_tables = radius_tables.replace(np.nan, -1)

radius_tables[['atomic_radius_empirical', 'van_der_waals_radius', 'covalent_radius_single_bond']] = radius_tables[[
    'atomic_radius_empirical', 'van_der_waals_radius', 'covalent_radius_single_bond']].apply(pandas.to_numeric)

#radius_tables[['van_der_waals_radius']] = radius_tables[['van_der_waals_radius']].apply(pandas.to_numeric)
#radius_tables[['covalent_radius_single_bond']] = radius_tables[['covalent_radius_single_bond']].apply(pandas.to_numeric)

pprint(radius_tables)
pprint(radius_tables.iloc[100])
