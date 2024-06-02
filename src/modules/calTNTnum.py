# ============================================== #
# @Author: Fantasy_Silence                       #
# @Time: 2024-05-21                              #
# @IDE: Visual Studio Code & PyCharm             #
# @Python: 3.9.7                                 #
# ============================================== #
# @Description: 计算TNT的当量                     #
# ============================================== #
import numpy as np
import pandas as pd
from src.common.const import DIRECTION_ROTATION
from src.common.const import DIRECTION_CODE_TABLE
from src.modules.loadTNTmotion import LoadOneTNTMotion


class CalculateTNTNumber:

    """
    计算TNT当量
    """

    def __init__(
            self, x: float, y: float, z: float, t: int,
            # ------ 初始位置 ------ #
            x0: float = DIRECTION_ROTATION["X"],
            y0: float = 178.34722638929412,
            z0: float = DIRECTION_ROTATION["Z"]
    ) -> None:
        
        """
        初始化
        x, y, z: 珍珠落点位置
        t: 预期珍珠飞行时间
        """

        self.x, self.y, self.z, self.t = x, y, z, t
        self.x0, self.y0, self.z0 = x0, y0, z0
        self.TNT_motion, self.direction_code = LoadOneTNTMotion.load(x, z)
        self.TNT_num = self.__cal__()
    

    def __cal__(self) -> pd.DataFrame:

        """
        计算TNT当量
        """

        solution_list = []
        for tick in range(self.t, self.t + 100):

            # ------ 计算配置珍珠炮所需动量 ------ #
            px = (self.x - self.x0)/(100 * (1 - 0.99 ** tick))
            py = (self.y - self.y0 + 3 * tick)/(100 * (1 - 0.99 ** tick) - 3)
            pz = (self.z - self.z0)/(100 * (1 - 0.99 ** tick))

            # ------ 利用计算得到的动量，求解线性方程组得到所需TNT数量 ------ #
            # 系数矩阵为得到的TNT动量矩阵，右端向量为到达目的地所需动量
            tntSolve = np.vstack((self.TNT_motion, np.array([px, py, pz]))).T
            tntSolution = np.linalg.solve(tntSolve[:, :-1], tntSolve[:, -1])
            # TNT数量取整
            final_solution = list(map(lambda x: round(x), tntSolution))

            # ------ 计算实际的TNT动量用于测试与校准 ------ #
            real_px = np.sum(
                final_solution[i] * self.TNT_motion[i, 0] for i in range(3)
            )
            real_py = np.sum(
                final_solution[i] * self.TNT_motion[i, 1] for i in range(3)
            )
            real_pz = np.sum(
                final_solution[i] * self.TNT_motion[i, 2] for i in range(3)
            )
            final_solution.extend([real_px, real_py, real_pz])
            # 输出方向
            final_solution.append(DIRECTION_CODE_TABLE[self.direction_code])
            # final_solution.append(self.direction_code)
            solution_list.append(final_solution)
        
        # ------ 转换为DataFrame ------ #
        df = pd.DataFrame(
            solution_list, 
            columns=[
                '第一个点tnt','第二个点tnt','第三个点tnt',
                'x动量','y动量','z动量', '方向',
            ]
        )

        # ------ 返回配置所需的TNT数量 ------ #
        return df
