const isUniqueUsingSet = (input: string): boolean => {
  return new Set(input).size === input.length;
};

const isUniqueArray = (input: string): boolean => {
  const ALPHA_LENGTH = 128;

  if (input.length > ALPHA_LENGTH) {
    return false;
  }

  const char_set = new Array(ALPHA_LENGTH).fill(false);

  for (let i = 0; i < input.length; i++) {
    let value = input.charCodeAt(i);

    if (char_set[value]) {
      return false;
    }

    char_set[value] = true;
  }

  return true;
};

const isUniqueBit = (input: string): boolean => {
  let checker = 0;

  for (let i = 0; i < input.length; i++) {
    let value = input.charCodeAt(i) - "a".charCodeAt(0);

    if (value < 0 || value > 25) {
      throw new Error("Apenas letras minúsculas são permitidas");
    }

    if ((checker & (1 << value)) !== 0) {
      return false;
    }

    checker |= 1 << value;
  }

  return true;
};

const isUniqueSort = (input: string): boolean => {
  const ordenedStr = input.split("").sort();

  for (let i = 0; i < ordenedStr.length - 1; i++) {
    if (ordenedStr[i] === ordenedStr[i + 1]) {
      return false;
    }
  }

  return true;
};

// not unique
let input = "abcdefgha";

console.log(isUniqueUsingSet(input));

console.log(isUniqueArray(input));

console.log(isUniqueBit(input));

console.log(isUniqueSort(input));

// unique
input = "abcdefgh";

console.log(isUniqueUsingSet(input));

console.log(isUniqueArray(input));

console.log(isUniqueBit(input));

console.log(isUniqueSort(input));
