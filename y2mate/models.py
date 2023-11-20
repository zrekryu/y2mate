from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class VideoInfo:
    video_id: str
    title: str
    
    def get_thumbnail_url(self: "RelatedVideos") -> str:
        return f"https://i.ytimg.com/vi/{self.video_id}/0.jpg"

@dataclass
class SearchResult:
    query: str
    videos: List[VideoInfo]

@dataclass
class LinkInfo:
    size: str
    format: str
    quality: str
    key: str

@dataclass
class VideoMetadata:
    video_id: str
    title: str
    video_links: List[LinkInfo]
    audio_links: List[LinkInfo]
    other_links: List[LinkInfo]
    related_videos: Optional[List[VideoInfo]] = field(default=None)
    
    def get_thumbnail_url(self: "VideoDetails") -> str:
        return f"https://i.ytimg.com/vi/{self.video_id}/0.jpg"

@dataclass
class VideoDownloadInfo:
    video_id: str
    title: str
    format: str
    quality: str
    download_link: str
    
    def get_thumbnail_url(self: "VideoDetails") -> str:
        return f"https://i.ytimg.com/vi/{self.video_id}/0.jpg"