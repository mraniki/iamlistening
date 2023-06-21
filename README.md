# I Am Listening

| <img width="200" alt="Logo" src="https://github.com/mraniki/iamlistening/assets/8766259/f76331f6-8821-49eb-8f1c-06aedd8557be"> | A python package to listen to messaging platforms. |
| ------------- | ------------- |
|<br> [![wiki](https://img.shields.io/badge/🪙🗿-wiki-0080ff)](https://talkytrader.gitbook.io/talky/) [![Pypi](https://badgen.net/badge/icon/iamlistening?icon=pypi&label)](https://pypi.org/project/iamlistening/) ![Version](https://img.shields.io/pypi/v/iamlistening)<br>  ![Pypi](https://img.shields.io/pypi/dm/iamlistening)<br> [![Build](https://github.com/mraniki/iamlistening/actions/workflows/%E2%9C%A8Flow.yml/badge.svg)](https://github.com/mraniki/listening/actions/workflows/%E2%9C%A8Flow.yml) [![codecov](https://codecov.io/gh/mraniki/iamlistening/branch/main/graph/badge.svg?token=QZ55U6KQFN)](https://codecov.io/gh/mraniki/iamlistening) | build a client to interact with messaging platform|

Key features:

 - support discord, telegram and matrix platform

## Install

`pip install iamlistening`

## How to use it

```
  listener = Listener()
  task = asyncio.create_task(listener.run_forever())
  while True:
    try:
        msg = await listener.get_latest_message()
        if msg:
            print(f"Frasier👂: {msg}")

    except Exception as error:
        print(error)
  await task
  
```

### Example

[example](https://github.com/mraniki/iamlistening/blob/main/examples/example.py)

### Real use case

[TalkyTrader](https://github.com/mraniki/tt)

## Documentation


[![wiki](https://img.shields.io/badge/🪙🗿-wiki-0080ff)](https://talkytrader.gitbook.io/talky/)
