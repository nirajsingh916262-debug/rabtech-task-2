from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "raw" / "synthetic_students.csv"
OUTPUT = ROOT / "report" / "results.txt"

REQUIRED = {
    "student_id", "study_hours_per_week", "sleep_hours_per_night", "exam_score"
}

def load_and_validate():
    df = pd.read_csv(INPUT)
    if set(df.columns) != REQUIRED:
        raise ValueError(f"Unexpected schema: {list(df.columns)}")
    if df["student_id"].duplicated().any():
        raise ValueError("Duplicate student IDs found.")
    df = df.dropna(subset=[
        "study_hours_per_week", "sleep_hours_per_night", "exam_score"
    ])
    df = df[
        df["study_hours_per_week"].between(0, 80)
        & df["sleep_hours_per_night"].between(0, 24)
        & df["exam_score"].between(0, 100)
    ].copy()
    return df

def main():
    df = load_and_validate()
    r, p_corr = pearsonr(df["study_hours_per_week"], df["exam_score"])

    X = sm.add_constant(df[["study_hours_per_week", "sleep_hours_per_night"]])
    model = sm.OLS(df["exam_score"], X).fit()

    q01 = df["study_hours_per_week"].quantile(0.01)
    q99 = df["study_hours_per_week"].quantile(0.99)
    robust = df[df["study_hours_per_week"].between(q01, q99)].copy()
    Xr = sm.add_constant(robust[["study_hours_per_week", "sleep_hours_per_night"]])
    robust_model = sm.OLS(robust["exam_score"], Xr).fit()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        f.write("SYNTHETIC PIPELINE RESULT\n")
        f.write(f"valid_rows={len(df)}\n")
        f.write(f"pearson_r={r:.4f}\n")
        f.write(f"pearson_p={p_corr:.6g}\n")
        f.write(f"study_hours_coefficient={model.params['study_hours_per_week']:.4f}\n")
        ci = model.conf_int().loc["study_hours_per_week"]
        f.write(f"study_hours_ci95=[{ci.iloc[0]:.4f}, {ci.iloc[1]:.4f}]\n")
        f.write(f"study_hours_p={model.pvalues['study_hours_per_week']:.6g}\n")
        f.write(f"r_squared={model.rsquared:.4f}\n")
        f.write(f"robust_valid_rows={len(robust)}\n")
        f.write(f"robust_study_hours_coefficient={robust_model.params['study_hours_per_week']:.4f}\n")
    print(OUTPUT.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
