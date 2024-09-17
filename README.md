# Talos

# 项目介绍
python浏览器脚本

# 环境配置
## 创建虚拟环境并激活
```bash
    # MacOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate
```

## 安装依赖
    ```bash
    pip install -r requirements.txt
    ```

# build 命令
```shell
pyinstaller --onefile --add-binary "./chromedriver-mac-arm64/chromedriver:./chromedriver-mac-arm64" index.py
```

