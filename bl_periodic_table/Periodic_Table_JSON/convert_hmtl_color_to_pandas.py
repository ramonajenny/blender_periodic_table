from pprint import pprint
import pandas

url = r'file:///home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/atom_colors.html'

tables = pandas.read_html(url)
color_table = tables[0]
pprint(color_table)

#df_color = color_table.iloc[2]
#pprint(df_color)

#color_table['3'] = color_table['3'].astype(int)

#tables[2] = tables[2].apply(pandas.to_numeric)

#color_table[3] = color_table[3].apply(pandas.to_numeric)







