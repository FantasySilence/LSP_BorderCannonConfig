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
from src.modules.infotransform import ConfigInfoTransform


# ------ 用户期待的珍珠落点与飞行时间 ------ #
x = float(input('输入您想到达的目标 x 轴位置\n'))
y = float(input('输入您想到达的目标 y 轴位置\n'))
z = float(input('输入您想到达的目标 z 轴位置\n'))
t = int(input('输入您希望珍珠飞行的时间\n'))

print('开始生成珍珠配置文件...')
TNT_solution = CalculateTNTNumber(x, y, z, t).TNT_num

# TODO：方向配置直接输出二进制码?
df = pd.DataFrame(
    TNT_solution, 
    columns=[
        '第一个点tnt','第二个点tnt','第三个点tnt',
        'x动量','y动量','z动量', '方向',
    ]
)
df.to_csv(
    FilesIO.getConfigSavePath('LSP_BorderCannonConfig_NE.csv'), 
    index=False, encoding="utf-8"
)
print('珍珠配置文件生成完毕！')

flag = input("是否翻译配置信息(Y/N): ")
if flag.lower() == "y":
    tnt_1 = int(input("输入第一个TNT落点的当量: \n"))
    tnt_2 = int(input("输入第二个TNT落点的当量: \n"))
    tnt_3 = int(input("输入第三个TNT落点的当量: \n"))
    ConfigInfoTransform(tnt_1, tnt_2, tnt_3)
else:
    pass
