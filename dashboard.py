import pandas as pd
import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Vision Guard AI",
    layout="wide"
)

st.title(
    "🛵 Vision Guard AI"
)

st.subheader(
    "Helmet Detection Monitoring Dashboard"
)

csv_file = Path("s3_logs.csv")

if not csv_file.exists():

    st.warning(
        "No violation logs found."
    )

else:

    df = pd.read_csv(csv_file)

    total_violations = len(df)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Violations",
            total_violations
        )

    with col2:

        st.metric(
            "System Status",
            "ACTIVE"
        )

    st.divider()

    st.subheader(
        "Violation Logs"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    if total_violations > 0:

        latest = df.iloc[-1]

        st.divider()

        st.subheader(
            "Latest Violation"
        )

        st.write(
            f"📅 Timestamp: {latest['timestamp']}"
        )

        st.write(
            f"🖼️ Image: {latest['image_name']}"
        )

        st.write(
            f"🔗 S3 URL:"
        )

        st.code(
            latest["s3_url"]
        )

        st.image(
            latest["s3_url"],
            caption="Latest Uploaded Violation",
            use_container_width=True
        )