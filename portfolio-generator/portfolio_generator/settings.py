"""
Defines schemas for the configuration file that is the input to the static site generator
"""
from pathlib import Path
from typing import List, Optional, Set

import toml
from pydantic import BaseModel, Field, ValidationError, HttpUrl

from .resource_fetchers import RESOURCE_TYPE_FETCHERS


class ResourceSetting(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    destination: str = Field("resources/")
    add_unique_id: bool = Field(False)
    resource_type: str = Field(...)
    extra: dict = Field(...)

    def validate_resource_type(self, value):
        if value not in RESOURCE_TYPE_FETCHERS:
            raise ValidationError(
                "Resource type must be one of: {', '.join(VALID_RESOURCE_TYPES)}, not {value}",
                self.__class__,
            )


class ProfileJob(BaseModel):
    title: str = Field(..., description="Your current job title")
    employer: str = Field(..., description="The name of your employer")
    employer_link: Optional[str] = Field(
        None, description="The url to your employer's homepage"
    )


class ProfileInterest(BaseModel):
    name: str = Field(..., description="The name of your interest")
    link: Optional[str] = Field(
        None, description="A link to more info about your interest"
    )
    brief: Optional[str] = Field(
        None, description="More information about this interest"
    )


class ProfileSocialLinks(BaseModel):
    github_url: Optional[HttpUrl] = Field(
        None, description="The link to your github profile"
    )
    linkedin_url: Optional[HttpUrl] = Field(
        None, description="The link to your linkedin profile"
    )
    email: Optional[str] = Field(None, description="Your email address")


class PortfolioProfile(BaseModel):
    job: Optional[ProfileJob]
    interests: List[ProfileInterest]
    social_links: ProfileSocialLinks


class PortfolioGenSettings(BaseModel):
    resource_settings: List[ResourceSetting]
    profile: PortfolioProfile

    def validate_resource_settings(self, resource_settings: List[ResourceSetting]):
        seen_settings: Set[str] = set()
        for resource_setting in resource_settings:
            if resource_setting.name in seen_settings:
                raise ValidationError(
                    f"Found duplicate resource name: {resource_setting.name}",
                    self.__class__,
                )

            seen_settings.add(resource_setting.name)

    @classmethod
    def from_toml(cls, path: Path) -> "PortfolioGenSettings":
        return cls(**toml.load(path.absolute()))
