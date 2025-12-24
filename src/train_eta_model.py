import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


def main() -> None:
    df = pd.read_csv(Path("data/shipments.csv"), parse_dates=["ship_date"])
    df["dow"] = df["ship_date"].dt.dayofweek

    df = pd.get_dummies(
        df,
        columns=["origin_hub", "destination_hub", "service_type"],
        drop_first=True,
    )

    y = df["actual_transit_days"]
    X = df.drop(columns=["actual_transit_days", "ship_date", "shipment_id"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=300, max_depth=6, random_state=42
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"ETA Model MAE: {mae:.3f} days, R²: {r2:.3f}")


if __name__ == "__main__":
    main()
