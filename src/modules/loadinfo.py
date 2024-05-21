# ============================================== #
# @Author: Fantasy_Silence                       #
# @Time: 2024-05-21                              #
# @IDE: Visual Studio Code & PyCharm             #
# @Python: 3.9.7                                 #
# ============================================== #
# @Description: 生成配置信息                      #
# ============================================== #
import numpy as np
from typing import Optional
from src.modules.direction import DirectionJudgment
from src.common.const import DIRECTION_TABLE, DIRECTION_ROTATION


class ConfigInfo:

    """
    生成TNT落点的配置信息
    """

    @staticmethod
    def load(x: Optional[float], z: Optional[float]) -> tuple[np.ndarray, str]:

        """
        加载信息
        x, z: 珍珠的目标落点
        """

        # ------ 包含珍珠落点相对于炮口的方向以及TNT落点的方向代码 ------ #
        TNT_point_dict = DirectionJudgment.get_direction(
            x - DIRECTION_ROTATION["X"], z - DIRECTION_ROTATION["Z"]
        )

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
    