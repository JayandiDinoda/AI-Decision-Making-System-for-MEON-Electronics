# build.spec
import os
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

block_cipher = None

a = Analysis(
    ['app/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('knowledge_base/raw',    'knowledge_base/raw'),
        ('knowledge_base/chroma_db', 'knowledge_base/chroma_db'),
        ('config.py',             '.'),
    ],
    hiddenimports=[
        'sentence_transformers',
        'chromadb',
        'langchain',
        'langchain_community',
        'langchain_community.document_loaders',
        'langchain_community.embeddings',
        'langchain_community.vectorstores',
        'reportlab',
        'ollama',
        'PyQt6',
        'pypdf',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DecisionSupportSystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,   # no black terminal window
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DecisionSupportSystem',
)
