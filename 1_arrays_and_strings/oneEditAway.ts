function oneEditReplace(str1: string, str2: string): boolean {
  let foundDifference = false;

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) {
      if (foundDifference) return false;

      foundDifference = true;
    }
  }

  return true;
}

function oneEditInsert(str1: string, str2: string): boolean {
  let idx1 = 0;
  let idx2 = 0;

  while (idx1 < str1.length && idx2 < str2.length) {
    if (str1[idx1] !== str2[idx2]) {
      if (idx1 !== idx2) return false;

      idx2++;
    } else {
      idx1++;
      idx2++;
    }
  }

  return true;
}

function oneEditAway(str1: string, str2: string): boolean {
  if (str1.length === str2.length) {
    return oneEditReplace(str1, str2);
  } else if (str1.length + 1 === str2.length) {
    return oneEditInsert(str1, str2);
  } else if (str2.length + 1 === str1.length) {
    return oneEditInsert(str2, str1);
  }

  return true;
}

console.log(oneEditAway("pale", "ple")); // true

console.log(oneEditAway("pales", "pale")); // true

console.log(oneEditAway("pale", "bale")); // true

console.log(oneEditAway("pale", "bae")); // false
