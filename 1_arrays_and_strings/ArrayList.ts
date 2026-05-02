class ArrayList {
  size: number;
  data: number[];
  capacity: number;

  constructor(length: number) {
    this.size = 0;
    this.data = new Array(length);
    this.capacity = length;
  }

  append(value: number) {
    if (this.size >= this.capacity) {
      const newCapacity = this.capacity * 2;

      const newData: number[] = new Array(newCapacity);

      for (let i = 0; i < this.size; i++) {
        newData[i] = this.data[i];
      }

      this.capacity = newCapacity;
      this.data = newData;
    }

    this.data[this.size] = value;

    this.size++;
  }
}

let A = new ArrayList(2);

A.append(2);
A.append(3);

A.append(4);
A.append(7);

console.log(A);
