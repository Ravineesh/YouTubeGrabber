import config
import pandas as pd
import os


def write_output(video_data, file_name, output_dir):
    """Write the csv file into the path"""
    df = pd.DataFrame(video_data, columns=config.video_table)
    print('Total Records', len(df))

    df.to_csv(os.path.join(output_dir, file_name + "_" + config.FILE_NAME), index=False, header=True)


def key_in_dict_and_not_none(d, key):
    return key in d and d[key] is not None
