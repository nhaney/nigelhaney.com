"""
Defines schemas for the configuration file that is the input to the static site generator
"""
from pathlib import Path
from typing import List, Optional

import toml
from pydantic import BaseModel, Field, ValidationError

from .resource_fetchers import RESOURCE_TYPE_FETCHERS


class PortfolioResource(BaseModel):
    """
    "name": "resume.pdf", // will be generated as resume-5c7e1696.pdf
    "destination": "<resource path>", // path in built directory where this resource will be located. Defaults to `resources/`
    "resource_type": "googledoc", // there are different types of resources that will be pluggable to the generator
    "info": { // info is extra data needed to get the google doc
        "document_id": <google doc id>
    }
    """

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
    github_url: Optional[str] = Field(
        ..., description="The link to your github profile"
    )
    linkedin_url: Optional[str] = Field(
        ..., description="The link to your linkedin profile"
    )
    email: Optional[str] = Field(..., description="Your email address")


class PortfolioProfile(BaseModel):
    job: Optional[ProfileJob]
    interests: List[ProfileInterest]
    social_links: ProfileSocialLinks


class PortfolioGenSettings(BaseModel):
    #  resources: List[PortfolioResource]
    profile: PortfolioProfile

    @classmethod
    def from_toml(cls, path: Path) -> "PortfolioGenSettings":
        return cls(**toml.load(path.absolute()))
