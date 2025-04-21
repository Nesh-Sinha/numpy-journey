import numpy as np

file_path = r'D:\Python Programming\NumPy_journey\Student_Grades_Analysis\student_grades.csv'
# 'r' before the string makes it a raw string ,meaning skip sequences like \n or \t 


# Load names separately 
with open(file_path, 'r', encoding='utf-8') as f: # (path,mode, encoding='utf-8' for correct handling of text )
    lines = f.readlines() # reads all line from the file and store them asa a list ,each line being string

names = [line.split(',')[0] for line in lines[1:]]  # line.split(',')[0]: Splits each line by the comma , and grabs the first item

# Load only numeric data using NumPy
grades = np.genfromtxt(
    file_path,
    delimiter=',',
    skip_header=1, 
    usecols=(1, 2, 3, 4, 5),  # This tells NumPy to only load columns 1–5
    encoding='utf-8'
)

''' --- Mean Data --- '''

def meanData(i):
    student_name = names[i]
    student_scores = grades[i]
    avg = np.mean(student_scores)
    print(f"{student_name} - Average Marks: {avg:.2f}")


''' --- TOP 5 STUDENT ---'''
def top5students():
    avg_scores = np.mean(grades, axis =1)
    top_indices = np.argsort(avg_scores)[-5:][::-1]

    print("\n\n ----- TOP 5 Students ----- ")
    for idx in top_indices:
        print(f"{names[idx]} - Average Marks : {avg_scores[idx]:.2f}")


for i in range(len(grades)):
    meanData(i)

top5students()




