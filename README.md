# discordpy-commands

discord.py 라이브러리를 위한 커맨드 처리기

## Usage

해당 커맨드가 작동할 조건을 표현한 정규표현식 문자열과, 작동할 coroutine function을 사용해 `Command` 객체를 만듭니다.

```py
command = Command(regex, coro)
```

여기서 함수 `coro` 가 받는 인자는 두 개입니다.

```
1. 해당 명령어가 작동하게 한 메시지 객체
2. 명령어에 주어진 인자들의 이름과 값을 담은 사전
```

인자를 받을 필요가 있는 경우에는 `(?P<인자명><조건>)` 을 사용합니다.<br>
예를 들어, 띄어쓰기 없는 하나의 단어 `word` 를 인자로 받고자 하는 경우에는

```py
command = Command('^!comm (?P<word>\s+)', coro)
```

와 같이 할 수 있습니다.

그리고, `discord.Client` 객체와 등록할 `Command` 객체들이 담긴 집합 (set) 을  넘겨 `CommandWrapper` 객체를 만듭니다.

```py
cw = CommandWrapper(client, set([command]))
```

또는 `CommandWrapper` 객체를 생성한 후에 `register_command` 메소드를 호출하여 명령어를 등록할 수 있습니다.

```py
cw.register_command(command)
```

그리고, 따로 `on_message` 이벤트를 처리해야 할 경우에는 이벤트 함수의 맨 끝에 `CommandWrapper.process_commands` 메소드를 호출하여 주면 됩니다.

```py
@client.event
async def on_message(message):
    # 이것저것 한 뒤...
    await cw.process_commands(message)
```
