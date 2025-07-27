import heapq

posts = [
    {"post_id": 1, "likes": 150, "comments": 20, "recency": 0.8},
    {"post_id": 2, "likes": 80,  "comments": 10, "recency": 0.9},
    {"post_id": 3, "likes": 200, "comments": 50, "recency": 0.6},
    {"post_id": 4, "likes": 20,  "comments": 2,  "recency": 0.95},
    {"post_id": 5, "likes": 300, "comments": 40, "recency": 0.7},
    {"post_id": 6, "likes": 400, "comments": 15, "recency": 0.85},
    ]

def get_top_k_posts(posts, k, relevance_fn):
    if k <= 0:
        return []

    min_heap = []  
    score_cache = {}

    for post in posts:
        pid = post['post_id']  
        if pid not in score_cache:
            score_cache[pid] = relevance_fn(post)
        score = score_cache[pid]

        if len(min_heap) < k:
            heapq.heappush(min_heap, (score, post))
        else:
            if score > min_heap[0][0]:  
                heapq.heappushpop(min_heap, (score, post))

    return [post for _, post in sorted(min_heap, key=lambda x: -x[0])]

def relevance_score(post):
    return post["likes"] * 0.5 + post["comments"] * 0.3 + post["recency"] * 100 * 0.2

top_posts = get_top_k_posts(posts, k=3, relevance_fn=relevance_score)
print("\nTop K posts using Min-Heap:")
for p in top_posts:
    print(p, "Relevance:", relevance_score(p))
