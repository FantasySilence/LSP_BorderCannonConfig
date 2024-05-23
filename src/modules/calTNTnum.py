# ============================================== #
# @Author: Fantasy_Silence                       #
# @Time: 2024-05-21                              #
# @IDE: Visual Studio Code & PyCharm             #
# @Python: 3.9.7                                 #
# ============================================== #
# @Description: 计算TNT的当量                     #
# ============================================== #
import numpy as np
from src.common.const import DIRECTION_ROTATION
from src.common.const import DIRECTION_CODE_TABLE
from src.modules.loadTNTmotion import LoadOneTNTMotion


class CalculateTNTNumber:

    """
    计算TNT当量
    """

    def __init__(self, x: float, y: float, z: float, t: int) -> None:
        
        """
        初始化
        x, y, z: 珍珠落点位置
        t: 预期珍珠飞行时间
        """

        self.x, self.y, self.z, self.t = x, y, z, t
        self.TNT_motion, self.direction_code = LoadOneTNTMotion.load(x, z)
        self.TNT_num = self.__cal__()
    

    def __cal__(self) -> list[list[int, str]]:

        """
        计算TNT当量
        """

        # ------ 初始位置 ------ #
        x0 = DIRECTION_ROTATION["X"]
        y0 = 178.34722638929412
        z0 = DIRECTION_ROTATION["Z"]

        solution_list = []
        for tick in range(self.t, self.t + 100):

            # ------ 计算配置珍珠炮所需动量 ------ #
            px = (self.x - x0)/(100 * (1 - 0.99 ** tick))
            py = (self.y - y0 + 3 * tick)/(100 * (1 - 0.99 ** tick) - 3)
            pz = (self.z - z0)/(100 * (1 - 0.99 ** tick))

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
            # # 如果需要输出方向的话
            # final_solution.append(DIRECTION_CODE_TABLE[self.direction_code])
            final_solution.append(self.direction_code)
            solution_list.append(final_solution)

        # ------ 返回配置所需的TNT数量 ------ #
        return solution_list
