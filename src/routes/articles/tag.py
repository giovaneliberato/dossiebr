from tekton.gae.middleware.json_middleware import JsonResponse

from articles import core


def search_tags(prefix):
    found_tags = [t.name for t in core.find_tags_by_prefix(prefix)]
    return JsonResponse(found_tags)
