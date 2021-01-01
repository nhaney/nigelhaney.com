from pathlib import Path, PosixPath
import shutil

from portfolio_generator.main import main
import pytest

TEST_CONFIG: PosixPath = PosixPath.joinpath(
    PosixPath(__file__).parent, "portfolio.toml"
)
TEST_SRC_DIR: PosixPath = PosixPath.joinpath(PosixPath(__file__).parent, "example_site")
TEST_OUTPUT_DIR: PosixPath = PosixPath.joinpath(
    PosixPath(__file__).parent, "test_output"
)


@pytest.fixture(scope="session", autouse=True)
def generate_site(request):
    """Generates the site and puts the output of generation in the TEST_OUTPUT_DIR location"""
    request.addfinalizer(remove_test_output_directory)
    main(site_dir=TEST_SRC_DIR, output_dir=TEST_OUTPUT_DIR, config=TEST_CONFIG)


def remove_test_output_directory():
    """Cleans up the TEST_OUTPUT_DIR location after all tests have finished running"""
    if TEST_OUTPUT_DIR.exists():
        shutil.rmtree(TEST_OUTPUT_DIR)
