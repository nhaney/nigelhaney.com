"""
High level integration tests of portfolio generator.
"""
from pathlib import PosixPath

from portfolio_generator.settings import PortfolioGenSettings

from .conftest import TEST_CONFIG, TEST_OUTPUT_DIR


def test_config_profile_values_appear_in_output():
    """Tests that profile values from the configuration file are filled in properly."""
    config = PortfolioGenSettings.from_toml(TEST_CONFIG)

    rendered_about_me_page = PosixPath.joinpath(
        TEST_OUTPUT_DIR, "about", "index.html"
    ).read_text()

    # job info is on the page
    job_info = config.profile.job
    assert job_info.title in rendered_about_me_page
    assert job_info.employer in rendered_about_me_page
    if job_info.employer_link:
        assert job_info.employer_link in rendered_about_me_page

    # interests are on the page
    interests = config.profile.interests
    for interest in interests:
        assert interest.name
        if interest.brief:
            assert interest.brief in rendered_about_me_page
        if interest.link:
            assert interest.link in rendered_about_me_page

    # social links are on the page
    social_links = config.profile.social_links

    if social_links.github_url:
        assert social_links.github_url in rendered_about_me_page

    if social_links.email:
        assert social_links.email in rendered_about_me_page

    if social_links.linkedin_url:
        assert social_links.linkedin_url in rendered_about_me_page

    assert job_info.employer in rendered_about_me_page


def test_expected_files_appear_in_output():
    """Tests expected files are found in output directory and no extra files are added"""
    expected_files = ["index.html", "about/index.html"]

    for expected_file in expected_files:
        assert PosixPath.joinpath(TEST_OUTPUT_DIR, expected_file).exists()

    assert len(expected_files) == len([p for p in TEST_OUTPUT_DIR.rglob("*.*")])
