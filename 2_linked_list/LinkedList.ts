export class NodeLinked {
  next: NodeLinked | null;
  data: number;

  constructor(data: number | undefined) {
    this.next = null;
    this.data = data ?? 0;
  }

  appendToTail(data: number) {
    let currentNode: NodeLinked = this;

    while (currentNode.next !== null) {
      currentNode = currentNode.next;
    }

    const newNode = new NodeLinked(data);

    currentNode.next = newNode;

    return this;
  }

  deleteNode(data: number) {
    let currentNode: NodeLinked | null = this;

    if (currentNode.data === data) {
      return currentNode.next;
    }

    let nodeToDelete = null;

    let previousNode: NodeLinked | null = currentNode;

    while (currentNode !== null) {
      if (currentNode.data === data) {
        nodeToDelete = currentNode;
        break;
      }

      previousNode = currentNode;

      currentNode = currentNode.next ?? null;
    }

    if (nodeToDelete === null) {
      return this;
    }

    if (currentNode && currentNode.next !== null) {
      previousNode.next = currentNode.next;
    } else {
      previousNode.next = null;
    }

    return this;
  }

  printList() {
    let currentNode: NodeLinked | null = this;

    const arr = [];

    while (currentNode !== null) {
      arr.push(currentNode.data);

      currentNode = currentNode.next;
    }

    console.log(arr);
  }
}

let L: NodeLinked | null = new NodeLinked(1);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(5);

if (L) L = L.deleteNode(1);

if (L) L.printList();
