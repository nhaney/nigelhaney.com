from .google_doc import GoogleDocExportFetcher
from .github_actions import GitHubActionsArtifactFetcher

RESOURCE_TYPE_FETCHERS = {
    "google_doc": GoogleDocFetcher,
    "github_actions_artifact": GitHubActionsArtifactFetcher,
}
