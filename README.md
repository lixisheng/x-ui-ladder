# x-ui Ladder

Docker 化的 x-ui 梯子管理项目，用于在服务器上部署 x-ui 面板，并给电脑/手机上的 v2rayNG 添加节点。

## 端口

- x-ui Web 面板：`25143`，访问地址 `http://127.0.0.1:25143` 或 `http://<server-ip>:25143`
- 预留 v2rayNG 节点端口：`10086/tcp+udp`
- 预留 REALITY/TLS 节点端口：`9443/tcp+udp`
- 当前已创建节点：电脑端 `46274/tcp+udp`，移动端 `25776/tcp+udp`

> 本项目已经按你的要求把 Web 端访问端口设为 `25143`。

## 启动

```bash
cp .env.example .env
./scripts/start.sh
```

健康检查：

```bash
./scripts/healthcheck.sh
```

停止：

```bash
./scripts/stop.sh
```

## v2rayNG 使用

1. 浏览器打开 `http://<server-ip>:25143` 登录 x-ui。
2. 在 x-ui 中创建 VLESS/VMess/Trojan/Reality 等入站。
3. 复制分享链接或二维码。
4. 电脑或手机 v2rayNG 导入链接/扫码。
5. 连接后在 v2rayNG 内测试延迟和连通性。

## 数据说明

- `db/`：x-ui 运行数据库和配置，已加入 `.gitignore`，不会上传 GitHub。
- `cert/`：证书目录，已加入 `.gitignore`，不会上传 GitHub。
- `.env`：本机端口配置，已加入 `.gitignore`；仓库只提交 `.env.example`。

## 扫码后连不上时先检查

如果 x-ui 节点使用了新端口，必须同时在 `docker-compose.yml` / `.env` 中发布这个端口，然后重启容器。当前移动端节点端口是 `25776`，电脑端节点端口是 `46274`。
