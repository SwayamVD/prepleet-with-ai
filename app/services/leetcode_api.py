import requests

URL = "https://leetcode.com/graphql"
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
}

# Get details for one problem by slug
def get_problem_details(slug):
    headers = DEFAULT_HEADERS.copy()
    headers["Referer"] = f"https://leetcode.com/problems/{slug}/"

    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        difficulty
        content
        hints
        solution {
            id
            content
            canSeeDetail
        }
        exampleTestcaseList
        topicTags {
          name
          slug
        }
        companyTagStats
        similarQuestionList {
          difficulty
          titleSlug
          title
        }
        codeSnippets {
          lang
          langSlug
        }
      }
    }
    """

    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": query,
    }

    resp = requests.post(URL, headers=headers, json=payload)
    data = resp.json()
    if resp.status_code != 200 or "errors" in data:
        return resp.status_code;
    return data["data"]["question"]


# Generic problemset query
PROBLEMSET_QUERY = """
query problemsetQuestionListV2(
  $filters: QuestionFilterInput,
  $limit: Int,
  $searchKeyword: String,
  $skip: Int,
  $sortBy: QuestionSortByInput,
  $categorySlug: String
) {
  problemsetQuestionListV2(
    filters: $filters
    limit: $limit
    searchKeyword: $searchKeyword
    skip: $skip
    sortBy: $sortBy
    categorySlug: $categorySlug
  ) {
    questions {
      id
      titleSlug
      title
      questionFrontendId
      difficulty
      acRate
    }
    totalLength
    hasMore
  }
}
"""

def get_problem_set(category=None, search=None, limit=20, skip=0):
    headers = DEFAULT_HEADERS.copy()
    headers["Referer"] = "https://leetcode.com/problemset/all/"

    variables = {
        "skip": skip,
        "limit": limit,
        "categorySlug": category or "all-code-essentials",
        "filters": {"filterCombineType": "ALL"},
        "sortBy": {"sortField": "CUSTOM", "sortOrder": "ASCENDING"},
    }
    if search:
        variables["searchKeyword"] = search

    payload = {
        "query": PROBLEMSET_QUERY,
        "variables": variables,
        "operationName": "problemsetQuestionListV2",
    }

    resp = requests.post(URL, headers=headers, json=payload)
    data = resp.json()
    if resp.status_code != 200 or "errors" in data:
        return None
    return data["data"]["problemsetQuestionListV2"]["questions"]

# Generic Favorite Problem Set
FAVORITE_SET = """
    query favoriteQuestionList(
    $favoriteSlug: String!, 
    $filter: FavoriteQuestionFilterInput, 
    $filtersV2: QuestionFilterInput, 
    $searchKeyword: String, 
    $sortBy: QuestionSortByInput, 
    $limit: Int, 
    $skip: Int, 
    $version: String = "v2") {
        favoriteQuestionList(
        favoriteSlug: $favoriteSlug
        filter: $filter
        filtersV2: $filtersV2
        searchKeyword: $searchKeyword
        sortBy: $sortBy
        limit: $limit
        skip: $skip
        version: $version
        ) {
        questions {
            difficulty
            id
            paidOnly
            questionFrontendId
            status
            title
            titleSlug
            translatedTitle
            isInMyFavorites
            frequency
            acRate
            contestPoint
            topicTags {
            name
            nameTranslated
            slug
            }
        }
        totalLength
        hasMore
        }
    }
"""

def get_favorite_set(fname=None, limit=20, skip=0):
    headers = DEFAULT_HEADERS.copy()
    headers["Referer"] = "https://leetcode.com/problemset/all/"

    variables = {
        "skip": skip,
        "limit": limit,
        "favoriteSlug": fname,
        "filters": {"filterCombineType": "ALL"},
        "sortBy": {"sortField": "CUSTOM", "sortOrder": "ASCENDING"},
    }

    payload = {
        "query": FAVORITE_SET,
        "variables": variables,
        "operationName": "favoriteQuestionList",
    }

    resp = requests.post(URL, headers=headers, json=payload)
    data = resp.json()
    if resp.status_code != 200 or "errors" in data:
        return None
    return data["data"]["favoriteQuestionList"]["questions"]