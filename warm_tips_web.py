import tkinter as tk
import random
import threading
import time
import sys  # 用于退出程序

# 存储所有窗口实例的列表
all_windows = []
# 控制是否所有窗口都已创建的标志
all_created = False


def show_warm_tip():
    # 创建窗口
    window = tk.Tk()
    all_windows.append(window)  # 将窗口添加到列表

    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # 随机窗口位置（确保窗口完全显示在屏幕内）
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    # 设置窗口标题和大小位置
    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # 提示文字列表
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
        '梦想成真', '期待下一次见面', '金榜题名',
        '顺顺利利', '早点休息', '愿所有烦恼都消失',
        '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
    ]
    tip = random.choice(tips)
    # 多样的背景颜色
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)
    # 创建标签并显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()
    # 窗口置顶显示
    window.attributes('-topmost', True)

    # 绑定空格键事件，触发时退出所有窗口并终止程序
    def on_space(event):
        for win in all_windows:
            if win.winfo_exists():
                win.destroy()
        sys.exit()  # 退出程序

    window.bind('<space>', on_space)

    # 检查是否所有窗口都已创建，如果是则设置自动关闭
    def check_and_close():
        if all_created:
            # 每个窗口显示3秒后自动关闭（可调整时间）
            window.after(3000, window.destroy)
        else:
            # 未全部创建则继续检查
            window.after(100, check_and_close)

    check_and_close()
    window.mainloop()


def show_final_tip():
    final_window = tk.Tk()
    final_window.title('特别提示')
    final_window.geometry('300x100+300+300')
    final_window.attributes('-topmost', True)
    # 设置标签背景为粉红色（lightpink）
    tk.Label(
        final_window,
        text='恣瑶子想不想我呀！',
        font=('微软雅黑', 18),
        width=20,
        height=2,
        bg='lightpink'  # 新增粉红色背景
    ).pack()
    final_window.mainloop()


# 创建线程列表
threads = []
# 窗口数量（根据屏幕大小可调整）
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    time.sleep(0.01)  # 加快弹出速度
    threads[i].start()

# 所有窗口都已创建，设置标志
all_created = True

# 等待所有线程结束后显示最终窗口
for t in threads:
    t.join()
show_final_tip()
sys.exit()