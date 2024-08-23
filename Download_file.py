import boto3
import pandas as pd
import os

s3 = boto3.client('s3')

bucket_name = 'fitappbuckets3'
file_keys = [
    'user_info_1.csv', 'user_info_2.csv', 'user_info_3.csv', 'user_info_4.csv',
    'user_info_5.csv', 'user_info_6.csv', 'user_info_7.csv', 'user_info_8.csv',
    'user_info_9.csv', 'user_info_10.csv', 'user_info_11.csv', 'user_info_12.csv',
    'user_info_13.csv', 'user_info_14.csv', 'user_info_15.csv', 'user_info_16.csv',
    'user_info_17.csv', 'user_info_18.csv', 'user_info_19.csv', 'user_info_20.csv',
    'user_info_21.csv', 'user_info_22.csv',
    
    'user_1.csv', 'user_2.csv', 'user_3.csv', 'user_4.csv', 
    'user_5.csv', 'user_6.csv', 'user_7.csv', 'user_8.csv', 
    'user_9.csv', 'user_10.csv', 'user_11.csv', 'user_12.csv',
    'user_13.csv', 'user_14.csv', 'user_15.csv', 'user_16.csv',
    'user_17.csv', 'user_18.csv', 'user_19.csv', 'user_20.csv',
    'user_21.csv', 'user_22.csv',
    
    'user_1_A.csv', 'user_2_A.csv', 'user_3_A.csv', 'user_4_A.csv', 
    'user_5_A.csv', 'user_6_A.csv', 'user_7_A.csv', 'user_8_A.csv', 
    'user_9_A.csv', 'user_10_A.csv', 'user_11_A.csv', 'user_12_A.csv',
    'user_13_A.csv', 'user_14_A.csv', 'user_15_A.csv', 'user_16_A.csv',
    'user_17_A.csv', 'user_18_A.csv', 'user_19_A.csv', 'user_20_A.csv',
    'user_21_A.csv', 'user_22_A.csv',
    
    'sleep_data_1.csv', 'sleep_data_2.csv', 'sleep_data_3.csv', 'sleep_data_4.csv',
    'sleep_data_5.csv', 'sleep_data_6.csv', 'sleep_data_7.csv', 'sleep_data_8.csv',
    'sleep_data_9.csv', 'sleep_data_10.csv', 'sleep_data_11.csv', 'sleep_data_12.csv',
    'sleep_data_13.csv', 'sleep_data_14.csv', 'sleep_data_15.csv', 'sleep_data_16.csv',
    'sleep_data_17.csv', 'sleep_data_18.csv', 'sleep_data_19.csv', 'sleep_data_20.csv',
    'sleep_data_21.csv', 'sleep_data_22.csv',

    'user_1_plus.csv', 'user_2_plus.csv', 'user_3_plus.csv', 'user_4_plus.csv',
    'user_5_plus.csv', 'user_6_plus.csv', 'user_7_plus.csv', 'user_8_plus.csv',
    'user_9_plus.csv', 'user_10_plus.csv', 'user_11_plus.csv', 'user_12_plus.csv',
    'user_13_plus.csv', 'user_14_plus.csv', 'user_15_plus.csv', 'user_16_plus.csv',
    'user_17_plus.csv', 'user_18_plus.csv', 'user_19_plus.csv', 'user_20_plus.csv',
    'user_21_plus.csv', 'user_22_plus.csv'
]

save_dir = os.path.expanduser("~/Desktop/DataPaper")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for file_key in file_keys:
    try:
        s3.head_object(Bucket=bucket_name, Key=file_key)
        file_exists = True
    except:
        file_exists = False

    if file_exists:
        local_file_name = os.path.join(save_dir, file_key.split('/')[-1])
        s3.download_file(bucket_name, file_key, local_file_name)
        if file_key.endswith('.csv'):
            df = pd.read_csv(local_file_name)
        print(f"Processing {file_key}")
        print(df.head())
    else:
        print(f"File {file_key} does not exist in the bucket {bucket_name} and was skipped.")
