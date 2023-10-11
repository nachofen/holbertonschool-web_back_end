export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  const updatedStudents = listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
      let grade = 0;
      if (matchingGrade) {
        grade = matchingGrade.grade;
      } else {
        grade = 'N/A';
      }
      return {
        ...student,
        grade,
      };
    });

  return updatedStudents;
}
