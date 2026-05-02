interface Pos {
  line: number;
  column: number;
}

// n > m ? O(n) : O(m)
function setZeroInLinesAndColumns(
  matrix: Array<Array<number>>,
  pos: Pos,
  m: number,
  n: number,
): void {
  // To pass lines for 0
  for (let i = 0; i < n; i++) {
    matrix[pos.line][i] = 0;
  }
  // To pass columns for 0
  for (let i = 0; i < m; i++) {
    matrix[i][pos.column] = 0;
  }
}

// O(m*n)
function zeroMatrixMy(
  matrix: Array<Array<number>>,
  m: number,
  n: number,
): void {
  const positions: Pos[] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === 0) {
        positions.push({ line: i, column: j });
      }
    }
  }

  // O(positions.length * (n > m ? O(n) : O(m))
  for (let i = 0; i < positions.length; i++) {
    setZeroInLinesAndColumns(matrix, positions[i], m, n);
  }
}

const mat = [
  [1, 2, 3],
  [4, 5, 0],
  [0, 2, 4],
];

zeroMatrixMy(mat, 3, 3);

console.log(mat);
