# quant-common

> 퀀트 공통 모듈

## Install

```bash
pip install git+https://github.com/dalcon10028/quant-common.git
```

## 지원 모듈

- `discord`: 디스코드 웹훅 모듈
- `exception`: 공통 예외 모듈

## 사용법

### Discord
```python
from quant_common import discord

discord.send_info('message', {'key': 'value'}) # 디스코드 메시지 전송
```
