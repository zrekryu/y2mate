from httpx import AsyncClient

from .constants import ANALYZE_URL, CONVERT_URL
from .models import (
    SearchResult,
    VideoInfo,
    VideoMetadata,
    LinkInfo,
    VideoDownloadInfo
    )

class Y2MateClient:
    """
    An unofficial API wrapper for Y2Mate.com
    """
    def __init__(self: "Y2MateClient", analyze_url: str = ANALYZE_URL, convert_url: str = CONVERT_URL, language_code: str = "en") -> None:
        """
        Initialize the Y2MateClient.
        
        Parameters:
            analyze_url (str): The URL for video analysis.
            convert_url (str): The URL for video conversation.
            language_code (str): The language code. Defaults to "en".
        """
        self.analyze_url = ANALYZE_URL
        self.convert_url = CONVERT_URL
        self.language_code = language_code
        
        self.client = AsyncClient(timeout=60)
    
    async def search(self: "Y2MateClient", query: str) -> SearchResult:
        """
        Search for videos.
        
        Parameters:
            query (str): The search query.
        
        Raises:
            Exception: If something goes wrong with the y2mate API.
            HTTPError: If there's an error with the HTTP request.
        
        Returns:
            SearchResult: Information about the search result.
        """
        data = {
            "k_query": query,
            "k_page": "home",
            "hl": self.language_code,
            "q_auto": False
        }
        response = await self.client.post(self.analyze_url, data=data)
        response.raise_for_status()
        api_data = response.json()
        
        if api_data.get("mess"):
            raise Exception(api_data["mess"])
        
        return SearchResult(
            query=query,
            videos=[VideoInfo(
                video_id=info["v"],
                title=info["t"]
                ) for info in api_data["vitems"]]
            )
    
    async def from_url(self: "Y2MateClient", url: str) -> VideoMetadata:
        """
        Get video metadata from a URL.
        
        Parameters:
            url (str): The video URL.
        
        Raises:
            Exception: If something goes wrong with the y2mate API.
            HTTPError: If there's an error with the HTTP request.
        
        Returns:
            VideoMetadata: Information about the video.
        """
        data = {
            "k_query": url,
            "k_page": "home",
            "hl": self.language_code,
            "q_auto": False
        }
        response = await self.client.post(self.analyze_url, data=data)
        response.raise_for_status()
        api_data = response.json()
        
        if api_data.get("mess"):
            raise Exception(api_data["mess"])
        
        video_links = []
        for key in api_data["links"]["mp4"]:
            info = api_data["links"]["mp4"][key]
            video_links.append(
                LinkInfo(
                    size=info["size"],
                    format=info["f"],
                    quality=info["q"],
                    key=info["k"]
                    )
                )
        
        audio_links = []
        for key in api_data["links"]["mp3"]:
            info = api_data["links"]["mp3"][key]
            audio_links.append(
                LinkInfo(
                    size=info["size"],
                    format=info["f"],
                    quality=info["q"],
                    key=info["k"]
                    )
                )
        
        other_links = []
        for key in api_data["links"]["other"]:
            info = api_data["links"]["other"][key]
            other_links.append(
                LinkInfo(
                    size=info["size"],
                    format=info["f"],
                    quality=info["q"],
                    key=info["k"]
                    )
                )
        
        return VideoMetadata(
            video_id=api_data["vid"],
            title=api_data["title"],
            video_links=video_links,
            audio_links=audio_links,
            other_links=other_links,
            related_videos=[VideoInfo(
                video_id=info["v"],
                title=info["t"]
                ) for info in api_data["related"][0]["contents"]]
            )
    
    async def get_download_info(self: "Y2MateClient", video_id: str, key: str) -> VideoDownloadInfo:
        """
        Get information about the video along with download link.
        
        Parameters:
            video_id (str): The ID of the video.
            key (str): The key of the video from analytics.
        
        Raises:
            Exception: If something goes wrong with the y2mate API.
            HTTPError: If there's an error with the HTTP request.
        
        Returns:
            VideoDownloadInfo: Information about the video including video download link.
        """
        data = {
            "vid": video_id,
            "k": key
        }
        response = await self.client.post(self.convert_url, data=data)
        response.raise_for_status()
        api_data = response.json()
        
        if api_data.get("mess"):
            raise Exception(api_data["mess"])
        
        return VideoDownloadInfo(
            video_id=api_data["vid"],
            title=api_data["title"],
            format=api_data["ftype"],
            quality=api_data["fquality"],
            download_link=api_data["dlink"]
            )