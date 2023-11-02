import pandas as pd
import streamlit as st 
import plotly_express as px

#---------setting up the page--------------

st.set_page_config(page_title="End Sem Analyzer",
                   page_icon=":bar_chart:",
                   layout="wide"
)
# st.sidebar.success("Select the Semester you want to see")

#----------Reading the Data---------------

df = pd.read_excel(
    io='Data/Sem5 IOT.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='A:K',
    nrows= 40,
)

# new_df = pd.read_csv('grades.csv')
# print(new_df)
# df.set_index('Roll No')
# print(df)
# df.set_index('Roll No')
# print(df)




#----------------Sidebar and Sorting-----------------

st.header("End Semester Result")
st.header("Please Filter According To The Students")
student = st.multiselect(
    "Select the Student:",
    options=df['Student'].unique(),
    default=df['Student'].unique()
)

df_selection = df.query(
    "Student == @student"
)


st.markdown("This is an interactive table. You can choose which students marks you want to see from their Roll No")

st.dataframe(df_selection)

st.write("From this Semester, 21 students out of 38 cleared all the Subjects.")
pass_percent = int((21/38)*100)
st.write(f"The Passing Percent for this Semester is {pass_percent}%")

#----------------Displaying the Bar Graphs-----------------

O_grades : 0
A_grades : 0
B_grades : 0
C_grades : 0
D_grades : 0
E_grades : 0
P_grades : 0
F_grades : 0


cn_fig= px.bar(
    df,
    x="Seat No",
    y="Computer Network",
    orientation="v",
    title="<b>Computer Network</b>",
    color_discrete_sequence=["#45bb00"] * len("Seat No"),
    template="plotly_white",
)

wc_fig = px.bar(
    df,
    x="Seat No",
    y="Web Computing",
    orientation="v",
    title="<b>Web Computing</b>",
    color_discrete_sequence=["#0083BB"] * len("Seat No"),
    template="plotly_white",
)

ai_fig= px.bar(
    df,
    x="Seat No",
    y="Artificial Intelligence",
    orientation="v",
    title="<b>Artificial Intelligence</b>",
    color_discrete_sequence=["#bb002c"] * len("Seat No"),
    template="plotly_white",
)

dwm_fig= px.bar(
    df,
    x="Seat No",
    y="Data Warehousing & Mining",
    orientation="v",
    title="<b>Data Warehousing & Mining</b>",
    color_discrete_sequence=["#8600bb"] * len("Seat No"),
    template="plotly_white",
)

iot_fig= px.bar(
    df,
    x="Seat No",
    y="Internet of Things",
    orientation="v",
    title="<b>Internet of Things</b>",
    color_discrete_sequence=["#bbb200"] * len("Seat No"),
    template="plotly_white",
)


# for value in df["Engineering Mathematics - IV"]:
#     if value >= 85:
#         O_grades +=1
#     elif 80 >= value >= 75:
#         A_grades +=1
#     elif 75 > value >= 70:
#         B_grades +=1
#     elif 70 > value >= 60:
#         C_grades +=1
#     elif 60 > value >= 50:
#         D_grades +=1
#     elif 50 > value >= 45:
#         E_grades +=1
#     elif 45 > value >= 40:
#         P_grades +=1
#     else:
#         F_grades +=1


# print(D_grades)

          





def categorize_grades(dataframe, column_name):
    # Initialize a dictionary to count grades
    grade_counts = {
        'O': 0,
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'P': 0,
        'F': 0
    }

    for value in dataframe[column_name]:
        if value >= 80:
            grade_counts['O'] += 1
        elif 80 >= value >= 75:
            grade_counts['A'] += 1
        elif 75 > value >= 70:
            grade_counts['B'] += 1
        elif 70 > value >= 60:
            grade_counts['C'] += 1
        elif 60 > value >= 50:
            grade_counts['D'] += 1
        elif 50 > value >= 45:
            grade_counts['E'] += 1
        elif 45 > value >= 40:
            grade_counts['P'] += 1
        else:
            grade_counts['F'] += 1

    return grade_counts

def passPercent(dataframe, column_name):
    passn = 0
    failn = 0

    for value in dataframe[column_name]:
        if value > 32:
            passn += 1
        else:
            failn += 1
    return passn

st.plotly_chart(cn_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Computer Network')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Computer Network is {values}')
with col2:
    passed = passPercent(df, 'Computer Network')
    st.write(f"From this semester, {passed} number of students out of 39 have passed in Computer Network")
    percent = int((passed/39)*100)
    st.write(f"Therefore, {percent}% students have cleared Computer Network")



st.plotly_chart(wc_fig)
col1, col2 = st.columns(2)
with col1: 
    grades_counts = categorize_grades(df, 'Web Computing')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Web Computing is {values}')
with col2:
    passed = passPercent(df, 'Web Computing')
    st.write(f"From this semester, {passed} number of students out of 39 have passed in Web Computing")
    percent = int((passed/39)*100)
    st.write(f"Therefore, {percent}% students have cleared Web Computing")


st.plotly_chart(ai_fig)
col1, col2 = st.columns(2)
with col1: 
    grades_counts = categorize_grades(df, 'Artificial Intelligence')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Artificial Intelligence is {values}')
with col2:
    passed = passPercent(df, 'Artificial Intelligence')
    st.write(f"From this semester, {passed} number of students out of 39 have passed in Artificial Intelligence")
    percent = int((passed/39)*100)
    st.write(f"Therefore, {percent}% students have cleared Artificial Intelligence")


st.plotly_chart(dwm_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Data Warehousing & Mining')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Data Warehousing & Mining is {values}')
with col2:
    passed = passPercent(df, 'Data Warehousing & Mining')
    st.write(f"From this semester, {passed} number of students out of 39 have passed in Data Warehousing & Mining")
    percent = int((passed/39)*100)
    st.write(f"Therefore, {percent}% students have cleared Data Warehousing & Mining")

st.plotly_chart(iot_fig)
col1, col2 = st.columns(2)
with col1: 
    grades_counts = categorize_grades(df, 'Internet of Things')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Internet of Things is {values}')
with col2:
    passed = passPercent(df, 'Internet of Things')
    st.write(f"From this semester, {passed} number of students out of 39 have passed in Internet of Things")
    percent = int((passed/39)*100)
    st.write(f"Therefore, {percent}% students have cleared Internet of Things")
 
# st.header("This Is The Table of the Grades of Student in the last 3 years")

grade = {
        'O': 0,
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'P': 0,
        'F': 0
    }

for index, row in df.iterrows():
    for column, value in row.items():
        # Check if the value is numeric
        if isinstance(value, (int, float)):
            if value >= 85:
                grade['O'] += 1
            elif 80 >= value >= 75:
                grade['A'] += 1
            elif 75 > value >= 70:
                grade['B'] += 1
            elif 70 > value >= 60:
                grade['C'] += 1
            elif 60 > value >= 50:
                grade['D'] += 1
            elif 50 > value >= 45:
                grade['E'] += 1
            elif 45 > value >= 40:
                grade['P'] += 1
            else:
                grade['F'] += 1
        else:
            # Handle non-numeric values (e.g., strings)
            # You can add error handling or skip non-numeric values as needed
            pass

fig = px.pie(
    names=list(grade.keys()),  # Grade labels
    values=list(grade.values()),  # Grade counts
    title='Grade Distribution'
)
st.plotly_chart(fig)

#streamlit run Sem 4 22_23.py