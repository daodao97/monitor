#!/usr/bin/env python3
import json
import time
import random
import logging
from datetime import datetime
import sys

# 配置 JSON 格式的日志
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "service": "sample-app",
            "component": "main",
            "message": record.getMessage(),
            "trace_id": f"trace-{random.randint(1000, 9999)}",
            "span_id": f"span-{random.randint(100, 999)}",
            "user_id": random.choice(["user1", "user2", "user3", None]),
            "request_id": f"req-{random.randint(10000, 99999)}"
        }
        
        # 添加异常信息
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_entry, ensure_ascii=False)

# 设置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

def main():
    logger.info("应用程序启动")
    
    messages = [
        "用户登录成功",
        "处理订单请求",
        "数据库查询完成",
        "发送邮件通知",
        "缓存更新",
        "API 调用成功",
        "文件上传完成",
        "数据同步开始"
    ]
    
    levels = [
        (logging.INFO, 0.7),
        (logging.WARNING, 0.2),
        (logging.ERROR, 0.08),
        (logging.DEBUG, 0.02)
    ]
    
    counter = 0
    while True:
        try:
            # 随机选择日志级别
            level = random.choices([l[0] for l in levels], weights=[l[1] for l in levels])[0]
            message = random.choice(messages)
            
            if level == logging.ERROR:
                try:
                    # 模拟错误
                    raise ValueError(f"模拟错误: {message}")
                except Exception as e:
                    logger.error(f"处理失败: {message}", exc_info=True)
            else:
                logger.log(level, f"{message} - 计数器: {counter}")
            
            counter += 1
            
            # 随机等待时间
            time.sleep(random.uniform(1, 5))
            
        except KeyboardInterrupt:
            logger.info("应用程序停止")
            break
        except Exception as e:
            logger.error(f"未预期的错误: {str(e)}", exc_info=True)
            time.sleep(1)

if __name__ == "__main__":
    main() 