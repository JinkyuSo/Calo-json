import json


############ Outer ###############

Calo_json = []

n_col = 66
n_row = 54
step = 121.9
x_start = -4022.7
y_start = -3291.3
area = 0
col_start = -1
row_start = 5

for bin_id in range(3564):
    column = bin_id % n_col
    row = bin_id // n_col

    x1 = x_start + column * step
    y1 = y_start + row * step
    x2 = x1 + step
    y2 = y1 + step

    text = {
        "bin_id": bin_id,
        "bin_center": [(x1 + x2) / 2, (y1 + y2) / 2],
        "bin_edges": [x1, y1, x2, y2],
        "hover_label": {
            "Area": area,
            "Column": column,
            "Row": row,
            "CellID": f"{area}_{column + col_start}_{row + row_start}"
        }
    }

    Calo_json.append(text)

with open("calo_Outer.json", "w") as f:
    json.dump(Calo_json, f, indent=4)
