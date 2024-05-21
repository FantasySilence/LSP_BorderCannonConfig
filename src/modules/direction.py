# ======================================================== #
# @Author: Fantasy_Silence                                 #
# @Time: 2024-05-21                                        #
# @IDE: Visual Studio Code & PyCharm                       #
# @Python: 3.9.7                                           #
# ======================================================== #
# @Description: 这里用于进行方向的判断                       #
# ======================================================== #
from typing import Optional


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
    ) -> dict[str, list[str]]:
        
        """
        x, z: 珍珠的目标落点
        根据传入的珍珠落点获取方向以及TNT落点配置
        例如：NWD表示TNT落在西北的海泡菜上，SEU表示TNT落在东南的栅栏门上
        """

        # ------ 东南偏东方向 ------ #
        if z < x and x >= 0 and z >= 0:
            return {"000": ["NWD", "NWU", "SWU"]}
        # ------ 东南偏南方向 ------ #
        if z >= x and x > 0 and z >= 0:
            return {"100": ["NWD", "NWU", "NEU"]}
        # ------ 西南偏南方向 ------ #
        if z > -x and x <= 0 and z >= 0:
            return {"101": ["NED", "NEU", "NWU"]}
        # ------ 西南偏西方向 ------ #
        if z <= -x and x <= 0 and z > 0:
            return {"111": ["NED", "NEU", "SEU"]}
        # ------ 西北偏西方向 ------ #
        if z > x and x <= 0 and z <= 0:
            return {"110": ["SED", "SEU", "NEU"]}
        # ------ 西北偏北方向 ------ #
        if z <= x and x < 0 and z <= 0:
            return {"010": ["SED", "SEU", "SWU"]}
        # ------ 东北偏东方向 ------ #
        if z >= -x and x >= 0 and z < 0:
            return {"001": ["SWD", "SWU", "NWU"]}
        # ------ 东北偏北方向 ------ #
        if z < -x and x >= 0 and z <= 0:
            return {"011": ["SWD", "SWU", "SEU"]}
