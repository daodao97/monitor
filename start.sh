#!/bin/bash

# 设置环境变量
export GRAFANA_ADMIN_USER=admin
export GRAFANA_ADMIN_PASSWORD=admin123

echo "启动 Loki 监控系统..."
echo "Grafana 用户名: $GRAFANA_ADMIN_USER"
echo "Grafana 密码: $GRAFANA_ADMIN_PASSWORD"

# 构建并启动所有服务
docker-compose up --build -d

echo ""
echo "服务启动完成！"
echo ""
echo "访问地址："
echo "- Grafana: http://localhost:3001 (用户名: admin, 密码: admin123)"
echo "- Prometheus: http://localhost:9090"
echo "- Loki: http://localhost:3100"
echo "- Nginx 示例: http://localhost:8080"
echo ""
echo "查看日志："
echo "docker-compose logs -f sample-app"
echo "docker-compose logs -f nginx-app"
echo "docker-compose logs -f promtail"
echo ""
echo "停止服务："
echo "docker-compose down" 