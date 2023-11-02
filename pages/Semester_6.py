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
    io='Data/Sem6.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='A:L',
    nrows= 76,
)



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

# st.write("From this Semester, there were no drops.")
# st.write("This Semester the result was 100%")


#----------------Displaying the Bar Graphs-----------------

O_grades : 0
A_grades : 0
B_grades : 0
C_grades : 0
D_grades : 0
E_grades : 0
P_grades : 0
F_grades : 0


dva_fig= px.bar(
    df,
    x="Seat No",
    y="Data Analytics and Visualization",
    orientation="v",
    title="<b>Data Analytics and Visualization</b>",
    color_discrete_sequence=["#45bb00"] * len("Seat No"),
    template="plotly_white",
)

crypt_fig = px.bar(
    df,
    x="Seat No",
    y="Cryptography and System Security",
    orientation="v",
    title="<b>Cryptography and System Security</b>",
    color_discrete_sequence=["#0083BB"] * len("Seat No"),
    template="plotly_white",
)

sepm_fig = px.bar(
    df,
    x="Seat No",
    y="Software Engineering and Project Management",
    orientation="v",
    title="<b>Software Engineering and Project Management</b>",
    color_discrete_sequence=["#bb002c"] * len("Seat No"),
    template="plotly_white",
)

ml_fig= px.bar(
    df,
    x="Seat No",
    y="Machine Learning",
    orientation="v",
    title="<b>Machine Learning</b>",
    color_discrete_sequence=["#8600bb"] * len("Seat No"),
    template="plotly_white",
)

dc_fig= px.bar(
    df,
    x="Seat No",
    y="Distributed Computing",
    orientation="v",
    title="<b>Distributed Computing</b>",
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

st.plotly_chart(dva_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Data Analytics and Visualization')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Data Analytics and Visualization is {values}')
with col2:
    passed = passPercent(df, 'Data Analytics and Visualization')
    st.write(f"From this semester, {passed} number of students have passed in Data Analytics and Visualization")
    percent = int((passed/75)*100)
    st.write(f"Therefore, {percent}% students have cleared Data Analytics and Visualization")


st.plotly_chart(crypt_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Cryptography and System Security')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Cryptography and System Security is {values}')
with col2:
    passed = passPercent(df, 'Cryptography and System Security')
    st.write(f"From this semester, {passed} number of students have passed in Cryptography and System Security")
    percent = int((passed/75)*100)
    st.write(f"Therefore, {percent}% students have cleared Cryptography and System Security")


st.plotly_chart(sepm_fig)
col1 , col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Software Engineering and Project Management')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Software Engineering and Project Management is {values}')

with col2:
    passed = passPercent(df, 'Software Engineering and Project Management')
    st.write(f"From this semester, {passed} number of students have passed in Software Engineering and Project Management")
    percent = int((passed/75)*100)
    st.write(f"Therefore, {percent}% students have cleared Software Engineering and Project Management")


st.plotly_chart(ml_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Machine Learning')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Machine Learning is {values}')

with col2:
    passed = passPercent(df, 'Machine Learning')
    st.write(f"From this semester, {passed} number of students have passed in Machine Learning")
    percent = int((passed/75)*100)
    st.write(f"Therefore, {percent}% students have cleared Machine Learning")


st.plotly_chart(dc_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Distributed Computing')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Distributed Computing is {values}')
 
with col2:
    passed = passPercent(df, 'Distributed Computing')
    st.write(f"From this semester, {passed} number of students have passed in Distributed Computing")
    percent = int((passed/75)*100)
    st.write(f"Therefore, {percent}% students have cleared Distributed Computing")
 
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