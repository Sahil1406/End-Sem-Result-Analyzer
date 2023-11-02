import pandas as pd
import streamlit as st 
import plotly_express as px

#---------setting up the page--------------

st.set_page_config(page_title="End Sem Analyzer",
                   page_icon=":bar_chart:",
                   layout="wide"
)

#----------Reading the Data---------------

df = pd.read_excel(
    io='Data/Sem3 DSE.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='A:J',
    nrows= 32,
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

st.write("From this Semester, there were no drops.")
st.write("This Semester the result was 100%")

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
    y="Engineering Mathematics- III",
    orientation="v",
    title="<b>Engineering Mathematics 3</b>",
    color_discrete_sequence=["#45bb00"] * len("Seat No"),
    template="plotly_white",
)

dsgt_fig = px.bar(
    df,
    x="Seat No",
    y="Discrete Structures and Graph Theory",
    orientation="v",
    title="<b>Discrete Structures and Graph Theory</b>",
    color_discrete_sequence=["#0083BB"] * len("Seat No"),
    template="plotly_white",
)

ds_fig= px.bar(
    df,
    x="Seat No",
    y="Data Structures",
    orientation="v",
    title="<b>Data Structures</b>",
    color_discrete_sequence=["#bb002c"] * len("Seat No"),
    template="plotly_white",
)

dlca_fig= px.bar(
    df,
    x="Seat No",
    y="Digital Logic & Computer Architecture",
    orientation="v",
    title="<b>Digital Logic & Computer Architecture</b>",
    color_discrete_sequence=["#8600bb"] * len("Seat No"),
    template="plotly_white",
)

cg_fig= px.bar(
    df,
    x="Seat No",
    y="Computer Graphics",
    orientation="v",
    title="<b>Computer Graphics</b>",
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

st.plotly_chart(Maths_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Engineering Mathematics- III')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Engineering Mathematics- III is {values}')
with col2:
    passed = passPercent(df, 'Engineering Mathematics- III')
    st.write(f"From this semester, {passed} number of students have passed in Engineering Mathematics- III")
    percent = int((passed/31)*100)
    st.write(f"Therefore, {percent}% students have cleared Engineering Mathematics- III")


st.plotly_chart(dsgt_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Discrete Structures and Graph Theory')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Discrete Structures and Graph Theory is {values}')
with col2:
    passed = passPercent(df, 'Discrete Structures and Graph Theory')
    st.write(f"From this semester, {passed} number of students have passed in Discrete Structures and Graph Theory")
    percent = int((passed/31)*100)
    st.write(f"Therefore, {percent}% students have cleared Discrete Structures and Graph Theory")

st.plotly_chart(ds_fig)
col1 , col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Data Structures')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Data Structures is {values}')

with col2:
    passed = passPercent(df, 'Data Structures')
    st.write(f"From this semester, {passed} number of students have passed in Data Structures")
    percent = int((passed/31)*100)
    st.write(f"Therefore, {percent}% students have cleared Data Structures")


st.plotly_chart(dlca_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Digital Logic & Computer Architecture')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Digital Logic & Computer Architecture is {values}')

with col2:
    passed = passPercent(df, 'Digital Logic & Computer Architecture')
    st.write(f"From this semester, {passed} number of students have passed in Digital Logic & Computer Architecture")
    percent = int((passed/31)*100)
    st.write(f"Therefore, {percent}% students have cleared Digital Logic & Computer Architecture")

st.plotly_chart(cg_fig)
col1, col2 = st.columns(2)
with col1:
    grades_counts = categorize_grades(df, 'Computer Graphics')
    for key, values in grades_counts.items():
        st.write(f'The number of {key} Grades in Computer Graphics is {values}')
 
with col2:
    passed = passPercent(df, 'Computer Graphics')
    st.write(f"From this semester, {passed} number of students have passed in Computer Graphics")
    percent = int((passed/31)*100)
    st.write(f"Therefore, {percent}% students have cleared Computer Graphics")

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