export default function getStudentIdsSum(studentList) {
  const onlyIds = studentList.map((student) => student.id);
  const sum = onlyIds.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  return sum;
}
