import requests

# token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTc2MjMxMjEsInN1YiI6InRlc3RlciJ9.y-RbR2mbrDLqFuh2hMpLs8LErl5OJ2nA_3tH1Ooxi2A"
token="yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTc2MjY3NzQsInN1YiI6InRlc3RlciJ9.DDJCEeqTTRPEiVeji9avfiz1ZHW7kL_4cVCU0_5VGM0"
# request with token in header
# /me (get)
res = requests.get(
    "http://127.0.0.1:3000/me",
    headers={
        "Authorization": f"Bearer {token}"
    }
)
print(res.json())

