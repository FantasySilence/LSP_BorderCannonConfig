# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 设置界面               #
# =================================== #
import os
import sys
import json
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *
from src.common.input_validation import validate_number


class SettingsFrame(ttk.Frame):

    def __init__(self, master) -> None:
        
        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        # 珍珠初始位置
        self.x0_input = ttk.StringVar()
        self.y0_input = ttk.StringVar()
        self.z0_input = ttk.StringVar()
        # 目的地位置
        self.x_input = ttk.StringVar()
        self.y_input = ttk.StringVar()
        self.z_input = ttk.StringVar()
        # 预期飞行时间
        self.intended_time = ttk.StringVar()
        # 存放输入框的根容器
        self.frame = ttk.Labelframe(
            self, text="设置", padding=(10, 10)
        )
        self.frame.pack(fill=BOTH, expand=YES)
        self.validation_func = self.frame.register(validate_number)
        self.pack(fill=BOTH, expand=YES)
        self.create_page()

    def create_page(self) -> None:
        
        """
        创建页面
        """

        # ------ 输入珍珠初始位置的x坐标 ------ #
        x0_label = ttk.Label(
            master=self.frame, 
            text="输入珍珠默认初始x位置:", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x0_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        x0_input = ttk.Entry(
            master=self.frame, textvariable=self.x0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        x0_input.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入珍珠初始位置的y坐标 ------ #
        y0_label = ttk.Label(
            master=self.frame,
            text="输入珍珠默认初始y位置:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        y0_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        y0_input = ttk.Entry(
            master=self.frame, textvariable=self.y0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        y0_input.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入珍珠初始位置的z坐标 ------ #
        z0_label = ttk.Label(
            master=self.frame,
            text="输入珍珠默认初始z位置:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z0_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        z0_input = ttk.Entry(
            master=self.frame, textvariable=self.z0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        z0_input.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入目的地位置的x坐标 ------ #
        x_label = ttk.Label(
            master=self.frame,
            text="输入目的地的默认x坐标:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.frame, textvariable=self.x_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        x_input.grid(row=3, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入目的地位置的y坐标 ------ #
        y_label = ttk.Label(
            master=self.frame,
            text="输入目的地的默认y坐标:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        y_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        y_input = ttk.Entry(
            master=self.frame, textvariable=self.y_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        y_input.grid(row=4, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入目的地位置的z坐标 ------ #
        z_label = ttk.Label(
            master=self.frame,
            text="输入目的地的默认z坐标:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.frame, textvariable=self.z_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        z_input.grid(row=5, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入预期到达时间 ------ #
        intended_time_label = ttk.Label(
            master=self.frame,
            text="输入默认预期到达时间:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        intended_time_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)
        intended_time_input = ttk.Entry(
            master=self.frame, textvariable=self.intended_time, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        intended_time_input.grid(row=6, column=1, padx=5, pady=5, sticky=EW)

        # ------ 应用按钮 ------ #
        apply_button = ttk.Button(
            master=self.frame,
            text="应用",
            command=self.apply_settings,
            bootstyle=(PRIMARY, LIGHT),
        )
        apply_button.grid(
            row=7, column=0, padx=5, pady=5, sticky=EW, columnspan=2
        )
    
    def apply_settings(self) -> None:

        """
        应用设置
        """

        # ------ 读取现有的设置并进行修改 ------ #
        with open(
            "resources/settings/settings.json", mode="r"
        ) as file:
            settings = json.load(file)
            if self.x0_input.get() != '':
                settings["default_x_init"] = self.x0_input.get()
            if self.y0_input.get() != '':
                settings["default_y_init"] = self.y0_input.get()
            if self.z0_input.get() != '':
                settings["default_z_init"] = self.z0_input.get()
            if self.x_input.get() != '':
                settings["default_x_target"] = self.x_input.get()
            if self.y_input.get() != '':
                settings["default_y_target"] = self.y_input.get()
            if self.z_input.get() != '':
                settings["default_z_target"] = self.z_input.get()

        # ------ 将修改后的设置进行保存 ------ #
        with open(
            "resources/settings/settings.json", mode="w"
        ) as files:    
            json.dump(settings, files, indent=4)

        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)
