# ========================================================================== #
# @Author: Fantasy_Silence                                                   #
# @Time: 2024-05-21                                                          #
# @IDE: Visual Studio Code & PyCharm                                         #
# @Python: 3.9.7                                                             #
# ========================================================================== #
# @Description: 这里是主程序入口，用户在这里配置，仅适用于LSP边境计划2.0版        #
# ========================================================================== #
import pandas as pd
from src.common.filesio import FilesIO
from src.modules.calTNTnum import CalculateTNTNumber


# ------ 用户期待的珍珠落点与飞行时间 ------ #
x = float(input('输入您想到达的目标 x 轴位置\n'))
y = float(input('输入您想到达的目标 y 轴位置\n'))
z = float(input('输入您想到达的目标 z 轴位置\n'))
t = int(input('输入您希望珍珠飞行的时间\n'))

print('开始生成珍珠配置文件...')
TNT_solution = CalculateTNTNumber(x, y, z, t).TNT_num

df = pd.DataFrame(
    TNT_solution, 
    columns=[
        '第一个点tnt','第二个点tnt','第三个点tnt',
        'x动量','y动量','z动量', '方向',
    ]
)
df.to_csv(
    FilesIO.getConfigSavePath('LSP_BorderCannonConfig_SE.csv'), 
    index=False, encoding="utf-8"
)
print('珍珠配置文件生成完毕！')
