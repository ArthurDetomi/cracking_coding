function urlify(str: string, n: number): string {
  let countSpaces = 0;

  for (let i = 0; i < n; i++) {
    if (str[i] === " ") {
      countSpaces++;
    }
  }

  const size = n + countSpaces * 2;

  let idx = 0;

  const response = new Array(size);

  for (let i = 0; i < n; i++) {
    if (str[i] === " ") {
      response[idx++] = "%";
      response[idx++] = "2";
      response[idx++] = "0";
    } else {
      response[idx++] = str[i];
    }
  }

  return response.join("");
}

console.log(urlify("Mr John Smith     ", 13));
