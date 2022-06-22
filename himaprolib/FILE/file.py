import os


# パスの中にあるファイルをリスト形式で出力
def find_dir(path="./cards"):
    ''' フォルダパス --> ファイルリスト '''
    files = os.listdir(path)
    file_list = [f for f in files if os.path.isfile(os.path.join(path, f))]

    return file_list