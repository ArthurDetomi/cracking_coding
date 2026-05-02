interface HashData {
  key: string;
  value: object;
}

class HashTable {
  data: Array<Array<HashData>>;
  length: number;

  constructor(length: number) {
    this.data = Array.from({ length }, () => []);
    this.length = length;
  }

  hashCode(key: string) {
    let hash = 0;

    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * (i + 1)) % this.length;
    }

    return hash;
  }

  insert(key: string, value: object) {
    let index = this.hashCode(key);

    // Caso já tenha a chave
    for (let i = 0; i < this.data[index].length; i++) {
      if (key === this.data[index][i].key) {
        this.data[index][i].value = value;
        return;
      }
    }

    this.data[index].push({ key, value });
  }

  find(key: string) {
    let index = this.hashCode(key);

    for (let i = 0; i < this.data[index].length; i++) {
      if (key === this.data[index][i].key) {
        return this.data[index][i].value;
      }
    }

    return undefined;
  }
}

const H = new HashTable(10);

H.insert("Arthur", { name: "Arthur" });

H.insert("Joao", { name: "Joao" });

H.insert("mariaas", { name: "mariaas" });

H.insert("Antonia", { name: "Antonia" });

console.log(H);
console.log(H.find("Detomi"));

console.log(H.find("Antonia"));

console.log(H.find("Lula"));
