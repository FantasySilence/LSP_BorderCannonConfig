# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-02                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 用户输入界面           #
# =================================== #
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *
from src.modules.calTNTnum import CalculateTNTNumber


class InputFrame(ttk.Frame):

    def __init__(self, master, res_page):
        
        # ------ 创建输入窗口的根容器 ------ #
        super().__init__(master)
        self.x0_input = ttk.StringVar(value="0")
        self.y0_input = ttk.StringVar(value="178.34722638929412")
        self.z0_input = ttk.StringVar(value="0")
        self.x_input = ttk.StringVar(value="0")
        self.y_input = ttk.StringVar(value="0")
        self.z_input = ttk.StringVar(value="0")
        self.intended_time = ttk.StringVar(value="0")

        # ------ 与结果显示页面建立通信 ------ #
        self.res_output_frame = res_page

        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        text = "输入珍珠的坐标与预期飞行时间"
        self.input_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5)
        )
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.pack(fill=BOTH, expand=YES)
        self.create_page()
    
    def create_page(self):

        # ------ 配置珍珠炮炮口的初始位置 ------ #
        self.original_config()

        # ------ 配置珍珠炮炮口的目标位置 ------ #
        self.target_config()
        
        # 输入珍珠的预计飞行时间坐标
        time_label = ttk.Label(
            master=self.input_frame, 
            text="预计飞行时间(gt)：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        time_label.grid(row=12, column=0, padx=5, pady=5, sticky=W)
        time_input = ttk.Entry(
            master=self.input_frame, textvariable=self.intended_time, width=10
        )
        time_input.grid(row=13, column=0, padx=5, pady=(0, 10), sticky=EW)
        
        # ------ 计算TNT当量按钮 ------ #
        calc_button = ttk.Button(
            master=self.input_frame,
            text="计算TNT当量",
            bootstyle=(INFO, OUTLINE),
            command=self._func_calc_button
        )
        calc_button.grid(row=14, column=0, padx=5, pady=5, sticky=EW)
        
        # ------ 退出按钮 ------ #
        exit_button = ttk.Button(
            master=self.input_frame,
            text="退出",
            bootstyle=(DANGER, OUTLINE),
            command=quit
        )
        exit_button.grid(row=15, column=0, padx=5, pady=(5, 10), sticky=EW)

    
    def original_config(self):

        # 输入珍珠x坐标
        x_label = ttk.Label(
            master=self.input_frame, 
            text="炮口X坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.input_frame, textvariable=self.x0_input, width=10
        )
        x_input.grid(row=1, column=0, padx=5, pady=5, sticky=EW)
        # 输入珍珠y坐标
        y_label = ttk.Label(
            master=self.input_frame, 
            text="炮口Y坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        y_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        y_input = ttk.Entry(
            master=self.input_frame, textvariable=self.y0_input, width=10
        )
        y_input.grid(row=3, column=0, padx=5, pady=5, sticky=EW)
        # 输入珍珠z坐标
        z_label = ttk.Label(
            master=self.input_frame, 
            text="炮口Z坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.input_frame, textvariable=self.z0_input, width=10
        )
        z_input.grid(row=5, column=0, padx=5, pady=5, sticky=EW)


    def target_config(self):

        # 输入目标x坐标
        x_label = ttk.Label(
            master=self.input_frame, 
            text="目标X坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.input_frame, textvariable=self.x_input, width=10
        )
        x_input.grid(row=7, column=0, padx=5, pady=5, sticky=EW)
        # 输入目标y坐标
        y_label = ttk.Label(
            master=self.input_frame, 
            text="目标Y坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        y_label.grid(row=8, column=0, padx=5, pady=5, sticky=W)
        y_input = ttk.Entry(
            master=self.input_frame, textvariable=self.y_input, width=10
        )
        y_input.grid(row=9, column=0, padx=5, pady=5, sticky=EW)
        # 输入目标z坐标
        z_label = ttk.Label(
            master=self.input_frame, 
            text="目标Z坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z_label.grid(row=10, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.input_frame, textvariable=self.z_input, width=10
        )
        z_input.grid(row=11, column=0, padx=5, pady=5, sticky=EW)


    def _func_calc_button(self):

        """
        "计算TNT当量"按钮的功能
        """

        config = CalculateTNTNumber(
            float(self.x_input.get()), float(self.y_input.get()), 
            float(self.z_input.get()), int(self.intended_time.get()), 
            float(self.x0_input.get()), float(self.y0_input.get()),
            float(self.z0_input.get()),
        ).TNT_num

        # ------ 与结果展示frame进行通信，确保结果以Treeview的形式展现 ------ #
        self.res_output_frame.load_res(config)
