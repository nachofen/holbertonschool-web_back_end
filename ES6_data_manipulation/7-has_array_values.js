export default function hasValuesFromArray(set, array) {
  const values = array.values();
  for (const value of values) {
    if (!set.has(value)) {
      return false;
    }
  }
  return true;
}
