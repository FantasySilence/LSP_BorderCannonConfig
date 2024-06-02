# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-02                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 主程序的界面           #
# =================================== #
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO
from src.ui.frames.user_input import InputFrame
from src.ui.frames.output import ResultTreeViewFrame


class MainFrame(ttk.Frame):

    def __init__(self, master) -> None:

        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.create_page()

    def create_page(self) -> None:
        
        """
        创建画面
        """

        # ------ 加载图片 ------ #
        self.images = [
            ttk.PhotoImage(
                name="logo", file=FilesIO.getFigPath("Ender_Pearl.png")
            ),
        ]

        # ------ 创建窗口标题的容器 ------ #
        hdr_frame = ttk.Frame(self, bootstyle=INFO)
        hdr_frame.pack(fill=X, side=TOP, pady=5)
        # 向标题子容器中放入一幅logo图片
        hdr_label = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE, INFO)
        )
        hdr_label.pack(side=LEFT)
        # 向标题子容器中添加标题文字
        logo_text = ttk.Label(
            master=hdr_frame,
            text='LSP Hub边境珍珠炮配置器',
            font=('TkDefaultFixed', 30),
            bootstyle=(INVERSE, INFO)
        )
        logo_text.pack(side=LEFT, padx=15, ipadx=50)

        # ------ 创建存放用户输入与结果显示的容器 ------ #
        main_frame = ttk.Frame(self, bootstyle=LIGHT)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)
        main_frame.rowconfigure(0, weight=1)
        main_frame.pack(side=TOP, fill=BOTH, expand=YES)
        # 向主容器中添加结果显示子容器
        result_frame = ResultTreeViewFrame(main_frame)
        result_frame.grid(row=0, column=1, sticky=NSEW)
        # 向主容器中添加用户输入子容器
        input_frame = InputFrame(main_frame, result_frame)
        input_frame.grid(row=0, column=0, sticky=NSEW)
        
    
    @staticmethod
    def _show() -> None:
        root = ttk.Window(title="LSP_BorderConfig v1.0", size=(1000, 730))
        MainFrame(root)
        root.mainloop()

    @classmethod
    def show(cls) -> None:
        MainFrame._show()