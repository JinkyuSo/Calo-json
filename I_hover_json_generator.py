import json


############ Inner ###############

Calo_json = []

n_col = 194
n_row = 158
step = 40.633
x_start = -3941.409
y_start = -3210.013
area = 2
col_start = -65
row_start = -47

for bin_id in range(30652):
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

with open("calo_Inner.json", "w") as f:
    json.dump(Calo_json, f, indent=4)
