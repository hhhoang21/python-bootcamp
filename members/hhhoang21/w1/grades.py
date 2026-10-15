
def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm không được để rỗng.")
    min_score =min(scores)
    max_score = max(scores)
    mean_score = round(sum(scores) / len(scores), 2)
    median_score = sorted(scores)[len(scores) // 2] if len(scores) % 2 != 0 else \
        (sorted(scores)[len(scores) // 2 - 1] + sorted(scores)[len(scores) // 2]) / 2
    return {
        "min": min_score,
        "max": max_score,
        "mean": mean_score,
        "median": median_score
    }