
<table style="border: 1px solid transparent">
  <tr>
    <td>
<a href="https://talkytrader.github.io/wiki/"><img src="https://img.shields.io/badge/Wiki-%23000000.svg?style=for-the-badge&logo=wikipedia&logoColor=white"></a><br>
<a href="https://github.com/mraniki/iamlistening/"><img src="https://img.shields.io/badge/github-%23000000.svg?style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://hub.docker.com/r/mraniki/tt"><img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/mraniki/tt?style=for-the-badge"></a><br>
<a href="https://coindrop.to/mraniki"><img src="https://img.shields.io/badge/tips-000000?style=for-the-badge&logo=buymeacoffee&logoColor=white"></a>
<a href="https://t.me/TTTalkyTraderChat/1"><img src="https://img.shields.io/badge/talky-blue?style=for-the-badge&logo=telegram&logoColor=white"></a> <a href="https://discord.gg/gMNERs5M9"><img src="https://img.shields.io/discord/1049307055867035648?style=for-the-badge&logo=discord&logoColor=white&label=%20%20&color=blue"></a>
    </td>
    <td align="center"><img width="200" alt="Logo" src="https://user-images.githubusercontent.com/8766259/242846519-f76331f6-8821-49eb-8f1c-06aedd8557be.jpeg"></td>
  </tr>
  <tr>
    <td>
      <a href="https://pypi.org/project/iamlistening/"><img src="https://img.shields.io/pypi/v/iamlistening?style=for-the-badge&logo=PyPI&logoColor=white"></a><br>
      <a href="https://pypi.org/project/iamlistening/"><img src="https://img.shields.io/pypi/dm/iamlistening?style=for-the-badge&logo=PyPI&logoColor=white&label=pypi&labelColor=grey"></a><br>
      <a href="https://github.com/mraniki/iamlistening/"><img src="https://img.shields.io/github/actions/workflow/status/mraniki/iamlistening/%F0%9F%91%B7%E2%80%8D%E2%99%82%EF%B8%8FFlow.yml?style=for-the-badge&logo=GitHub&logoColor=white"></a><br>
   <a href="https://talky.readthedocs.io/"><img src="https://readthedocs.org/projects/iamlistening/badge/?version=latest&style=for-the-badge"></a><br>
   <a href="https://codebeat.co/projects/github-com-mraniki-iamlistening-main"><img src="https://codebeat.co/badges/4085334e-4590-41f6-a70c-69e9a2641c79"/></a><br>
   <a href="https://codecov.io/gh/mraniki/iamlistening"> <img src="https://codecov.io/gh/mraniki/iamlistening/branch/main/graph/badge.svg?token=QZ55U6KQFN"/></a><br>
    </td>
    <td align="left"> 
       A python package to listen to messaging platforms,<br>
       such as discord, telegram and matrix 
    </td>
     
  </tr>
</table>

<h5>How to use it</h5>
<pre>
<code>
      from iamlistening import Listener
        listener = Listener()
        task = asyncio.create_task(listener.run_forever())
        while True:
          try:
              msg = await listener.get_latest_message()
              if msg:
                  print(f"Frasier👂: {msg}"
          except Exception as error:
              print(error)
        await task
</code>
</pre>

<h5>Example</h5>

https://github.com/mraniki/iamlistening/blob/52db0f4c194fe9edd12f48199737b4e1c73f7194/examples/example.py#L1-L54

