import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "17QMaTEuydmvzgBZuSA51LlEKD027WHiaAQAu0A3dIj0"
workbook = client.open_by_key(sheet_id)

worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

source_cells = [(2, 3), (2, 4), (2, 11)]
target_cells = [(2, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)


source_cells = [(4, 3), (4, 4), (4, 11)]
target_cells = [(4, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(16, 3), (16, 4), (16, 11)]
target_cells = [(16, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)


    source_cells = [(5, 3), (5, 4), (5, 11)]
target_cells = [(5, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(6, 3), (6, 4), (6, 11)]
target_cells = [(6, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(7, 3), (7, 4), (7, 11)]
target_cells = [(7, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(8, 3), (8, 4), (8, 11)]
target_cells = [(8, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(9, 3), (9, 4), (9, 11)]
target_cells = [(9, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(10, 3), (10, 4), (10, 11)]
target_cells = [(10, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)


    source_cells = [(11, 3), (11, 4), (11, 11)]
target_cells = [(11, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(2, 3), (2, 4), (2, 11)]
target_cells = [(2, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(12, 3), (12, 4), (12, 11)]
target_cells = [(12, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(13, 3), (13, 4), (13, 11)]
target_cells = [(13, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(14, 3), (14, 4), (14, 11)]
target_cells = [(14, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(15, 3), (15, 4), (15, 11)]
target_cells = [(15, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)

    source_cells = [(16, 3), (16, 4), (16, 11)]
target_cells = [(16, 2)]

thresholds = {
    0: [6.9, 7, 8, 9],  # Thresholds for source cell 1
    1: [-1, 0, 25, 40],  # Thresholds for source cell 2
    2: [249, 250, 350, 400]   # Thresholds for source cell 3
}
levels = ["Reset", "Level 2", "Level 3", "Level 4"]

def all_source_cells_meet_level(level, amounts, thresholds):
    for i, amount in enumerate(amounts):
        if amount < thresholds[i][level]:  # Check if amount meets or exceeds the threshold for the level
            return False
    return True

# Get values from all source cells
amounts = [float(sheet.cell(row, col).value or 0) for row, col in source_cells]

# Determine the level that all source cells meet
level = "Reset"  # Default level if no other level is met
for l in range(len(levels) - 1, 0, -1):  # Start from the highest level
    if all_source_cells_meet_level(l, amounts, thresholds):
        level = levels[l]
        break

# Update all target cells with the determined level
for target_row, target_col in target_cells:
    sheet.update_cell(target_row, target_col, level)