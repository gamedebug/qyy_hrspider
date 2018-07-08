#!/bin/bash

echo "================================"
echo "=         开始抓取任务         ="
echo "================================"
echo "任务一开始..."
python run_ali_bd.py
echo "任务一完成!!!"
echo "任务二开始..."
python run_baidu_bd.py
echo "任务二完成!!!"
echo "任务三开始..."
python run_didi_bd.py
echo "任务三完成!!!"
echo "任务四开始..."
python run_huawei_bd.py
echo "任务四完成!!!"
echo "任务五开始..."
python run_jd_bd.py
echo "任务五完成!!!"
echo "任务六开始..."
python run_meituan_bd.py
echo "任务六完成!!!"
echo "任务七开始..."
python run_tencent_bd.py
echo "任务七完成!!!"
