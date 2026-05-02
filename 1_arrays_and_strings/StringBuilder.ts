class StringBuilder {
  private data: string[];

  constructor() {
    this.data = [];
  }

  append(str: string) {
    this.data.push(str);
  }

  toString(): string {
    return this.data.join("");
  }
}

const STB = new StringBuilder();

STB.append("Arthur");

STB.append("Detomi");

STB.append("Juca");

console.log(STB.toString());
