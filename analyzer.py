def analyze_data(df):
    if df.empty:
        return None

    total_hours = df["hours"].sum()
    avg_hours = df["hours"].mean()
    avg_focus = df["focus"].mean()
    consistency = df["hours"].std()

    # Subject summary
    subject_summary = df.groupby("subject")["hours"].sum().sort_values(ascending=False)

    # Productivity Score
    score = (avg_hours * 10) + (avg_focus * 10) - (consistency * 5 if consistency else 0)
    score = max(0, min(100, round(score, 2)))
    top_subject = subject_summary.index[0] if len(subject_summary) > 0 else "N/A"

    # Suggestions
    if score < 40:
        tip = "Low productivity → increase study time and consistency"
    elif score < 70:
        tip = "Moderate productivity → improve focus"
    else:
        tip = "High productivity → maintain routine"

    return {
        "total_hours": round(total_hours, 2),
        "avg_hours": round(avg_hours, 2),
        "consistency": round(consistency, 2) if consistency else 0,
        "productivity_score": score,
        "tip": tip,
        "subject_summary": subject_summary,
        "top_subject": top_subject
    }