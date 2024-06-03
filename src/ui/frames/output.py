# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-02                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 结果输出界面           #
# =================================== #
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.modules.infotransform import ConfigInfoTransform


class ResultTreeViewFrame(ttk.Frame):

    def __init__(self, master) -> None:

        super().__init__(master)
        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        text = "配置信息结果输出"
        self.res_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5)
        )
        self.res_frame.columnconfigure(0, weight=1)
        self.res_frame.pack(fill=BOTH, expand=YES)
        self.details_frame = None
        self.scrollbar = None
        self.create_treeview()
    

    def create_treeview(self) -> None:

        # ------ 表头 ------ #
        columns = ("第一个点tnt", "第二个点tnt", "第三个点tnt", "方向")

        # ------ 创建Treeview ------ #
        self.treeview = ttk.Treeview(
            self.res_frame, columns=columns, show="headings"
        )
        self.treeview.pack(fill=BOTH, expand=YES)

        # ------ 设置列格式，确保对齐等 ------ #
        for col in columns:
            self.treeview.heading(col, text=col, anchor=CENTER)
            self.treeview.column(col, width=100, anchor=CENTER)
        
        # ------ 捕捉选中某一行，并绑定功能函数 ------ #
        self.treeview.bind("<<TreeviewSelect>>", self.on_item_selected)
        
    def load_res(self, config: pd.DataFrame) -> None:

        """
        与用户输入进行通信，实现结果互通
        """

        # ------ 清除Treeview中的旧数据 ------ #
        self.treeview.delete(*self.treeview.get_children())

        # ------ 从配置结果中获取信息 ------ #
        output_dataframe = config[
            ["第一个点tnt", "第二个点tnt", "第三个点tnt", "方向"]
        ]

        # ------ 将配置信息插入进先前创建的Treeview ------ #
        for _, row in output_dataframe.iterrows():
            self.treeview.insert(
                "", "end", values=(
                    row["第一个点tnt"], row["第二个点tnt"],
                    row["第三个点tnt"], row["方向"]
                )
            )
        
        # ------ 数据量可能较大，设置一个滚动条 ------ #
        if self.scrollbar:
            pass
        else:
            self.scrollbar = ttk.Scrollbar(
                self.treeview, orient="vertical", command=self.treeview.yview
            )
            self.scrollbar.pack(side='right', fill='y')
            self.treeview.configure(yscrollcommand=self.scrollbar.set)
    

    def on_item_selected(self, event) -> None:

        """
        当Treeview选中某一行时，将选中行的信息显示在小窗口中
        """

        # ------ 如果已经存在一个窗口，先销毁它 ------ #
        if self.details_frame:
            self.details_frame.destroy()

        # 获取选中行的标识符
        selected_item = self.treeview.focus()
        # 获取该行的值
        item_values = self.treeview.item(selected_item, 'values')
        
        # ------ 创建新的小窗口用于显示 ------ #
        # 获取主窗口的位置
        x, y = self.res_frame.winfo_rootx(), self.res_frame.winfo_rooty()
        # 获取主窗口的大小(宽度)
        width = self.res_frame.winfo_width()
        self.details_frame = ttk.Toplevel(self.res_frame)
        self.details_frame.title("详细信息")
        # 详细信息窗口将固定显示在主窗口的右侧
        self.details_frame.geometry(f"+{x + width + 10}+{y}")
        text_area = ttk.ScrolledText(self.details_frame, width=60, height=20)
        text_area.pack(padx=10, pady=10)

        # ------ 插入信息并设置禁止修改 ------ #
        res = ConfigInfoTransform(*item_values).res_strings
        text_area.insert(END, res)
        text_area.configure(state='disabled')
