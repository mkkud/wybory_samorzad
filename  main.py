import pandas as pd
import os 

def load_data_from_folder(folder_path):
    """
    Load all CSV files from a specified folder into a single DataFrame.
    
    Parameters:
    folder_path (str): The path to the folder containing CSV files.
    
    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files.
    """
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dataframes = []
    
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        # Optionally, you can add a column to identify the source file
        df['source_file'] = file
        dataframes.append(df)
    
    return pd.concat(dataframes, ignore_index=True)


if __name__ == "__main__":
    folder_path = 'data/data_2nd'  # Replace with your folder path
    combined_data = load_data_from_folder(folder_path)
    print(combined_data.head())  # Display the first few rows of the combined DataFrame
    combined_data.to_csv('combined_data.csv', index=False)  # Save the combined DataFrame to a CSV file




