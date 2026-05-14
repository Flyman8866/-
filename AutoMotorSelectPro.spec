# PyInstaller spec for AutoMotorSelectPro
block_cipher = None

a = Analysis(['main.py'])
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, name='AutoMotorSelectPro', console=False)
