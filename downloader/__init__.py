import aiohttp

async def download_tiktok(url):
    async with aiohttp.ClientSession() as session:
        api = f"https://tikwm.com/api/?url={url}"
        try:
            async with session.get(api) as resp:
                data = await resp.json()
                if not data.get("data"):
                    return "❌ Gagal download video TikTok."
                video_url = data["data"]["play"]
                return f"✅ Video berhasil ditemukan:\n{video_url}"
        except Exception as e:
            return f"❌ Error TikTok: {str(e)}"
