# AutoMotorSelectPro

Windows desktop motor selection demo software based on Python 3.12 + PySide6.

## Features
- Unit conversion
- Motion profile
- Ball screw / conveyor / turntable axis calculations
- Hard motor filtering rules
- Demo motor database with `DEMO_ONLY_NOT_FOR_ENGINEERING_USE` notice
- GUI pages: 项目概览页, 轴管理页, 计算结果页, 电机推荐页, BOM 页, 数据库管理页
- CLI smoke test for no-GUI environments

## Run
```bash
python -m pip install -r requirements.txt
python main.py --smoke-test
python main.py
```
