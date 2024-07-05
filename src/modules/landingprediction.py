# =============================================== #
# @Author: Fantasy_Silence                        #
# @Time: 2024-06-14                               #
# @IDE: Visual Studio Code & PyCharm              #
# @Python: 3.9.7                                  #
# =============================================== #
# @Description: 计算珍珠途径的坐标，进行落点预测     #
# =============================================== #
import json
import pandas as pd


class LandingPointPrediction:

    """
    珍珠落点位置的预报
    """

    @staticmethod
    def generate(
        x_motion: float, y_motion: float, z_motion: float
    ) -> pd.DataFrame:
        
        """
        x_motion, y_motion, z_motion: 珍珠起始动量
        """
        
        # ------ 读取默认设置，获取珍珠初始位置 ------ #
        with open("resources/settings/settings.json", "r") as f:
            settings = json.load(f)
        
        # ------ 珍珠初始位置 ------ #
        x = x_init = float(settings["default_x_init"])
        y = y_init = float(settings["default_y_init"])
        z = z_init = float(settings["default_z_init"])

        # ------ 初始化存储结果的列表 ------ #
        PearlLocation = [[0, x_init, y_init, z_init]]
        tick = 0

        # ------ 计算珍珠途径位置 ------ #
        while y>=128:
            tick = tick + 1
            x = x + x_motion
            y = y + y_motion
            z = z + z_motion
            x_motion = 0.99 * x_motion
            y_motion = 0.99 * y_motion - 0.03
            z_motion = 0.99 * z_motion
            PearlLocation.append([tick, x, y, z])

        # ------ 返回结果 ------ #
        PearlLocationFrame = pd.DataFrame(
            PearlLocation, columns=['珍珠飞行游戏刻','x坐标','y坐标','z坐标']
        )
        return PearlLocationFrame
