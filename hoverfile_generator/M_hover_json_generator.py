import json


############ Middle ###############

Calo_json = []

n_col = 130
n_row = 106
step = 60.95
x_start = -3961.75
y_start = -3230.35
area = 1
col_start = -33
row_start = -21

for bin_id in range(13780):
    column = bin_id % n_col
    row = bin_id // n_col

    if (33 <= column <= 96) and (33 <= row <= 72):
        if not (49 <= column <= 80 and 41 <= row <= 64):
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
                    "Column": column + col_start,
                    "Row": row + row_start,
                    "CellID": f"{area}_{column + col_start}_{row + row_start}"
                }
            }
            Calo_json.append(text)

with open("Calo_Middle.json", "w") as f:
    json.dump(Calo_json, f, indent=4)
