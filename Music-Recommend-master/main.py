import os
import csv
RATE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "Music-Recommend-master\\Music-Recommend-master\\Data\\rate.csv"
RATE_PATH1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "Music-Recommend-master\\Music-Recommend-master\\Data\\rate1.csv"
with open(RATE_PATH, 'r', newline='') as csvfile_in, open(RATE_PATH1, 'w', newline='') as csvfile_out:
    reader = csv.reader(csvfile_in)
    writer = csv.writer(csvfile_out)

    # 逐行读取原始CSV文件
    for row in reader:
        print("aaa")
        # 检查当前行是否有足够的列（至少三列）
        if len(row) >= 3:
            # 尝试将第三列的值转换为数值并加10
            try:
                row[2] = str(float(row[2]) + 10)
            except ValueError:
                # 如果第三列的值无法转换为数值，打印错误信息
                # 这里也可以选择跳过或者用其他方式处理错误
                print(f"无法将第三列的值转换为数值: {row[2]}")
        # 将修改后的行写入新的CSV文件
        writer.writerow(row)