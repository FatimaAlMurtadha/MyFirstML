from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path(__file__).with_name("car_price_dataset.csv")
NUMERIC_FEATURES = ["Year", "Engine_Size", "Mileage", "Doors", "Owner_Count"]
CATEGORICAL_FEATURES = ["Brand", "Model", "Fuel_Type", "Transmission"]
FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES


st.set_page_config(page_title="Car price predictor", page_icon=":material/directions_car:")
st.title("Car price predictor")
st.write("Enter the car details to estimate its price.")


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, sep=";")


@st.cache_resource
def train_model(data: pd.DataFrame) -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), NUMERIC_FEATURES),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
        ]
    )
    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=250,
                    min_samples_leaf=2,
                    random_state=42,
                    n_jobs=-1,
                ),
            ),
        ]
    )
    model.fit(data[FEATURES], data["Price"])
    return model


data = load_data()
model = train_model(data)

with st.form("car_details"):
    left, right = st.columns(2)
    with left:
        brand = st.selectbox("Brand", sorted(data["Brand"].unique()))
        car_model = st.selectbox("Model", sorted(data["Model"].unique()))
        year = st.number_input(
            "Year",
            min_value=int(data["Year"].min()),
            max_value=int(data["Year"].max()),
            value=int(data["Year"].median()),
            step=1,
        )
        engine_size = st.number_input(
            "Engine size",
            min_value=float(data["Engine_Size"].min()),
            max_value=float(data["Engine_Size"].max()),
            value=float(data["Engine_Size"].median()),
            step=0.1,
        )
        mileage = st.number_input(
            "Mileage",
            min_value=float(data["Mileage"].min()),
            max_value=float(data["Mileage"].max()),
            value=float(data["Mileage"].median()),
            step=100.0,
        )
    with right:
        fuel_type = st.selectbox("Fuel type", sorted(data["Fuel_Type"].unique()))
        transmission = st.selectbox(
            "Transmission", sorted(data["Transmission"].unique())
        )
        doors = st.number_input(
            "Doors",
            min_value=int(data["Doors"].min()),
            max_value=int(data["Doors"].max()),
            value=int(data["Doors"].median()),
            step=1,
        )
        owner_count = st.number_input(
            "Owner count",
            min_value=int(data["Owner_Count"].min()),
            max_value=int(data["Owner_Count"].max()),
            value=int(data["Owner_Count"].median()),
            step=1,
        )

    submitted = st.form_submit_button("Predict price", type="primary")

if submitted:
    input_data = pd.DataFrame(
        [
            {
                "Brand": brand,
                "Model": car_model,
                "Year": year,
                "Engine_Size": engine_size,
                "Fuel_Type": fuel_type,
                "Transmission": transmission,
                "Mileage": mileage,
                "Doors": doors,
                "Owner_Count": owner_count,
            }
        ]
    )
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated price: {prediction:,.0f}")
