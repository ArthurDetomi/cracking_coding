function palindromePermutation(str: string): boolean {
  const map = new Map<string, number>();

  for (const c of str) {
    if (c === " ") continue;

    if (map.has(c)) {
      let count = map.get(c) ?? 0;

      map.set(c, count + 1);
    } else {
      map.set(c, 1);
    }
  }

  let isOdd = false;

  for (const c of map.keys()) {
    const value = map.get(c) ?? 0;

    if (isOdd) {
      return false;
    }

    if (value % 2 !== 0) {
      isOdd = true;
    }
  }

  return true;
}

function toggleBit(bitVector: number, value: number): number {
  let mask = 1 << value;

  if ((bitVector & mask) === 0) {
    bitVector |= mask;
  } else {
    bitVector &= ~mask;
  }

  return bitVector;
}

function checkExactlyOneBitSet(bitVector: number): boolean {
  return (bitVector & (bitVector - 1)) === 0;
}

function createBitVector(str: string): number {
  let bitVector = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") continue;

    const value = str.charCodeAt(i) - "a".charCodeAt(0);

    bitVector = toggleBit(bitVector, value);
  }

  return bitVector;
}

function palindromePermutationBitwise(str: string): boolean {
  let bitVector = createBitVector(str);

  return bitVector === 0 || checkExactlyOneBitSet(bitVector);
}

console.log(palindromePermutation("taco cat"));

console.log(palindromePermutationBitwise("taco cat"));
