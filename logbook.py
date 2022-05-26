import datetime
import os

def Date_Int():
    """
    現在時刻をInt形式で出力
    :return: YYYY, MM, DD, hh, mm, ss, ms
    """
    date = datetime.datetime.now()

    YYYY = date.year    # 年
    MM = date.month     # 月
    DD = date.day       # 日

    hh = date.hour      # 時
    mm = date.minute    # 分
    ss = date.second    # 秒

    ms = date.microsecond   # マイクロ秒

    return YYYY, MM, DD, hh, mm, ss, ms

def Date_Str():
    """
    2桁に統一した現在時刻を出力
    :return: YYYY, MM, DD, hh, mm, ss, ms
    """

    # 現在時刻と時間を整数として取得
    YYYY, MM, DD, hh, mm, ss, ms = Date_Int()

    # 右詰めで数字をn桁の文字列に変換
    YYYY = str(YYYY).zfill(4)   # 年
    MM = str(MM).zfill(2)       # 月
    DD = str(DD).zfill(2)       # 日

    hh = str(hh).zfill(2)       # 時
    mm = str(mm).zfill(2)       # 分
    ss = str(ss).zfill(2)       # 秒

    ms = str(ms).zfill(6)       # マイクロ秒

    return YYYY, MM, DD, hh, mm, ss, ms

def Date_EachLog():
    """
    ログファイル用の時間を出力(str)
    :return: 2022-05-24_12:34:56
    """
    YYYY, MM, DD, hh, mm, ss, ms = Date_Str()

    date_for_log = "{0}-{1}-{2}_{3}:{4}:{5}".format(YYYY,MM,DD,hh,mm,ss)

    return date_for_log

def MakeLogFile(FolderName="log"):
    """
    最初にログファイルを作成するとき、そのファイル名を出力
    :param FolderName: ディレクトリ名
    :return: "LOG_20220524123456"
    """
    YYYY, MM, DD, hh, mm, ss, ms = Date_Str()

    if FolderName == "":
        filename = "./log_{1}{2}{3}_{4}{5}{6}.txt".format(FolderName, YYYY, MM, DD, hh, mm, ss)
    else:
        if not os.path.isdir(FolderName):
            os.mkdir(FolderName)
        filename = "./{0}/log_{1}{2}{3}_{4}{5}{6}.txt".format(FolderName,YYYY,MM,DD,hh,mm,ss)

    return filename

def WriteLog(FileName,data_list):
    """
    実際のログの一行
    :param FileName:
    :param data_list: [data1, data2, bool_data, str_data]
    :return: 2022-05-24_12:34:56 data1, data2, bool_data, str_data
    """

    str_data = Date_EachLog()
    for data in data_list:
        line = "{0}".format(data).replace(' ', '')
        str_data += ", {0}".format(line)
    str_data += "\n"

    with open(FileName, 'a', newline='') as f:
        f.write(str_data)


if __name__ == '__main__':
    print("\n****************************")
    print("You Opened {0}".format(__file__))
    print("****************************\n")

    filename = MakeLogFile("log") # 保存したいフォルダ・ファイル名を取得

    data_list = [[1,2,3,4], "A", "B", "Message", True]  # 保存したいデータをリスト形式で格納
    WriteLog(filename, data_list)    # ファイル名とデータを使用してログデータを書き込む

    data_list = [[2,4,6,8], "C", "D", "Message", False]
    WriteLog(filename, data_list)
