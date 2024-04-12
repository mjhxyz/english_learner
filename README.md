# 英语辅助学习系统

## 开发环境部署

### 运行环境

- MySQL5.7
- Python3.8

### 数据库准备

1. 创建数据 `english_learner`
2. 导入 sql 数据 `sql/english_learner.sql`

### 环境配置

1. `app/config/__init__.py` 文件下配置自己的 MySQL 地址和密码
2. 安装依赖

```bash
# 安装依赖
pip install -r requirements.txt
```

### 开发运行

```bash
python app.py
```

### 账号说明

- mao 管理员 密码: 000000
- dfsef 普通用户 密码: 000000

