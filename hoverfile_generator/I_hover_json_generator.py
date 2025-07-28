import json

def make_cell_id(area: int, row: int, col: int) -> int:
    BitsCol = 6
    BitsRow = 6
    BitsArea = 2

    ShiftCol = 0
    ShiftRow = ShiftCol + BitsCol      
    ShiftArea = ShiftRow + BitsRow     

    mask_col  = (1 << BitsCol) - 1
    mask_row  = (1 << BitsRow) - 1
    mask_area = (1 << BitsArea) - 1

    return ((area & mask_area) << ShiftArea) | \
           ((row  & mask_row)  << ShiftRow)  | \
           ((col  & mask_col)  << ShiftCol)

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

    if (73 <= column <= 120) and (61 <= row <= 96):
        if not (89 <= column <= 104 and 73 <= row <= 84):
            x1 = x_start + column * step
            y1 = y_start + row * step
            x2 = x1 + step
            y2 = y1 + step

            col_id = column + col_start  
            row_id = row + row_start     
            encoded_id = (1 << 15) | make_cell_id(area, row_id, col_id)

            text = {
                "bin_id": bin_id,
                "bin_center": [(x1 + x2) / 2, (y1 + y2) / 2],
                "bin_edges": [x1, y1, x2, y2],
                "hover_label": {
                    "Area": area,
                    "Column": column + col_start,
                    "Row": row + row_start,
                    "CellID": encoded_id
                }
            }
            Calo_json.append(text)

with open("Calo_Inner.json", "w") as f:
    json.dump(Calo_json, f, indent=4)

