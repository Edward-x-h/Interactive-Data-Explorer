import pandas as pd

def process_data(csv_file):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 提取设备名称
    device_names = df.iloc[1].tolist()

    # 提取测试间隔时间
    interval_times = df.iloc[5].tolist()

    # 提取测试结果数据
    test_data = df.iloc[49:].reset_index(drop=True)

    # 构建新的 DataFrame
    new_df = pd.DataFrame()

    # 添加设备名称列
    for i, name in enumerate(device_names):
        new_df[name] = test_data.iloc[:, i]

    # 添加测试间隔时间列
    new_df['Interval Time'] = interval_times

    return new_df
