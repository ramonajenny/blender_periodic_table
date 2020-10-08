from pprint import pprint
import json
import pandas as panda

url = r'file:///home/ramona/Desktop/atomColors.html'
tables = panda.read_html(url)
color_table = tables[0]
#pprint(color_table)
#color_table.columns=["Atomic_Number", "Atom_Name", "Jmol_Color", "Rasmol_Color"]
#color_table.to_json(r'/home/ramona/PycharmProjects/EarProject/convertHTMLtoJSON.json')

with open("PeriodicTableJSON.json", "r") as read_file:
    periodic_table = json.load(read_file)

indx = 0
for ele in periodic_table["elements"]:
    del periodic_table["elements"][indx]["discovered_by"]
    del periodic_table["elements"][indx]["named_by"]
    del periodic_table["elements"][indx]["source"]
    del periodic_table["elements"][indx]["spectral_img"]
    del periodic_table["elements"][indx]["summary"]

    get_number = periodic_table["elements"][indx]["number"]
    df_val = color_table.loc[color_table[0] == get_number]
    #print(df_val)

    if not df_val.empty:
        get_color = color_table.loc[indx, 2]
        periodic_table["elements"][indx].update({"color_RBG": get_color})
        get_color_hex = color_table.loc[indx, 3]
        periodic_table["elements"][indx].update({"color": get_color_hex})
        #print("has color")
        print(periodic_table)
    else:
        if get_number == 112:
            periodic_table["elements"][indx].update({"color_RBG": "[184,184,208]"})
            periodic_table["elements"][indx].update({"color": "B8B8D0"})
        else:
            periodic_table["elements"][indx].update({"color_RBG": "[235,235,235]"})
            periodic_table["elements"][indx].update({"color": "EBEBEB"})
        print("no color")

   # print(df_val)
  #  print(indx)
  #  print(ele)
    indx += 1

with open("MyPeriodic_Table.json", "w") as write_file:
    json.dump(periodic_table, write_file)







