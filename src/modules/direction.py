# ======================================================== #
# @Author: Fantasy_Silence                                 #
# @Time: 2024-05-21                                        #
# @IDE: Visual Studio Code & PyCharm                       #
# @Python: 3.9.7                                           #
# ======================================================== #
# @Description: 这里用于进行方向的判断                       #
# ======================================================== #
import numpy as np
from typing import Optional
from src.common.const import *


class DirectionJudgment:

    """
    方向判断类
    珍珠实际落点的方向判断
    以炮口为坐标原点，建立直角坐标系，由于MC中正方向于实际不符，因此为了匹配
    我们重新定义y轴正方向为南方(South)，这样我们可以使用一般的坐标系进行运算而不翻转
    坐标系再计算。方向的判断基于一个二元不等式组实现。
    """

    @staticmethod
    def get_direction(
        x: Optional[float], z: Optional[float]
    ) -> tuple[np.ndarray[int], str]:
        
        """
        x, z: 珍珠的目标落点
        根据传入的珍珠落点获取方向以及TNT落点配置
        例如：NWD表示TNT落在西北的海泡菜上，SEU表示TNT落在东南的栅栏门上
        """

        ## ------ 判断落点相对炮口的方向 ------ ##
        # ------ 平移坐标系 ------ #
        x = x - DIRECTION_ROTATION["X"]
        z = z - DIRECTION_ROTATION["Z"]

        # ------ 东南偏东方向 ------ #
        if z < x and x >= 0 and z >= 0:
            TNT_point_dict = {"000": ["NWD", "NWU", "SWU"]}
        # ------ 东南偏南方向 ------ #
        if z >= x and x > 0 and z >= 0:
            TNT_point_dict = {"100": ["NWD", "NWU", "NEU"]}
        # ------ 西南偏南方向 ------ #
        if z > -x and x <= 0 and z >= 0:
            TNT_point_dict = {"101": ["NED", "NEU", "NWU"]}
        # ------ 西南偏西方向 ------ #
        if z <= -x and x <= 0 and z > 0:
            TNT_point_dict = {"111": ["NED", "NEU", "SEU"]}
        # ------ 西北偏西方向 ------ #
        if z > x and x <= 0 and z <= 0:
            TNT_point_dict = {"110": ["SED", "SEU", "NEU"]}
        # ------ 西北偏北方向 ------ #
        if z <= x and x < 0 and z <= 0:
            TNT_point_dict = {"010": ["SED", "SEU", "SWU"]}
        # ------ 东北偏东方向 ------ #
        if z >= -x and x >= 0 and z < 0:
            TNT_point_dict = {"001": ["SWD", "SWU", "NWU"]}
        # ------ 东北偏北方向 ------ #
        if z < -x and x >= 0 and z <= 0:
            TNT_point_dict = {"011": ["SWD", "SWU", "SEU"]}
        
        ## ------ 生成方向矩阵 ------ ##
        # ------ 提取TNT落点相对于炮口的方向代码 ------ #
        landing_point = list(TNT_point_dict.values())[0]

        # ------ 珍珠落点相对于炮口的方向二进制码 ------ #
        direction_code = list(TNT_point_dict.keys())[0]

        # ------ 初始化一个3x3的矩阵存储TNT落点方向 ------ #
        TNT_direction = np.zeros((3, 3), dtype=int)

        # ------ 将TNT落点相对于炮口的方向代码转换为数字 ------ #
        for i in range(len(landing_point)):
            # 编码与实际处理程序不符，将最后一个字符替换到第一个位置
            true_landing_point = landing_point[i][1:] + landing_point[i][0]
            # 逐个将编码转换为数字1或-1
            for j in range(len(true_landing_point)):
                TNT_direction[i][j] = DIRECTION_TABLE[true_landing_point[j]]

        # ------ 返回最终的TNT落点方向矩阵 ------ #
        return TNT_direction, direction_code
