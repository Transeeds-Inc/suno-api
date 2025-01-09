from typing import Any, Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None


class CustomModeGenerateParam(BaseModel):
    """Generate with Custom Mode"""

    prompt: str = Field(..., description="lyrics")
    mv: str = Field(
        default="chirp-v4",
        description="model version, default: chirp-v4",
        examples=["chirp-v4"],
    )
    title: str = Field(..., description="song title")
    tags: str = Field(..., description="style of music")
    continue_at: Optional[float] = Field(
        default=None,
        description="continue a new clip from a previous song, format number",
        examples=[120],
    )
    continue_clip_id: Optional[str] = None


class DescriptionModeGenerateParam(BaseModel):
    """Generate with Song Description"""

    prompt: str
    make_instrumental: bool = False
    mv: str = Field(
        default="chirp-v4",
        description="model version, default: chirp-v4",
        examples=["chirp-v4"],
    )
    title: str = Field(..., description="song title")


class ConcatParam(BaseModel):
    """Concatenate multiple songs"""

    clip_id: str
    is_infill: bool = False

class GenerateLyricsParam(BaseModel):
    prompt: str = Field(..., description="lyrics")

class ExtendParam(BaseModel):
    """Extend a song"""

    prompt: str
    make_instrumental: bool = False
    mv: str = Field(
        default="chirp-v4",
        description="model version, default: chirp-v4",
        examples=["chirp-v4"],
    )
    title: str = Field(..., description="song title")
    style: str = Field(..., description="style of music")
    audio_id: str
    continue_at: Optional[float] = Field(
        default=None,
        description="continue a new clip from a previous song, format number",
        examples=[120],
    )
