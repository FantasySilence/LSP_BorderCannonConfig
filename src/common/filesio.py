# ================================================ #
# @Author: Fantasy_Silence                         #
# @Time: 2024-05-22                                #
# @IDE: Visual Studio Code & PyCharm               #
# @Python: 3.9.7                                   #
# ================================================ #
# @Description: 一个文件IO流类                      #
# ================================================ #
import os


class FilesIO:

    """
    实现一个文件IO流类用于文件管理
    """

    @staticmethod
    def getConfigSavePath(filename: str) -> str:

        src_path = os.path.dirname(os.path.dirname(__file__))
        ROOTPATH = os.path.dirname(src_path)
        resources_path = os.path.join(ROOTPATH, 'resources')
        config_path = os.path.join(resources_path, filename)
        return config_path

    @staticmethod
    def getFigPath(figname: str) -> str:

        src_path = os.path.dirname(os.path.dirname(__file__))
        ROOTPATH = os.path.dirname(src_path)
        images_path = os.path.join(ROOTPATH, 'images')
        fig_path = os.path.join(images_path, figname)
        return fig_path
