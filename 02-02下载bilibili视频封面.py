import requests

def download_bilibili_cover(bvid):
    api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        cover_url = data["data"]["pic"]
        # 下载封面
        res = requests.get(cover_url)
        with open(f"cover_{bvid}.jpg", "wb") as f:
            f.write(res.content)
        print("封面下载成功！")
    else:
        print("请求失败，错误码：", response.status_code)

# 使用示例（直接传入BV号）
download_bilibili_cover("BV1GJ411x7h7")
