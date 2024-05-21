# =========================================================== #
# @Author: Fantasy_Silence                                    #
# @Time: 2024-05-21                                           #
# @IDE: Visual Studio Code & PyCharm                          #
# @Python: 3.9.7                                              #
# =========================================================== #
# @Description: 根据TNT落点信息加载单个TNT动量                  #
# =========================================================== #
import numpy as np
from typing import Optional
from src.common.const import MOTION_PER_TNT
from src.modules.loadinfo import ConfigInfo


class LoadOneTNTMotion:

    """
    根据之前生成的TNT配置信息矩阵计算单个TNT的动量
    """

    @staticmethod
    def load(x: Optional[float], z: Optional[float]) -> tuple[np.ndarray, str]:

        """
        加载信息
        x, z: 珍珠的目标落点
        """

        # ------ TNT相对于炮口的方向信息 ------ #
        TNT_direction, direction_code = ConfigInfo.load(x, z)

        # ------ 存储单个TNT的动量 ------ #
        TNT_motion = np.zeros((3, 3), dtype=float)

        # ------ 遍历TNT落点方向矩阵 ------ #
        for i in range(TNT_direction.shape[0]):
            # ------ 如果TNT落在海泡菜上 ------ #
            if TNT_direction[i, 1] == -1:
                TNT_motion[i, 0] = MOTION_PER_TNT["D"]["X"] * TNT_direction[i, 0]
                TNT_motion[i, 1] = MOTION_PER_TNT["D"]["Y"]
                TNT_motion[i, 2] = MOTION_PER_TNT["D"]["Z"] * TNT_direction[i, 2]
            # ------ 如果TNT落在栅栏门上 ------ #
            else:
                TNT_motion[i, 0] = MOTION_PER_TNT["U"]["X"] * TNT_direction[i, 0]
                TNT_motion[i, 1] = MOTION_PER_TNT["U"]["Y"]
                TNT_motion[i, 2] = MOTION_PER_TNT["U"]["Z"] * TNT_direction[i, 2]
        
        # ------ 返回单个TNT给珍珠的动量与珍珠落点相对于炮口的方向二进制码 ------ #
        return TNT_motion, direction_code
            