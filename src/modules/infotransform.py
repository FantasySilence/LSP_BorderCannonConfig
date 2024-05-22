# ================================================ #
# @Author: Fantasy_Silence                         #
# @Time: 2024-05-22                                #
# @IDE: Visual Studio Code & PyCharm               #
# @Python: 3.9.7                                   #
# ================================================ #
# @Description: 翻译信息，便于玩家配置               #
# ================================================ #
import numpy as np


class ConfigInfoTransform:

    """
    将配置器计算出的动量翻译为珍珠炮阵列能看懂的信息
    方便玩家配置边境炮
    """

    def __init__(self, tnt_1: int, tnt_2: int, tnt_3: int) -> None:
        
        """
        tnt_1, tnt_2, tnt_3: 分别为第一个第二个第三个TNT的当量
        例如第一个TNT：2113，第二个TNT：60128，第三个TNT：166
        """

        self.TNT_num = np.array([tnt_1, tnt_2, tnt_3])
        # ------ 二进制基础数 ------ #
        self.bin_unit = np.array([16, 8, 4, 2, 1])
        # ------ 数量单位 ------ #
        self.TNT_unit = [260, 10, 1]
        self.times_unit = [1000, 100, 10, 1]

        # ------ 计算TNT当量中260, 10, 1的数量 ------ #
        self.rest_num_of_260 = (self.TNT_num % 780) // 260
        self.rest_num_of_10 = (self.TNT_num % 780) % 260 // 10
        self.rest_num_of_1 = (self.TNT_num % 780) % 260 % 10
        
        # ------ 计算TNT当量中780的数量，即大头的次数 ------ #
        self.times_1000 = (self.TNT_num // 780) // 1000
        self.times_100 = (self.TNT_num // 780) % 1000 // 100
        self.times_10 = (self.TNT_num // 780) % 1000 % 100 // 10
        self.times_1 = (self.TNT_num // 780) % 1000 % 100 % 10

        # ------ 格式化输出结果 ------ #
        self.getResult()
    

    def getResult(self) -> None:

        """
        格式化输出结果
        """

        tnt_dict = self.__getRestofTNTinfo__(
            num_unit=self.TNT_unit, rest="self.rest_num_of_", n=3
        )
        times_dict = self.__getRestofTNTinfo__(
            num_unit=self.times_unit, rest="self.times_", n=4
        )
        print("3个TNT对应的配置信息为：")
        for key in tnt_dict:
            print("-" * 50)
            print("%s的配置信息：" % key[:-2])
            print("大头(以780满当量蓄力的次数)：", times_dict[key])
            print("小头(满当量蓄力后剩余的TNT)：", tnt_dict[key])
        print("-" * 50)


    def __getRestofTNTinfo__(self, num_unit: list, rest: str, n: int) -> dict[str, str]:

        """
        将小头TNT数量进行转化
        例如：
        第1个TNT:  553 = 520 + 20 + 10 + 2 + 1 
        第2个TNT:  68 = 40 + 20 + 8
        第3个TNT:  166 = 160 + 4 + 2
        """
        
        # ------ 初始化一个结果矩阵，用于存储结果 ------ #
        res_matrix = np.zeros((3, n * 5))

        # ------ 将二进制码与数量单元的乘积拼到结果矩阵中 ------ #
        for i in range(len(num_unit)):
            res_matrix[:, 5 * i: 5 * (i + 1)] = ConfigInfoTransform.binNum(
                eval(rest + str(num_unit[i])), 
                num_unit[i], self.bin_unit
            )
        
        # ------ 初始化一个字典存储结果 ------ #
        res_dict = {}

        # ------ 遍历前面生成的结果矩阵，将结果存储到字典中 ------ #
        for i in range(res_matrix.shape[0]):
            res_str = "%d = " % sum(res_matrix[i])
            for j in range(res_matrix.shape[1]):
                if res_matrix[i, j] != 0:
                    res_str += "%d + " % res_matrix[i, j]
            res_dict["第%d个TNT: " % (i + 1)] = res_str[:-2]
        
        # ------ 返回结果字典 ------ #
        return res_dict
    

    @staticmethod
    def binNum(rest: np.ndarray, base: int, bin_unit: np.ndarray) -> np.ndarray:
        
        """
        将转化的二进制码与数量单位相乘
        """

        # ------ 生成一个矩阵用于存储结果 ------ #
        num_matrix = np.zeros((3, 5))

        # ------ 遍历填入，第i行为第i个数量对应的二进制码 ------ #
        for i in range(3):
            num_matrix[i] = np.array(
                list(map(int, bin(rest[i])[2:].zfill(5)))
            )
        
        # ------ 返回二进制码与数量单位相乘 ------ #
        return num_matrix * bin_unit * base
