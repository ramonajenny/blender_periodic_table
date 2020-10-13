from pprint import pprint
import json
import pandas

url = r'file:///home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_colors.html'
table = pandas.read_html(url)
color_table = table[0]
pprint(color_table)

txt = '/home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_radius.csv'
radius_tables = pandas.read_csv(txt, sep=',', names=['atomic_number', 'symbol', 'name', 'atomic_radius_empirical', 'atomic_radius_calculated', 'van_der_waals_radius', 'covalent_radius_single_bond', 'covalent_radius_triple_bond', 'metallic_radius'])
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

    '''col3 = radius_tables.loc[:, "atomic_radius_empirical"]
    #pprint(col3)
    col5 = radius_tables.loc[:, "van_der_waals_radius"]
    #pprint(col5)
    col6 = radius_tables.loc[:, "covalent_radius_single_bond"]
    #pprint(col6)
    # #get_atomic_radius_empirical = radius_tables.loc[indx]
    #pprint(get_atomic_radius_empirical['atomic_radius_empirical'])
    periodic_table["elements"][i].update({"atomic_radius_empirical": col3})
    get_van_der_waals_radius = radius_tables.loc[i]
    periodic_table["elements"][i].update({"van_der_waals_radius": col5})
    get_covalent_radius_single_bond = radius_tables.loc[i]
    periodic_table["elements"][i].update({"covalent_radius_single_bond": col6})'''

    #print(indx)
    #print(ele)

    i += 1

#radius_tables.to_json()

with open("my_periodic_table.json", "w") as write_file:
    json.dump(periodic_table, write_file)







