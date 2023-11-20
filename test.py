import asyncio

from y2mate import Y2MateClient

client = Y2MateClient()

async def main() -> None:
    # Search for videos
    search_result = await client.search("The Girl I Like Forgot Her Glasses OP")
    print(search_result)
    
    # Get video metadata info from url
    video_metadata = await client.from_url("https://youtu.be/mpWnhkMLIu4?feature=shared")
    print(video_metadata)
    
    # Get video download info with download link
    download_info = await client.get_download_info(video_metadata.video_id, video_metadata.video_links[0].key)
    print(download_info)

asyncio.run(main())