from config import plugins_config


class MyDict:
    """
    用于读取、存储、查找、删除teach内容
    """
    def __init__(self):
        # 初始化，读取文件
        self.d = {}
        self._read_dict()

    def add_kv(self, k: str, v: str):
        """
        添加键值对
        :param k: key
        :param v: calue
        :return: None
        """
        if self.find_k(k):
            return "我好像已经学过了呢……"
        else:
            self.d[k] = v
            self._save_dict()
            return "我学会啦~快夸我！"

    def delete_k(self, k: str) -> str:
        """
        删除键（以及相关的值）
        :param k: key
        :return: None
        """
        if self.find_k(k):
            self.d.pop(k)
            self._save_dict()
            return "我好像忘了什么……"
        else:
            return "我好像不记得我学过这个呢……"

    def find_k(self, k: str) -> str:
        """
        查找键
        :param k: key
        :return: value->str
        """
        if k in self.d:
            return self.d[k]
        else:
            return ""

    def _read_dict(self):
        """
        逐行读取文件至d
        :return: None
        """
        with open(plugins_config.data_url, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                k = line.split(' ')[0]
                v = line.split(' ')[1]
                self.d[k] = v

    def _save_dict(self):
        """
        保存d至文件
        :return: None
        """
        with open(plugins_config.data_url, 'w+') as f:
            for k, v in self.d.items():
                f.write(str(k) + ' ' + str(v) + '\n')


md = MyDict()
