import aiohttp

async def download_xhs(url):
    api = f"https://www.xhsdownload.com/api/download?url={url}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api) as resp:
                data = await resp.json()
                if not data.get("success"):
                    return "❌ Gagal download dari Xiaohongshu."
                return f"✅ Link video:\n{data['video_url']}"
        except Exception as e:
            return f"❌ Error Xiaohongshu: {str(e)}"
