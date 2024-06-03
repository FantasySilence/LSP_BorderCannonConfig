# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-03                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 输入框输入验证         #
# =================================== #

def validate_number(x: str) -> bool:
    
    """
    验证输入的字符是否为数字
    """

    if x[1:].isdigit():
        return True
    elif x == "":
        return True
    else:
        return False
