import pandas as pd

from label_2index import label2index
from Rhapsody_cell_keys import CLS1, CLS2, CLS3

CLS1 = dict(zip(CLS1, range(1, len(CLS1)+1)))
CLS2 = dict(zip(CLS2, range(1, len(CLS2)+1)))
CLS3 = dict(zip(CLS3, range(1, len(CLS3)+1)))

my_data = pd.read_csv("C:/Users/Cathal/Desktop/bartable_27.csv")
col_1 = my_data["label"]
col_1 = [f"{CLS1[tag[:9]]}-{CLS2[tag[9:18]]}-{CLS3[tag[18:27]]}" for tag in col_1]
col_2 = [label2index(tag) for tag in col_1]
my_data["identifier_no"] = col_1
my_data["cell_indices"] = col_2
my_data.to_csv("C:/Users/Cathal/Desktop/New_bar_table_converted.csv")



