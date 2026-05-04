import { NodeLinked } from "./LinkedList";

function removeDups(list: NodeLinked) {
  const CONTAINER = new Set();

  let currentNode: NodeLinked | null = list;

  let previousNode = currentNode;

  while (currentNode !== null) {
    if (CONTAINER.has(currentNode.data)) {
      previousNode.next = currentNode.next;
    }

    CONTAINER.add(currentNode.data);

    previousNode = currentNode;
    currentNode = currentNode.next;
  }
}

let L: NodeLinked | null = new NodeLinked(1);

L = L.appendToTail(2);

L = L.appendToTail(3);

L = L.appendToTail(1);

L = L.appendToTail(5);

L = L.appendToTail(2);

if (L) L.printList();

removeDups(L);

L.printList();
