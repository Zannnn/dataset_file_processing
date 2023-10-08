@echo off
setlocal enabledelayedexpansion

rem 设置要处理的文件夹路径！还是放到指定文件夹吧
set "folder_path=D:\task\paper\ReadPaper\sketch\code\pytorch-CycleGAN-and-pix2pix-master\datasets\sketch_chair2photo\trainA"

rem 进入文件夹
cd "%folder_path%"

rem 遍历文件夹中的所有文件
for %%f in (*) do (
    rem 获取文件名（不含扩展名）
    set "filename=%%~nf"

    rem 删除文件名的最后两个字符
    set "new_filename=!filename:~0,-2!"

    rem 生成新的文件名
    ren "%%f" "!new_filename!%%~xf"
)

echo 文件名处理完成。
pause
