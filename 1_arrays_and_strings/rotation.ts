function isRotation(s1: string, s2: string): boolean {
  if (s1.length > 0 && s1.length === s2.length) {
    const s1s1 = s1 + s1;

    return s1s1.includes(s2);
  }

  return false;
}

const s1 = "waterbottle";
const s2 = "erbottlewat";

console.log(isRotation(s1, s2));
