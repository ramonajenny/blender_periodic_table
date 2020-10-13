from pprint import pprint
import json
import pandas
import numpy as np

url = r'file:///home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_colors.html'
table = pandas.read_html(url)
color_table = table[0]
pprint(color_table)

txt = '/home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_radius.csv'
radius_tables = pandas.read_csv(txt.strip(), sep=',', names=['atomic_number', 'symbol', 'name', 'atomic_radius_empirical', 'atomic_radius_calculated', 'van_der_waals_radius', 'covalent_radius_single_bond', 'covalent_radius_triple_bond', 'metallic_radius'])
pprint(radius_tables)
radius_tables = radius_tables.replace(r'^\s*$', -1, regex=True)
radius_tables = radius_tables.replace(np.nan, -1)

radius_tables[['atomic_radius_empirical', 'van_der_waals_radius', 'covalent_radius_single_bond']] = radius_tables[[
    'atomic_radius_empirical', 'van_der_waals_radius', 'covalent_radius_single_bond']].apply(pandas.to_numeric)

pprint(radius_tables)

with open("master_periodic_table_json_not_mine.json", "r") as read_file:
    periodic_table = json.load(read_file)

i = 0
for ele in periodic_table["elements"]:
    del periodic_table["elements"][i]["discovered_by"]
    del periodic_table["elements"][i]["named_by"]
    del periodic_table["elements"][i]["source"]
    del periodic_table["elements"][i]["spectral_img"]
    del periodic_table["elements"][i]["summary"]

    get_number = periodic_table["elements"][i]["number"]
    df_color = color_table.loc[color_table[0] == get_number]

    if not df_color.empty:
        get_color = color_table.loc[i, 2]
        periodic_table["elements"][i].update({"color_RBG": get_color})
        get_color_hex = color_table.loc[i, 3]
        periodic_table["elements"][i].update({"color": get_color_hex})
        #print("has color")
        #print(periodic_table)
    else:
        if get_number == 112:
            periodic_table["elements"][i].update({"color_RBG": "[184,184,208]"})
            periodic_table["elements"][i].update({"color": "B8B8D0"})
        else:
            periodic_table["elements"][i].update({"color_RBG": "[235,235,235]"})
            periodic_table["elements"][i].update({"color": "EBEBEB"})
        #print("no color")

    df_radius = radius_tables.loc[radius_tables['atomic_number'] == get_number]
    if not df_radius.empty:
        ate = int(df_radius['atomic_radius_empirical'].values[0])
        vdwr = int(df_radius['van_der_waals_radius'].values[0])
        crsb = int(df_radius['covalent_radius_single_bond'].values[0])
        print(str(ate) +","+ str(vdwr) +","+ str(crsb))

        periodic_table["elements"][i].update({"atomic_radius_empirical": ate})
        periodic_table["elements"][i].update({"van_der_waals_radius": vdwr})
        periodic_table["elements"][i].update({"covalent_radius_single_bond": crsb})

        #pprint("this is " +str(ate))

    #print(indx)
    #print(ele)

    i += 1

#radius_tables.to_json()

with open("my_periodic_table.json", "w") as write_file:
    json.dump(periodic_table, write_file)







