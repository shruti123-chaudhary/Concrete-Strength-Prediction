# import pandas as pd
# import glob

# # Get all CSV files in the folder
# files = glob.glob("*.csv")
# print(files)
# # Read and merge
# df_list = [pd.read_csv(f) for f in files]
# merged_df = pd.concat(df_list, ignore_index=True)
# # Save merged file
# merged_df.to_csv("merged.csv", index=False)

import pandas as pd
import numpy as np

# Step 1: Read your CSV file
df = pd.read_csv("final_sheet.csv")

# Step 2: Fill the empty column (say the column name is 'flag') with random 0s and 1s
df['flag'] = np.random.randint(0, 2, size=len(df))

# Step 3: Save the updated file
df.to_csv("final_sheet2.csv", index=False)

print("Column filled and file saved successfully!")

# import pandas as pd
# import glob

# # Step 1: Get all CSV file names from a folder
# csv_files = glob.glob("*.csv")  # or use a specific path like "data/*.csv"

# # Step 2: Read and merge column-wise
# merged_df = pd.concat([pd.read_csv(f) for f in csv_files], axis=1)

# # Step 3: Save the merged file
# merged_df.to_csv("merged_columns.csv", index=False)

# print("✅ CSV files merged column-wise and saved as merged_columns.csv")
