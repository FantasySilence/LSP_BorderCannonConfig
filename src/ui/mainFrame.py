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
from src.ui.frames.settings import SettingsFrame
from src.ui.frames.output import ResultTreeViewFrame


class MainFrame(ttk.Frame):

    def __init__(self, master) -> None:

        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.pack(fill=BOTH, expand=YES)
        self.settings_window = None
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
        # 添加一个设置按钮，用户可以配置一些默认值
        settings_button = ttk.Button(
            master=hdr_frame,
            text="设置",
            command=self._func_settings,
        )
        settings_button.pack(side=RIGHT, padx=5, ipadx=10, ipady=8)

        # ------ 创建存放用户输入与结果显示的容器 ------ #
        self.main_frame = ttk.Frame(self, bootstyle=LIGHT)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=3)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=YES)
        # 向主容器中添加结果显示子容器
        result_frame = ResultTreeViewFrame(self.main_frame, width=700)
        result_frame.grid(row=0, column=1, sticky=NSEW)
        # 向主容器中添加用户输入子容器
        input_frame = InputFrame(self.main_frame, result_frame, width=300)
        input_frame.grid(row=0, column=0, sticky=NSEW)
    
    def _func_settings(self) -> None:
        
        """
        为设置按钮配置功能
        """

        # ------ 如果已经存在一个窗口，先销毁它 ------ #
        if self.settings_window:
            self.settings_window.destroy()

        # ------ 创建弹窗 ------ #
        self.settings_window = ttk.Toplevel(self.main_frame)
        self.settings_window.title("设置")
        
        # ------ 显示在主窗口的靠中心位置 ------ #
        x = self.main_frame.winfo_rootx() + self.main_frame.winfo_width() // 2
        y = self.main_frame.winfo_rooty()
        self.settings_window.geometry(f"+{x}+{y}")

        # ------ 创建页面 ------ #
        settings_frame = SettingsFrame(self.settings_window)
        settings_frame.pack(fill=BOTH, expand=YES)
        
    
    @staticmethod
    def _show() -> None:
        root = ttk.Window(title="LSP_BorderConfig v2.0", size=(1000, 730))
        root.resizable(False, False)
        MainFrame(root)
        root.mainloop()

    @classmethod
    def show(cls) -> None:
        MainFrame._show()
