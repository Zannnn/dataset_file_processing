@echo off
setlocal EnableDelayedExpansion

set folder=D:\task\paper\ReadPaper\sketch\code\pytorch-CycleGAN-and-pix2pix-master\datasets\sketch_chair2photo\trainA

for /F "delims=" %%I in ('dir /b %folder%') do (
  set name=%%~nI
  if "!name:~-1!" NEQ "1" (
    del "%folder%\%%I"
  ) 
)