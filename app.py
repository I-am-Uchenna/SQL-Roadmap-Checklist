import streamlit as st
import json
from io import BytesIO

st.set_page_config(page_title="SQL Roadmap Checklist", page_icon="🧠", layout="wide")

st.title("📊 SQL Roadmap Learning Checklist")
st.markdown("Follow this interactive roadmap to master SQL — from beginner basics to advanced analytics.")

# Initialize session state
if "checked" not in st.session_state:
    st.session_state.checked = {}

# Define roadmap levels and topics with resource links
roadmap = {
    "🟢 Beginner Level": [
        ("What is SQL?", "Learn what SQL is, how it's used in databases, and why it's essential for data analysis.", "https://www.w3schools.com/sql/sql_intro.asp"),
        ("SELECT Statements", "Retrieve specific data from one table using the SELECT keyword.", "https://www.w3schools.com/sql/sql_select.asp"),
        ("Filtering with WHERE", "Narrow down data using conditional logic with WHERE.", "https://www.w3schools.com/sql/sql_where.asp"),
        ("Logical Operators", "Use AND, OR, and NOT to combine multiple conditions.", "https://www.w3schools.com/sql/sql_and_or.asp"),
        ("Sorting with ORDER BY", "Sort your query results in ascending or descending order.", "https://www.w3schools.com/sql/sql_orderby.asp"),
        ("Limiting Results with LIMIT", "Control how many rows are returned. Useful for previews.", "https://www.w3schools.com/sql/sql_top.asp"),
        ("NULL and IS NULL", "Handle missing or unknown data using IS NULL / IS NOT NULL.", "https://www.w3schools.com/sql/sql_null_values.asp")
    ],
    "🟡 Intermediate Level": [
        ("GROUP BY", "Aggregate rows into groups and perform summary calculations.", "https://www.w3schools.com/sql/sql_groupby.asp"),
        ("COUNT, SUM, AVG, MIN, MAX", "Summarize data using aggregate functions.", "https://www.w3schools.com/sql/sql_count_avg_sum.asp"),
        ("HAVING Clause", "Filter groups after aggregation (like WHERE for groups).", "https://www.w3schools.com/sql/sql_having.asp"),
        ("INNER JOIN", "Combine rows from two tables based on related columns.", "https://www.w3schools.com/sql/sql_join_inner.asp"),
        ("LEFT JOIN", "Get all records from one table, even if there's no match.", "https://www.w3schools.com/sql/sql_join_left.asp"),
        ("RIGHT & FULL JOIN", "Learn variations of joins to handle different use cases.", "https://www.w3schools.com/sql/sql_join_right.asp"),
        ("Subqueries", "Nest queries inside others for advanced logic.", "https://www.w3schools.com/sql/sql_subqueries.asp")
    ],
    "🔴 Advanced Level": [
        ("Window Functions", "Perform calculations across rows without grouping (e.g. RANK(), ROW_NUMBER()).", "https://mode.com/sql-tutorial/sql-window-functions/"),
        ("CTEs (WITH Clauses)", "Use Common Table Expressions to simplify complex queries.", "https://www.w3schools.com/sql/sql_cte.asp"),
        ("CASE Statements", "Create conditional logic in SELECT statements.", "https://www.w3schools.com/sql/sql_case.asp"),
        ("Date & Time Functions", "Work with dates, timestamps, and intervals.", "https://www.w3schools.com/sql/sql_dates.asp"),
        ("COALESCE & NULLIF", "Handle missing values smartly.", "https://www.w3schools.com/sql/func_sqlserver_coalesce.asp"),
        ("UNION & UNION ALL", "Combine multiple result sets into one.", "https://www.w3schools.com/sql/sql_union.asp"),
        ("Temporary Tables", "Store intermediate results during query processing.", "https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql")
    ],
    "🏁 Real World & Optimization": [
        ("Indexing Basics", "Speed up queries by indexing the right columns.", "https://www.geeksforgeeks.org/sql-indexes/"),
        ("EXPLAIN Plans", "See how your query is being executed.", "https://www.geeksforgeeks.org/sql-explain/"),
        ("SQL in Data Analysis", "Use SQL in analytics, BI, dashboards, and storytelling.", "https://mode.com/sql-tutorial/introduction-to-sql/"),
        ("Writing Clean SQL", "Style, formatting, and readability tips.", "https://towardsdatascience.com/how-to-write-better-sql-queries-a92058c2759c"),
        ("Security (SQL Injection)", "Learn how bad queries can be abused and how to stay safe.", "https://owasp.org/www-community/attacks/SQL_Injection")
    ]
}

# Count all topics
total_topics = sum(len(topics) for topics in roadmap.values())
checked_count = 0

# Display sections
for level, topics in roadmap.items():
    st.subheader(level)
    for title, description, link in topics:
        key = f"{level}_{title}"
        checked = st.checkbox(f"**{title}**", value=st.session_state.checked.get(key, False), key=key)
        st.caption(f"{description} → [Learn more]({link})")
        st.session_state.checked[key] = checked
        if checked:
            checked_count += 1
    st.markdown("---")

# Progress
progress = int((checked_count / total_topics) * 100)
st.progress(progress, text=f"✅ {progress}% completed")

# Export Feature
st.markdown("## 📤 Export Your Progress")
if st.button("Download My Checklist (JSON)"):
    saved = {
        "completed": {k: v for k, v in st.session_state.checked.items() if v},
        "progress": f"{progress}%"
    }
    json_bytes = json.dumps(saved, indent=2).encode('utf-8')
    st.download_button(
        label="📄 Download Checklist",
        data=json_bytes,
        file_name="sql_learning_checklist.json",
        mime="application/json"
    )
