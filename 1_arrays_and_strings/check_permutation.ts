function sortString(str: string): string {
  return str.split("").sort().join("");
}

const checkPermutation = (str1: string, str2: string): boolean => {
  if (str1.length !== str2.length) return false;
  return sortString(str1) === sortString(str2);
};

function checkPermutation2(str1: string, str2: string): boolean {
  if (str1.length !== str2.length) return false;

  const letters = new Array(128).fill(0);

  for (let i = 0; i < str1.length; i++) {
    let value = str1.charCodeAt(i);

    letters[value]++;
  }

  for (let i = 0; i < str2.length; i++) {
    let value = str2.charCodeAt(i);

    letters[value]--;

    if (letters[value] < 0) {
      return false;
    }
  }

  return true;
}

const str1 = "abacaxi";

const str2 = "baaacix";

console.log(checkPermutation(str1, str2));

console.log(checkPermutation2(str1, str2));
