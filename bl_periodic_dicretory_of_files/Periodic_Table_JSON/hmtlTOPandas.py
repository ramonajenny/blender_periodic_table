from pprint import pprint
import json
import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas as panda

url = r'file:///home/ramona/Desktop/atomColors.html'
tables = panda.read_html(url)
color_table = tables[0]
#pprint(color_table)
#color_table.columns=["Atomic_Number", "Atom_Name", "Jmol_Color", "Rasmol_Color"]
#color_table.to_json(r'/home/ramona/PycharmProjects/EarProject/convertHTMLtoJSON.json')

#df_val = color_table.loc[color_table[0], [2]]
indx = 2
df_val = color_table.loc[indx, 2]
#print("this is my value:", df_val)
pprint(color_table)






