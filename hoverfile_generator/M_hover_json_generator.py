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

with open("Calo_Middle.json", "w") as f:
    json.dump(Calo_json, f, indent=4)
