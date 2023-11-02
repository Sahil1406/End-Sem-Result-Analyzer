import pandas as pd
import streamlit as st 
import plotly_express as px

#---------setting up the page--------------

st.set_page_config(page_title="End Sem Analyzer",
                   page_icon=":bar_chart:",
                   layout="wide"
)
# with st.sidebar:
#     st.write("Welcome To End Sem Result Analyzer.")

#----------Reading the Data---------------

df = pd.read_excel(
    io='Data/Sem 4.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='A:L',
    nrows= 77,
)

# new_df = pd.read_excel(
#     io='Data/Sem 4.xlsx',
#     engine='openpyxl',
#     sheet_name='Sheet1',
#     skiprows=0,
#     usecols='A:G',
#     nrows= 77,
# )

# df.set_index("Seat No")
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

# passn = 0
# failn = 0

# for index, row in new_df.iterrows():
#     for column, value in row.items():
#         # Check if the value is numeric
#         if isinstance(value, (int, float)):
#             if value > 32:
#                 passn += 1
#             else:
#                 failn += 1

# print(passn)
# print(failn)



#----------------Displaying the Bar Graphs-----------------

O_grades : 0
A_grades : 0
B_grades : 0
C_grades : 0
D_grades : 0
E_grades : 0
P_grades : 0
F_grades : 0


Maths_fig= px.bar(
    df,
    x="Seat No",
    y="Engineering Mathematics- IV",
    orientation="v",
    title="<b>Engineering Mathematics 4</b>",
    color_discrete_sequence=["#45bb00"] * len("Roll No"),
    template="plotly_white",
)

aoa_fig = px.bar(
    df,
    x="Seat No",
    y="Analysis of Algorithm",
    orientation="v",
    title="<b>Analysis Of Algorithm</b>",
    color_discrete_sequence=["#0083BB"] * len("Roll No"),
    template="plotly_white",
)

dbms_fig= px.bar(
    df,
    x="Seat No",
    y="Database Management System",
    orientation="v",
    title="<b>Database Management System</b>",
    color_discrete_sequence=["#8600bb"] * len("Roll No"),
    template="plotly_white",
)

os_fig= px.bar(
    df,
    x="Seat No",
    y="Operating System",
    orientation="v",
    title="<b>Operating System</b>",
    color_discrete_sequence=["#bbb200"] * len("Roll No"),
    template="plotly_white",
)

mp_fig= px.bar(
    df,
    x="Seat No",
    y="Microprocessor",
    orientation="v",
    title="<b>Microprocessor</b>",
    color_discrete_sequence=["#bb002c"] * len("Roll No"),
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



st.plotly_chart(Maths_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Engineering Mathematics- IV')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Engineering Mathematics- IV is {values}')
with col2: 
    passed = passPercent(df, 'Engineering Mathematics- IV')
    st.write(f"From this semester, {passed} number of students out of 76 have passed in Engineering Mathematics- IV")
    percent = int((passed/76)*100)
    st.write(f"Therefore, {percent}% students have cleared Engineering Mathematics- IV")


st.plotly_chart(aoa_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Analysis of Algorithm')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Analysis of Algorithm is {values}')
with col2:
    passed = passPercent(df, 'Analysis of Algorithm')
    st.write(f"From this semester, {passed} number of students out of 76 have passed in Analysis of Algorithm")
    percent = int((passed/76)*100)
    st.write(f"Therefore, {percent}% students have cleared Analysis of Algorithm")


st.plotly_chart(dbms_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Database Management System')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Database Management System is {values}')
with col2:
    passed = passPercent(df, 'Database Management System')
    st.write(f"From this semester, {passed} number of students out of 76 have passed in Database Management System")
    percent = int((passed/76)*100)
    st.write(f"Therefore, {percent}% students have cleared Database Management System")


st.plotly_chart(os_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Operating System')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Operating System is {values}')
with col2:
    passed = passPercent(df, 'Operating System')
    st.write(f"From this semester, {passed} number of students out of 76 have passed in Operating System")
    percent = int((passed/76)*100)
    st.write(f"Therefore, {percent}% students have cleared Operating System")


st.plotly_chart(mp_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Microprocessor')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Microprocessor is {values}')
with col2:
    passed = passPercent(df, 'Microprocessor')
    st.write(f"From this semester, {passed} number of students out of 76 have passed in Microprocessor")
    percent = int((passed/76)*100)
    st.write(f"Therefore, {percent}% students have cleared Microprocessor")

# st.header("This Is The Table of the Grades of Student in the last 3 years")
# st.dataframe(new_df)

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


#streamlit run Sem4.py